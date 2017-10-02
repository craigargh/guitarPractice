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
