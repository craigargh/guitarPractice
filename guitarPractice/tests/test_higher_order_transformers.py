from unittest import TestCase
from unittest.mock import patch, Mock

from guitarPractice.exercise_builder.higher_order_transformers import make_consistent_random_transformer


class TestMakeConsistentRandomOrderTransformer(TestCase):
    @patch('random.sample', Mock(return_value=[0, 2, 1, 3]))
    def test_notes_are_returned_in_random_order(self):
        transformer = make_consistent_random_transformer(4)
        note_sequence = transformer([1, 2, 3, 4])

        self.assertEqual(note_sequence, [1, 3, 2, 4])

    @patch('random.sample', Mock(return_value=[0, 2, 1, 3]))
    def test_random_order_is_consistent_when_applied_several_times(self):
        transformer = make_consistent_random_transformer(4)
        note_sequence_1 = transformer([1, 2, 3, 4])
        note_sequence_2 = transformer([5, 6, 7, 8])

        self.assertEqual(note_sequence_1, [1, 3, 2, 4])
        self.assertEqual(note_sequence_2, [5, 7, 6, 8])

    @patch('random.sample', Mock(return_value=[4, 2, 1, 3]))
    def test_last_note_is_used_if_index_is_out_of_range(self):
        transformer = make_consistent_random_transformer(4)
        note_sequence = transformer([1, 2, 3, 4])

        self.assertEqual(note_sequence, [4, 3, 2, 4])

    @patch('random.sample', Mock(return_value=[0, 2, 1, 3]))
    def test_repeats_last_notes_if_sequence_length_is_long_than_notes(self):
        transformer = make_consistent_random_transformer(4)
        note_sequence = transformer([1, 2, 3, 4], 6)

        self.assertEqual(note_sequence, [1, 3, 2, 4, 2, 4])

    @patch('random.sample', Mock(return_value=[0, 2, 1, 3]))
    def test_shortens_if_sequence_length_is_less_than_notes(self):
        transformer = make_consistent_random_transformer(4)
        note_sequence = transformer([1, 2, 3, 4], 2)

        self.assertEqual(note_sequence, [1, 3])
