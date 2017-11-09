from unittest import TestCase

from guitarPractice.exercise_builder.transformers import pick_pattern
from guitarPractice.guitar_shapes.chord_shapes import g_major
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


class TestPickPattern(TestCase):
    def setUp(self):
        positions = [
            Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
            Position(guitar_string=5, fret=2, finger=1),
            Position(guitar_string=4),
            Position(guitar_string=3, is_highlighted=True),
            Position(guitar_string=2),
            Position(guitar_string=1, fret=3, finger=3, is_highlighted=True),
        ]

        self.six_string_shape = GuitarShape('G', 'Major', positions)

    def test_can_get_note_on_string_one(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 1)

        self.assertEqual(note.guitar_string, 1)

    def test_can_get_note_on_string_two(self):
        shape = g_major()

        note = pick_pattern.get_guitar_string_note(shape, 2)

        self.assertEqual(note.guitar_string, 2)

    def test_can_get_note_on_string_three(self):
        shape = g_major()

        note = pick_pattern.get_guitar_string_note(shape, 3)

        self.assertEqual(note.guitar_string, 3)

    def test_can_get_note_on_string_four(self):
        shape = g_major()

        note = pick_pattern.get_guitar_string_note(shape, 4)

        self.assertEqual(note.guitar_string, 4)

    def test_can_get_note_on_string_five(self):
        shape = g_major()

        note = pick_pattern.get_guitar_string_note(shape, 5)

        self.assertEqual(note.guitar_string, 5)

    def test_can_get_note_on_string_six(self):
        shape = g_major()

        note = pick_pattern.get_guitar_string_note(shape, 6)

        self.assertEqual(note.guitar_string, 6)

    def test_throws_an_exception_for_an_invalid_string(self):
        shape = g_major()

        with self.assertRaises(ValueError):
            pick_pattern.get_guitar_string_note(shape, 7)
