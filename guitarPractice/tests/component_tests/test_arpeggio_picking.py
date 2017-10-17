from collections import Counter
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercises.arpeggio_picking import level_one, level_two


class TestRhythmArpeggios(TestCase):
    def test_level_one_returns_an_exercise(self):
        exercise = level_one()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_one_exercise_contains_two_chords(self):
        exercise = level_one()

        self.assertEqual(len(exercise.shapes), 2)
        self.assertTrue(exercise.shapes[0].is_chord)
        self.assertTrue(exercise.shapes[1].is_chord)

    def test_level_one_sequence_contains_between_eight_and_sixteen_positions(self):
        exercise = level_one()

        self.assertGreaterEqual(len(exercise.sequence), 8)
        self.assertLessEqual(len(exercise.sequence), 16)

    def test_level_one_sequence_has_no_two_positions_with_the_same_order(self):
        exercise = level_one()

        order_counter = Counter(
            item.order
            for item in exercise.sequence
        )

        are_all_order_values_unique = all(
            count == 1
            for _, count in order_counter.items()
        )

        self.assertTrue(are_all_order_values_unique)

    def test_level_two_returns_an_exercise(self):
        exercise = level_two()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_two_exercise_contains_between_two_and_four_chords(self):
        exercise = level_two()

        are_all_shapes_chords = all(
            shape.is_chord
            for shape in exercise.shapes
        )

        self.assertGreaterEqual(len(exercise.shapes), 2)
        self.assertLessEqual(len(exercise.shapes), 4)
        self.assertTrue(are_all_shapes_chords)

    def test_level_two_sequence_contains_between_eight_and_thirty_two_positions(self):
        exercise = level_two()

        self.assertGreaterEqual(len(exercise.sequence), 8)
        self.assertLessEqual(len(exercise.sequence), 32)

    def test_level_two_sequence_has_no_two_positions_with_the_same_order(self):
        exercise = level_two()

        order_counter = Counter(
            item.order
            for item in exercise.sequence
        )

        are_all_order_values_unique = all(
            count == 1
            for _, count in order_counter.items()
        )

        self.assertTrue(are_all_order_values_unique)
