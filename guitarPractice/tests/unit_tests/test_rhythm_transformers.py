from random import Random
from unittest import TestCase
from unittest.mock import patch

from guitarPractice.exercise_builder.transformers.rhythm import set_rhythm, Beat, random_rhythm_factory
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

        self.assertEqual(updated_sequence[0].note_subdivision, 6)
        self.assertEqual(updated_sequence[1].note_subdivision, 6)
        self.assertEqual(updated_sequence[2].note_subdivision, 6)


class TestRandomRhythmFactory(TestCase):
    def test_random_rhythm_factory_sets_length_of_a_rhythm(self):
        beat_sequences = [
            [
                Beat(2, 2)
            ],
        ]

        rhythm = random_rhythm_factory(2, beat_sequences)

        self.assertEqual(2, len(rhythm))

    @patch('guitarPractice.exercise_builder.transformers.rhythm.random')
    def test_random_rhythm_factory_chooses_random_beats(self, random_mock):
        random_mock.choice.side_effect = Random(1).choice

        beat_sequences = [
            [
                Beat(1, 1)
            ],
            [
                Beat(2, 2),
                Beat(3, 3)
            ]
        ]

        rhythm = random_rhythm_factory(4, beat_sequences)

        self.assertEqual(rhythm[0].note_subdivision, 1)
        self.assertEqual(rhythm[1].note_subdivision, 1)
        self.assertEqual(rhythm[2].note_subdivision, 2)
        self.assertEqual(rhythm[3].note_subdivision, 3)
        self.assertEqual(rhythm[4].note_subdivision, 1)

    @patch('guitarPractice.exercise_builder.transformers.rhythm.random')
    def test_random_rhythm_factory_returns_a_length(self, random_mock):
        random_mock.choice.side_effect = Random(1).choice

        beat_sequences = [
            [
                Beat(1, 1)
            ],
            [
                Beat(2, 2),
                Beat(3, 3)
            ]
        ]

        rhythm = random_rhythm_factory(4, beat_sequences)

        self.assertEqual(5, len(rhythm))
