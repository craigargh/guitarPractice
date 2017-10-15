from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.guitar_shapes.position import Position


class TestExercise(TestCase):
    def test_exercise_shapes_are_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=['a', 'b', 'c', 'd'])

        self.assertEqual(exercise.shapes, [1, 2, 3, 4])

    def test_exercise_sequence_is_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=['a', 'b', 'c', 'd'])

        self.assertEqual(exercise.sequence, ['a', 'b', 'c', 'd'])

    def test_str_returns_sequence_as_tabs(self):
        sequence = [
            Position(guitar_string=1, order=1),
            Position(guitar_string=2, order=0),
            Position(guitar_string=3, order=2),
        ]

        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=sequence)

        expected_tab = \
            "--0---\n" \
            "0-----\n" \
            "----0-\n" \
            "------\n" \
            "------\n" \
            "------"

        self.assertEqual(expected_tab, str(exercise))

    def test_str_returns_chord_sequence_as_tabs(self):
        sequence = [
            Position(guitar_string=1, order=1),
            Position(guitar_string=2, order=0),
            Position(guitar_string=3, order=1),
        ]

        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=sequence)

        expected_tab = \
            "--0-\n" \
            "0---\n" \
            "--0-\n" \
            "----\n" \
            "----\n" \
            "----"

        self.assertEqual(expected_tab, str(exercise))