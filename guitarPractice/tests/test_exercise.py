from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise


class TestExercise(TestCase):
    def test_exercise_shapes_are_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=['a', 'b', 'c', 'd'])

        self.assertEqual(exercise.shapes, [1, 2, 3, 4])

    def test_exercise_sequence_is_set(self):
        exercise = Exercise(shapes=[1, 2, 3, 4], sequence=['a', 'b', 'c', 'd'])

        self.assertEqual(exercise.sequence, ['a', 'b', 'c', 'd'])
