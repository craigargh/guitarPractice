from unittest import TestCase

from guitarPractice.exercises.chord import Chord


class ChordTest(TestCase):
    def test_root_note_is_set(self):
        c_major = Chord('C', 'major', [])

        self.assertEqual('C', c_major.root_note)

    def test_voicing_is_set(self):
        c_major = Chord('C', 'major', [])

        self.assertEqual('major', c_major.voicing)

    def test_name_is_built_from_root_note_and_voicing(self):
        c_major = Chord('C', 'major', [])

        self.assertEqual('C major', c_major.name)

    def test_chord_length_is_set_from_number_of_positions(self):
        c_major = Chord('C', 'major', [1, 2, 3])

        self.assertEqual(3, len(c_major))

    def test_can_access_chord_positions(self):
        c_major = Chord('C', 'major', [1, 2, 3])

        self.assertEqual(1, c_major[0])
        self.assertEqual(2, c_major[1])
        self.assertEqual(3, c_major[2])

    def test_iterating_over_chord_returns_positions_in_order(self):
        c_major = Chord('C', 'major', [1, 2, 3])

        results = []

        for value in c_major:
            results.append(value)

        self.assertEqual(1, results[0])
        self.assertEqual(2, results[1])
        self.assertEqual(3, results[2])
