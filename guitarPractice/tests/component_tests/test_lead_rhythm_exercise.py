from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercises.lead_rhythm import level_one, level_two


class TestLeadRhythm(TestCase):
    def test_level_one_returns_an_exercise(self):
        exercise = level_one()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_one_contains_one_shape(self):
        exercise = level_one()

        self.assertEqual(len(exercise.shapes), 1)

    def test_level_one_contains_11_positions(self):
        exercise = level_one()

        self.assertEqual(len(exercise.sequence), 11)

    def test_level_two_returns_an_exercise(self):
        exercise = level_two()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_two_contains_one_shape(self):
        exercise = level_two()

        self.assertEqual(len(exercise.shapes), 1)

    def test_level_two_contains_at_least_11_positions(self):
        exercise = level_two()

        self.assertGreaterEqual(len(exercise.sequence), 11)

    def test_level_two_contains_no_more_than_15_positions(self):
        exercise = level_two()

        self.assertLessEqual(len(exercise.sequence), 15)
