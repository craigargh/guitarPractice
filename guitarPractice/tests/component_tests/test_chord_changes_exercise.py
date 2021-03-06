from collections import Counter
from unittest import TestCase

from guitarPractice.exercise_builder.exercise import Exercise
from guitarPractice.exercises.chord_changes import level_one, level_two


class TestChordChanges(TestCase):
    def test_level_one_returns_an_exercise(self):
        exercise = level_one()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_one_exercise_contains_two_chords(self):
        exercise = level_one()

        self.assertEqual(len(exercise.shapes), 2)
        self.assertTrue(exercise.shapes[0].is_chord)
        self.assertTrue(exercise.shapes[1].is_chord)

    def test_level_one_has_eight_beats(self):
        exercise = level_one()

        beats = set(position.order for position in exercise.sequence)

        self.assertEqual(len(beats), 8)

    def test_level_one_sequence_has_no_single_picked_notes(self):
        exercise = level_one()

        order_counter = Counter(
            item.order
            for item in exercise.sequence
        )

        are_all_order_values_unique = all(
            count > 1
            for _, count in order_counter.items()
        )

        self.assertTrue(are_all_order_values_unique)

    def test_level_two_returns_an_exercise(self):
        exercise = level_two()

        self.assertTrue(type(exercise) is Exercise)

    def test_level_two_exercise_contains_at_least_three_chords(self):
        exercise = level_two()

        self.assertGreaterEqual(len(exercise.shapes), 3)

    def test_level_two_exercise_contains_no_more_than_four_chords(self):
        exercise = level_two()

        self.assertLessEqual(len(exercise.shapes), 4)

    def test_level_two_exercise_has_sixteen_beats(self):
        exercise = level_two()

        beats = set(position.order for position in exercise.sequence)

        self.assertEqual(len(beats), 16)
