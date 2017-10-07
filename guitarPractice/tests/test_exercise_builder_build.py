from unittest import TestCase

from guitarPractice.exercises.exercise import Exercise
from guitarPractice.exercises.exercise_builder import ExerciseBuilder
from guitarPractice.exercises.guitar_shape import GuitarShape


class TestExerciseBuilderBuild(TestCase):
    def setUp(self):
        self.shapes = [
            GuitarShape(positions=[1, 2, 3, 4], root_note='A', voicing='m'),
            GuitarShape(positions=[5, 6, 7, 8], root_note='B', voicing='m'),
            GuitarShape(positions=[9, 10, 11, 12], root_note='C', voicing='m'),
        ]

    def test_build_combines_shapes_and_sets_sequence(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .build()

        expected_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_build_returns_an_exercise(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .build()

        self.assertTrue(isinstance(exercise, Exercise))

    def test_build_sets_shapes_for_exercise(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .build()

        self.assertEqual(exercise.shapes, self.shapes)
