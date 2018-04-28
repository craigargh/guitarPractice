from collections import namedtuple
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise


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
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=make_sequence(5))

        expected_rhythm = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
        ]

        self.assertEqual(expected_rhythm, exercise.rhythm)


def make_sequence(qty):
    SequenceItem = namedtuple('SequenceItem', ['order'])

    return [
        SequenceItem(order=index)
        for index in range(qty)
    ]
