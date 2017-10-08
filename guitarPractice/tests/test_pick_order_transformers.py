from unittest import TestCase
from guitarPractice.exercise_builder import pick_order_transformers


class TestAscendingTransformer(TestCase):
    def test_ascending_transformer_returns_notes_in_ascending_order(self):
        note_sequence = pick_order_transformers.ascending_transformer([1, 2, 3, 4, 5])

        self.assertEqual(len(note_sequence), 5)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 5])

    def test_ascending_transformer_can_shorten_sequence_when_length_value_is_set(self):
        note_sequence = pick_order_transformers.ascending_transformer([1, 2, 3, 4, 5], sequence_length=3)

        self.assertEqual(len(note_sequence), 3)
        self.assertEqual(note_sequence, [1, 2, 3])

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_shape_length(self):
        note_sequence = pick_order_transformers.ascending_transformer([1, 2, 3, 4, 5], sequence_length=8)

        self.assertEqual(len(note_sequence), 8)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 5, 3, 4, 5])

    def test_ascending_transformer_will_repeat_notes_if_length_is_greater_than_double_shape_length(self):
        note_sequence = pick_order_transformers.ascending_transformer([1, 2, 3, 4, 5], sequence_length=13)

        self.assertEqual(len(note_sequence), 13)
        self.assertEqual(note_sequence, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 4, 5])
