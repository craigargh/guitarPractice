from unittest import TestCase

from guitarPractice.exercises.exercise import Exercise
from guitarPractice.exercises.exercise_builder import ExerciseBuilder


class TestExerciseBuilder(TestCase):
    def test_build_returns_an_exercise(self):
        builder = ExerciseBuilder() \
            .build()

        self.assertTrue(isinstance(builder, Exercise))
