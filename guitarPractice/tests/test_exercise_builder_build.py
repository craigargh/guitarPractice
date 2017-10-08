import operator
from functools import partial
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape


class TestExerciseBuilderBuild(TestCase):
    def setUp(self):
        self.shapes = [
            GuitarShape(positions=[1, 2, 3, 4], root_note='A', tonality='m'),
            GuitarShape(positions=[5, 6, 7, 8], root_note='B', tonality='m'),
            GuitarShape(positions=[9, 10, 11, 12], root_note='C', tonality='m'),
        ]

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

    def test_shapes_are_required_before_build(self):
        with self.assertRaises(AttributeError):
            ExerciseBuilder() \
                .build()

    def test_build_combines_shapes_and_sets_sequence(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .build()

        expected_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_transform_is_applied_to_each_shape(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .transform(reversed) \
            .build()

        expected_sequence = [4, 3, 2, 1, 8, 7, 6, 5, 12, 11, 10, 9]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_multiple_transforms_can_be_applied_to_each_shape(self):
        add_one = partial(operator.add, 1)
        add_one_to_each = partial(map, add_one)

        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .transform(reversed) \
            .transform(add_one_to_each) \
            .build()

        expected_sequence = [5, 4, 3, 2, 9, 8, 7, 6, 13, 12, 11, 10]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_sequencer_is_applied_to_shape_sequence(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .set_sequencer(reversed) \
            .build()

        expected_sequence = [9, 10, 11, 12, 5, 6, 7, 8, 1, 2, 3, 4]

        self.assertEqual(exercise.sequence, expected_sequence)
