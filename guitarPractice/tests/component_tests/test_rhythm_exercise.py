from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercises.rhythm import level_one


class TestRhythmExercise(TestCase):
    def test_level_one_returns_an_exercise(self):
        exercise = level_one()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_one_returns_one_shape(self):
        exercise = level_one()

        self.assertEqual(len(exercise.shapes), 1)

    def test_level_one_returns_at_least_eight_positions(self):
        exercise = level_one()

        self.assertGreaterEqual(len(exercise.sequence), 8)

    def test_level_one_returns_at_no_more_than_sixteen_positions(self):
        exercise = level_one()

        self.assertLessEqual(len(exercise.sequence), 16)
