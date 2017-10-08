from functools import partial
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


class TestExerciseBuilderBuild(TestCase):
    def setUp(self):
        a_positions = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
            Position(guitar_string=4),
        ]
        b_positions = [
            Position(guitar_string=5),
            Position(guitar_string=6),
            Position(guitar_string=7),
            Position(guitar_string=8),
        ]

        self.shapes = [
            GuitarShape(positions=a_positions, root_note='A', tonality='m'),
            GuitarShape(positions=b_positions, root_note='B', tonality='m'),
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

        expected_sequence = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
            Position(guitar_string=4),
            Position(guitar_string=5),
            Position(guitar_string=6),
            Position(guitar_string=7),
            Position(guitar_string=8),
        ]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_transform_is_applied_to_each_shape(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .transform(reversed) \
            .build()

        expected_sequence = [
            Position(guitar_string=4),
            Position(guitar_string=3),
            Position(guitar_string=2),
            Position(guitar_string=1),
            Position(guitar_string=8),
            Position(guitar_string=7),
            Position(guitar_string=6),
            Position(guitar_string=5)
        ]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_multiple_transforms_can_be_applied_to_each_shape(self):
        def increase_guitar_string(position):
            position.guitar_string += 1
            return position

        add_one_to_each = partial(map, increase_guitar_string)

        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .transform(reversed) \
            .transform(add_one_to_each) \
            .build()

        expected_sequence = [
            Position(guitar_string=5),
            Position(guitar_string=4),
            Position(guitar_string=3),
            Position(guitar_string=2),
            Position(guitar_string=9),
            Position(guitar_string=8),
            Position(guitar_string=7),
            Position(guitar_string=6)
        ]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_sequencer_is_applied_to_shape_sequence(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .set_sequencer(reversed) \
            .build()

        expected_sequence = [
            Position(guitar_string=5),
            Position(guitar_string=6),
            Position(guitar_string=7),
            Position(guitar_string=8),
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
            Position(guitar_string=4),
        ]

        self.assertEqual(exercise.sequence, expected_sequence)

    def test_combiner_sets_order_of_positions(self):
        exercise = ExerciseBuilder() \
            .set_shapes(self.shapes) \
            .build()

        self.assertEqual(exercise.sequence[0].order, 0)
        self.assertEqual(exercise.sequence[1].order, 1)
        self.assertEqual(exercise.sequence[2].order, 2)
        self.assertEqual(exercise.sequence[3].order, 3)
        self.assertEqual(exercise.sequence[4].order, 4)
        self.assertEqual(exercise.sequence[5].order, 5)
        self.assertEqual(exercise.sequence[6].order, 6)
        self.assertEqual(exercise.sequence[7].order, 7)
