from functools import partial
from unittest import TestCase
from guitarPractice.exercise_builder import sequencers


class TestSequencers(TestCase):
    def setUp(self):
        self.shape1 = ['a', 'b']
        self.shape2 = ['c', 'd']
        self.shape3 = ['e', 'f']

    def test_in_order_sequencer_combines_shape_notes_in_order(self):
        note_sequence = sequencers.in_order_sequencer([self.shape1, self.shape2, self.shape3])

        self.assertEqual(note_sequence, [['a', 'b'], ['c', 'd'], ['e', 'f']])

    def test_repeat_first_shape_sequencer_alternates_with_first_shape(self):
        note_sequence = sequencers.repeat_first_shape_sequencer([self.shape1, self.shape2, self.shape3])

        self.assertEqual(note_sequence, [['a', 'b'], ['c', 'd'], ['a', 'b'], ['e', 'f']])

    def test_repeat_shapes_repeats_each_shape_a_number_of_times(self):
        repeater = partial(sequencers.repeat_shapes, times=2)

        note_sequnce = repeater([self.shape1, self.shape2, self.shape3])

        self.assertEqual(note_sequnce, [['a', 'b'], ['a', 'b'], ['c', 'd'], ['c', 'd'], ['e', 'f'], ['e', 'f']])
