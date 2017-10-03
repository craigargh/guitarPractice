from unittest import TestCase
from guitarPractice.exercises import sequencers


class TestSequencers(TestCase):
    def setUp(self):
        self.shape1 = ['a', 'b']
        self.shape2 = ['c', 'd']
        self.shape3 = ['e', 'f']

    def test_in_order_sequencer_combines_shape_notes_in_order(self):
        note_sequence = sequencers.in_order_sequencer(self.shape1, self.shape2, self.shape3)

        self.assertEqual(note_sequence, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_repeat_first_shape_sequencer_alternates_with_first_shape(self):
        note_sequence = sequencers.repeat_first_shape_sequencer(self.shape1, self.shape2, self.shape3)

        self.assertEqual(note_sequence, ['a', 'b', 'c', 'd', 'a', 'b', 'e', 'f'])
