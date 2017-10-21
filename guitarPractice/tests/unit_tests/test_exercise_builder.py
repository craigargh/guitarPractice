from unittest import TestCase

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape


class TestExerciseBuilder(TestCase):
    def setUp(self):
        self.shapes = [
            GuitarShape(positions=[1, 2, 3, 4], root_note='A', tonality='m'),
            GuitarShape(positions=[5, 6, 7, 8], root_note='B', tonality='m'),
            GuitarShape(positions=[9, 10, 11, 12], root_note='C', tonality='m'),
        ]

    def test_set_shapes_sets_builder_shapes(self):
        builder = ExerciseBuilder() \
            .set_shapes(self.shapes)

        self.assertEqual(builder.shapes, self.shapes)

    def test_set_shapes_can_only_be_called_once(self):
        with self.assertRaises(AttributeError):
            ExerciseBuilder() \
                .set_shapes(self.shapes) \
                .set_shapes(self.shapes)

    def test_transform_adds_transformer_to_exercise(self):
        builder = ExerciseBuilder() \
            .transform("transformer double")

        self.assertEqual(builder.transformers, ["transformer double"])

    def test_can_add_multiple_transformers_to_exercise(self):
        builder = ExerciseBuilder() \
            .transform("a") \
            .transform("b") \
            .transform("c") \
            .transform("d")

        self.assertEqual(builder.transformers, ["a", "b", "c", "d"])

    def test_set_rhythm_for_builder(self):
        builder = ExerciseBuilder() \
            .set_rhythm("rhythm")

        self.assertEqual(builder.rhythm, "rhythm")

    def test_can_only_set_rhythm_once(self):
        with self.assertRaises(AttributeError):
            ExerciseBuilder() \
                .set_rhythm("rhythm") \
                .set_rhythm("another")

    def test_can_set_sequencer(self):
        builder = ExerciseBuilder() \
            .set_sequencer("sequencer")

        self.assertEqual(builder.sequencer, "sequencer")

    def test_can_only_set_sequencer_once(self):
        with self.assertRaises(AttributeError):
            ExerciseBuilder() \
                .set_sequencer("sequencer") \
                .set_sequencer("again")

    def test_can_set_display_modified_shapes(self):
        builder = ExerciseBuilder() \
            .display_modified_shapes(True)

        self.assertEqual(True, builder._display_modified_shapes)

    def test_can_set_display_modified_shapes_defaults_to_false(self):
        builder = ExerciseBuilder()

        self.assertEqual(False, builder._display_modified_shapes)
