from unittest import TestCase

from guitarPractice.exercise_builder.transformers.order import (
    ascending,
    asc_and_desc,
    ascending_skip,
    asc_and_desc_skip,
    repeat_first,
    descending
)


class TestAscendingTransformer(TestCase):
    def test_ascending_transformer_returns_notes_in_ascending_order(self):
        note_sequence = ascending([1, 2, 3, 4, 5])

        self.assertEqual(5, len(note_sequence))
        self.assertEqual([1, 2, 3, 4, 5], note_sequence)

    def test_ascending_transformer_can_shorten_sequence_when_length_value_is_set(self):
        note_sequence = ascending([1, 2, 3, 4, 5], sequence_length=3)

        self.assertEqual(3, len(note_sequence))
        self.assertEqual([1, 2, 3], note_sequence)

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_shape_length(self):
        note_sequence = ascending([1, 2, 3, 4, 5], sequence_length=8)

        self.assertEqual(8, len(note_sequence))
        self.assertEqual([1, 2, 3, 4, 5, 3, 4, 5], note_sequence)

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_double_shape_length(self):
        note_sequence = ascending([1, 2, 3, 4, 5], sequence_length=13)

        self.assertEqual(13, len(note_sequence))
        self.assertEqual([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 4, 5], note_sequence)

    def test_ascending_transformer_will_repeat_notes_when_length_is_multiple_of_shape_length(self):
        note_sequence = ascending([1, 2, 3, 4], sequence_length=12)

        self.assertEqual(len(note_sequence), 12)
        self.assertEqual([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], note_sequence)


class TestDescendingTransformer(TestCase):
    def test_ascending_transformer_returns_notes_in_descending_order(self):
        note_sequence = descending([1, 2, 3, 4, 5])

        self.assertEqual(5, len(note_sequence))
        self.assertEqual([5, 4, 3, 2, 1], note_sequence)

    def test_descending_transformer_can_shorten_sequence_when_length_value_is_set(self):
        note_sequence = descending([1, 2, 3, 4, 5], sequence_length=3)

        self.assertEqual(3, len(note_sequence))
        self.assertEqual([5, 4, 3], note_sequence)

    def test_descending_transformer_will_repeat_notes_if_length_is_greater_than_shape_length(self):
        note_sequence = descending([1, 2, 3, 4, 5], sequence_length=8)

        self.assertEqual(8, len(note_sequence))
        self.assertEqual([5, 4, 3, 2, 1, 3, 2, 1], note_sequence)

    def test_descending_transformer_will_repeat_notes_if_length_is_greater_than_double_shape_length(self):
        note_sequence = descending([1, 2, 3, 4, 5], sequence_length=13)

        self.assertEqual(13, len(note_sequence))
        self.assertEqual([5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 3, 2, 1], note_sequence)

    def test_descending_transformer_will_repeat_notes_when_length_is_multiple_of_shape_length(self):
        note_sequence = descending([1, 2, 3, 4], sequence_length=12)

        self.assertEqual(len(note_sequence), 12)
        self.assertEqual([4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1], note_sequence)


class TestAscendingAndDescendingTransformer(TestCase):
    def test_returns_notes_in_ascending_and_descending_order(self):
        note_sequence = asc_and_desc([1, 2, 3, 4])

        self.assertEqual([1, 2, 3, 4, 3, 2], note_sequence)

    def test_can_shorten_sequence(self):
        note_sequence = asc_and_desc([1, 2, 3, 4], sequence_length=4)

        self.assertEqual([1, 2, 4, 3], note_sequence)

    def test_can_lengthen_sequence(self):
        note_sequence = asc_and_desc([1, 2, 3, 4], sequence_length=8)

        self.assertEqual([1, 2, 3, 4, 4, 3, 2, 1], note_sequence)

    def test_can_lengthen_sequence_beyond_multiple_of_length(self):
        note_sequence = asc_and_desc([1, 2, 3, 4], sequence_length=10)

        self.assertEqual([1, 2, 3, 4, 4, 3, 2, 1, 2, 1], note_sequence)

    def test_can_set_length_to_an_uneven_number(self):
        note_sequence = asc_and_desc([1, 2], sequence_length=3)

        self.assertEqual([1, 2, 1], note_sequence)


