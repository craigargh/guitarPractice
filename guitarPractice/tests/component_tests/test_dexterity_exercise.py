from unittest import TestCase

from guitarPractice.exercises.dexterity import level_one


class TestDexterity(TestCase):
    def test_dexterity_exercise_has_one_shape(self):
        exercise = level_one()

        self.assertEqual(1, len(exercise.shapes))

    def test_dexterity_exercise_has_four_sequence_positions(self):
        exercise = level_one()

        self.assertGreaterEqual(6, len(exercise.sequence))
        self.assertLessEqual(4, len(exercise.sequence))
