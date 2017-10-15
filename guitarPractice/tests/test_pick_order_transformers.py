from unittest import TestCase

from guitarPractice.exercise_builder.pick_order_transformers import (
    ascending_transformer,
    ascending_and_descending_transformer,
    ascending_skip_transformer
)


class TestAscendingTransformer(TestCase):
    def test_ascending_transformer_returns_notes_in_ascending_order(self):
        note_sequence = ascending_transformer([1, 2, 3, 4, 5])

        self.assertEqual(len(note_sequence), 5)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 5])

    def test_ascending_transformer_can_shorten_sequence_when_length_value_is_set(self):
        note_sequence = ascending_transformer([1, 2, 3, 4, 5], sequence_length=3)

        self.assertEqual(len(note_sequence), 3)
        self.assertEqual(note_sequence, [1, 2, 3])

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_shape_length(self):
        note_sequence = ascending_transformer([1, 2, 3, 4, 5], sequence_length=8)

        self.assertEqual(len(note_sequence), 8)
        self.assertEqual([1, 2, 3, 4, 5, 3, 4, 5], note_sequence)

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_double_shape_length(self):
        note_sequence = ascending_transformer([1, 2, 3, 4, 5], sequence_length=13)

        self.assertEqual(len(note_sequence), 13)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 4, 5])

    def test_ascending_transformer_will_repeat_notes_when_length_is_multiple_of_shape_length(self):
        note_sequence = ascending_transformer([1, 2, 3, 4], sequence_length=12)

        self.assertEqual(len(note_sequence), 12)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])


class TestAscendingAndDescendingTransformer(TestCase):
    def test_returns_notes_in_ascending_and_descending_order(self):
        note_sequence = ascending_and_descending_transformer([1, 2, 3, 4])

        self.assertEqual(note_sequence, [1, 2, 3, 4, 3, 2])

    def test_can_shorten_sequence(self):
        note_sequence = ascending_and_descending_transformer([1, 2, 3, 4], sequence_length=4)

        self.assertEqual(note_sequence, [1, 2, 4, 3])

    def test_can_lengthen_sequence(self):
        note_sequence = ascending_and_descending_transformer([1, 2, 3, 4], sequence_length=8)

        self.assertEqual(note_sequence, [1, 2, 3, 4, 4, 3, 2, 1])

    def test_can_lengthen_sequence_beyond_multiple_of_length(self):
        note_sequence = ascending_and_descending_transformer([1, 2, 3, 4], sequence_length=10)

        self.assertEqual(note_sequence, [1, 2, 3, 4, 4, 3, 2, 1, 2, 1])


class TestAscendingSkipTransformer(TestCase):
    def test_returns_notes_in_ascending_order(self):
        note_sequence = ascending_skip_transformer(([1, 2, 3, 4]))

        self.assertEqual(note_sequence, [1, 2, 3, 4])

    def test_plays_first_note_then_skips_to_last_notes_when_length_set(self):
        note_sequence = ascending_skip_transformer(([1, 2, 3, 4, 5, 6]), sequence_length=4)

        self.assertEqual(note_sequence, [1, 4, 5, 6])

    def test_extends_sequence_if_less_than_length(self):
        note_sequence = ascending_skip_transformer(([1, 2, 3]), sequence_length=5)

        self.assertEqual(note_sequence, [1, 2, 3, 2, 3])

    def test_shortens_sequence_playing_first_note(self):
        note_sequence = ascending_skip_transformer(([1, 2, 3, 4, 5]), sequence_length=4)

        self.assertEqual(note_sequence, [1, 3, 4, 5])