class TestAscendingSkipTransformer(TestCase):
    def test_returns_notes_in_ascending_order(self):
        note_sequence = ascending_skip(([1, 2, 3, 4]))

        self.assertEqual([1, 2, 3, 4], note_sequence)

    def test_plays_first_note_then_skips_to_last_notes_when_length_set(self):
        note_sequence = ascending_skip(([1, 2, 3, 4, 5, 6]), sequence_length=4)

        self.assertEqual([1, 4, 5, 6], note_sequence)

    def test_extends_sequence_if_less_than_length(self):
        note_sequence = ascending_skip(([1, 2, 3]), sequence_length=5)

        self.assertEqual([1, 2, 3, 2, 3], note_sequence)

    def test_shortens_sequence_playing_first_note(self):
        note_sequence = ascending_skip(([1, 2, 3, 4, 5]), sequence_length=4)

        self.assertEqual([1, 3, 4, 5], note_sequence)


class AscendingAndDescendingSkipTransformer(TestCase):
    def test_returns_notes_in_asc_and_desc_order(self):
        note_sequence = asc_and_desc_skip(([1, 2, 3, 4]))

        self.assertEqual([1, 2, 3, 4, 3, 2], note_sequence)

    def test_plays_first_note_and_skips_notes_when_length_is_set(self):
        note_sequence = asc_and_desc_skip(([1, 2, 3, 4]), sequence_length=4)

        self.assertEqual([1, 3, 4, 3], note_sequence)

    def test_plays_repeats_notes_when_length_is_uneven(self):
        note_sequence = asc_and_desc_skip(([1, 2, 3, 4]), sequence_length=5)

        self.assertEqual([1, 3, 4, 4, 3], note_sequence)

    def test_extends_sequence_when_less_than_length(self):
        note_sequence = asc_and_desc_skip(([1, 2, 3, 4]), sequence_length=8)

        self.assertEqual([1, 2, 3, 4, 4, 3, 2, 1], note_sequence)

    def test_shortens_long_sequences(self):
        note_sequence = asc_and_desc_skip(([1, 2, 3, 4, 5, 6]), sequence_length=8)

        self.assertEqual([1, 3, 4, 5, 6, 5, 4, 3], note_sequence)


class TestRepeatFirstTransformer(TestCase):
    def test_every_other_position_is_the_first_note(self):
        note_sequence = repeat_first([1, 2, 3, 4])

        self.assertEqual([1, 2, 1, 3, 1, 4], note_sequence)

    def test_length_can_match(self):
        note_sequence = repeat_first([1, 2, 3, 4], 6)

        self.assertEqual([1, 2, 1, 3, 1, 4], note_sequence)

    def test_length_can_be_extended(self):
        note_sequence = repeat_first([1, 2, 3, 4], 10)

        self.assertEqual([1, 2, 1, 3, 1, 4, 1, 3, 1, 4], note_sequence)

    def test_length_can_be_shortened(self):
        note_sequence = repeat_first([1, 2, 3, 4], 4)

        self.assertEqual([1, 2, 1, 3], note_sequence)

    def test_length_can_be_extended_to_an_odd_number(self):
        note_sequence = repeat_first([1, 2, 3, 4], 7)

        self.assertEqual([1, 2, 1, 3, 1, 4, 1], note_sequence)

    def test_length_can_be_shortened_to_an_odd_number(self):
        note_sequence = repeat_first([1, 2, 3, 4], 5)

        self.assertEqual([1, 2, 1, 3, 1], note_sequence)
