from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercises.pentatonic_scale import level_one


class TestPentatonicScaleExercise(TestCase):
    def test_level_one_returns_an_exercise(self):
        exercise = level_one()

        self.assertTrue(type(exercise) is Exercise)

    def test_exercise_contains_at_least_one_shape(self):
        exercise = level_one()

        self.assertGreaterEqual(len(exercise.shapes), 1)

    def test_exercise_contains_no_more_than_two_shapes(self):
        exercise = level_one()

        self.assertLessEqual(len(exercise.shapes), 2)

    def test_exercise_contains_at_least_11_positions(self):
        exercise = level_one()

        self.assertGreaterEqual(len(exercise.sequence), 11)

    def test_exercise_contains_no_more_than_12_positions(self):
        exercise = level_one()

        self.assertLessEqual(len(exercise.sequence), 12)
