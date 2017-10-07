from unittest import TestCase

from guitarPractice.exercises.exercise import Exercise
from guitarPractice.exercises.exercise_builder import ExerciseBuilder


class TestExerciseBuilder(TestCase):
    def test_build_returns_an_exercise(self):
        exercise = ExerciseBuilder() \
            .build()

        self.assertTrue(isinstance(exercise, Exercise))

    def test_set_shapes_sets_shapes_for_exercise(self):
        exercise = ExerciseBuilder() \
            .set_shapes([1, 2, 3, 4]) \
            .build()

        self.assertEqual(exercise.shapes, [1, 2, 3, 4])

    def test_set_shapes_can_only_be_called_once(self):
        with self.assertRaises(AttributeError):
            ExerciseBuilder() \
                .set_shapes([1, 2, 3, 4]) \
                .set_shapes([4, 3, 2, 1])
