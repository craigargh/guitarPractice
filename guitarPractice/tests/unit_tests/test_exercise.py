from collections import namedtuple
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.guitar_shapes.position import Position


def make_sequence(qty):
    SequenceItem = namedtuple('SequenceItem', ['order'])

    return [
        SequenceItem(order=index)
        for index in range(qty)
    ]


class TestExercise(TestCase):
    def test_exercise_shapes_are_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=make_sequence(4))

        self.assertEqual(exercise.shapes, [1, 2, 3, 4])

    def test_exercise_sequence_is_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=make_sequence(4))

        self.assertEqual(exercise.sequence, make_sequence(4))

    def test_rhythm_can_be_set(self):
        exercise = Exercise(
            shapes=[1, 2, 3, 4],
            sequence=['a', 'b', 'c', 'd'],
            rhythm=[
                {'duration': 1, 'division': 4},
                {'duration': 1, 'division': 4},
                {'duration': 1, 'division': 4},
                {'duration': 1, 'division': 4},
            ]
        )

        expected_rhythm = [
            {'duration': 1, 'division': 4},
            {'duration': 1, 'division': 4},
            {'duration': 1, 'division': 4},
            {'duration': 1, 'division': 4},
        ]

        self.assertEqual(expected_rhythm, exercise.rhythm)

    def test_rhythm_defaults_to_eighth_notes(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=make_sequence(4))

        expected_rhythm = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
        ]

        self.assertEqual(expected_rhythm, exercise.rhythm)

    def test_rhythm_default_ends_on_full_note_for_odd_number_of_beats(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=make_sequence(5))

        expected_rhythm = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 4},
        ]

        self.assertEqual(expected_rhythm, exercise.rhythm)


class TestExerciseAsDict(TestCase):
    def setUp(self):
        self.shapes = []
        self.default_sequence = [
            Position(guitar_string=1, fret=0, finger=0, is_highlighted=False, order=0),
            Position(guitar_string=2, fret=2, finger=1, is_highlighted=True, order=1),
        ]

    def test_exercise_as_dict_has_sequence(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertIn('sequence', result)

    def test_exercise_as_dict_has_shapes(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertIn('shapes', result)

    def test_each_sequence_item_has_an_order(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertEqual(result['sequence'][0]['order'], 0)
        self.assertEqual(result['sequence'][1]['order'], 1)

    def test_each_sequence_item_has_a_list_of_positions(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertEqual(1, len(result['sequence'][0]['positions']))
        self.assertEqual(1, len(result['sequence'][1]['positions']))

    def test_order_items_are_not_duplicated(self):
        sequence = [
            Position(guitar_string=1, fret=0, finger=0, is_highlighted=False, order=0),
            Position(guitar_string=2, fret=2, finger=1, is_highlighted=True, order=0),
        ]

        exercise = Exercise(shapes=self.shapes, sequence=sequence)
        result = exercise.as_dict()

        self.assertEqual(1, len(result['sequence']))
        self.assertEqual(2, len(result['sequence'][0]['positions']))

    def test_positions_have_correct_attributes(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()
        positions = result['sequence'][0]['positions']

        expected = {
            'fret': 0,
            'guitar_string': 1,
            'finger': 0,
            'is_highlighted': False,
        }

        self.assertEqual(expected, positions[0])

    def test_sequence_has_rhythm(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertIn('rhythm', result['sequence'][0])

    def test_sequence_sets_rhythm(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        expected = {
            'duration': 1,
            'division': 8,
        }

        self.assertEqual(expected, result['sequence'][0]['rhythm'])

    def test_shapes_are_set(self):
        exercise = Exercise(shapes=self.shapes, sequence=self.default_sequence)
        result = exercise.as_dict()

        self.assertEqual(self.shapes, result['shapes'])
