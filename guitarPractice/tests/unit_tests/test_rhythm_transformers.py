from unittest import TestCase

from guitarPractice.exercise_builder.transformers.rhythm import set_rhythm, Beat
from guitarPractice.guitar_shapes.position import Position


class TestRhythmTransformers(TestCase):
    def test_set_rhythm_sets_the_duration_of_a_note(self):
        sequence = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
        ]

        rhythm = [
            Beat(duration=3, note_subdivision=6),
            Beat(duration=2, note_subdivision=5),
            Beat(duration=1, note_subdivision=4),
        ]

        updated_sequence = set_rhythm(sequence, rhythm)

        self.assertEqual(updated_sequence[0].duration, 3)
        self.assertEqual(updated_sequence[1].duration, 2)
        self.assertEqual(updated_sequence[2].duration, 1)

    def test_set_rhythm_sets_the_subdivision_of_a_note(self):
        sequence = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
        ]

        rhythm = [
            Beat(duration=3, note_subdivision=6),
            Beat(duration=2, note_subdivision=5),
            Beat(duration=1, note_subdivision=4),
        ]

        updated_sequence = set_rhythm(sequence, rhythm)

        self.assertEqual(updated_sequence[0].note_subdivision, 6)
        self.assertEqual(updated_sequence[1].note_subdivision, 5)
        self.assertEqual(updated_sequence[2].note_subdivision, 4)

    def test_set_rhythm_repeats_beats_to_length_of_sequence(self):
        sequence = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
        ]

        rhythm = [
            Beat(duration=3, note_subdivision=6),
        ]

        updated_sequence = set_rhythm(sequence, rhythm)

        self.assertEqual(updated_sequence[0].duration, 3)
        self.assertEqual(updated_sequence[1].duration, 3)
        self.assertEqual(updated_sequence[2].duration, 3)

    def test_set_rhythm_repeats_beats_to_length_of_sequence(self):
        sequence = [
            Position(guitar_string=1),
            Position(guitar_string=2),
            Position(guitar_string=3),
        ]

        rhythm = [
            Beat(duration=3, note_subdivision=6),
        ]

        updated_sequence = set_rhythm(sequence, rhythm)

        self.assertEqual(updated_sequence[0].note_subdivision, 6)
        self.assertEqual(updated_sequence[1].note_subdivision, 6)
        self.assertEqual(updated_sequence[2].note_subdivision, 6)
