from unittest import TestCase

from guitarPractice.exercise_builder.transformers import pick_pattern
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

        positions_without_string_5 = [
            Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
            Position(guitar_string=4),
            Position(guitar_string=3, is_highlighted=True),
            Position(guitar_string=2),
            Position(guitar_string=1, fret=3, finger=3, is_highlighted=True),
        ]

        self.shortened_shape = GuitarShape('G', 'Major', positions_without_string_5)

        single_note = [
            Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        ]

        self.single_note_shape = GuitarShape('G', 'Major', single_note)

    def test_can_get_note_on_string_one(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 1)

        self.assertEqual(note.guitar_string, 1)

    def test_can_get_note_on_string_two(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 2)

        self.assertEqual(note.guitar_string, 2)

    def test_can_get_note_on_string_three(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 3)

        self.assertEqual(note.guitar_string, 3)

    def test_can_get_note_on_string_four(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 4)

        self.assertEqual(note.guitar_string, 4)

    def test_can_get_note_on_string_five(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 5)

        self.assertEqual(note.guitar_string, 5)

    def test_can_get_note_on_string_six(self):
        note = pick_pattern.get_guitar_string_note(self.six_string_shape, 6)

        self.assertEqual(note.guitar_string, 6)

    def test_throws_an_exception_for_an_invalid_string(self):
        with self.assertRaises(ValueError):
            pick_pattern.get_guitar_string_note(self.six_string_shape, 7)

    def test_get_root_note_returns_lowest_note(self):
        note = pick_pattern.get_root_note(self.six_string_shape)

        self.assertEqual(note.guitar_string, 6)

    def test_get_alternate_root_note_returns_second_lowest_string(self):
        note = pick_pattern.get_alternate_root_note(self.six_string_shape)

        self.assertEqual(note.guitar_string, 5)

    def test_get_alternate_root_note_adjusts_for_string_that_is_not_played(self):
        note = pick_pattern.get_alternate_root_note(self.shortened_shape)

        self.assertEqual(note.guitar_string, 4)

    def test_get_alternate_root_note_raises_error_if_not_found(self):
        with self.assertRaises(ValueError):
            pick_pattern.get_alternate_root_note(self.single_note_shape)

    def test_pick_pattern_works_with_string_numbers(self):
        pattern = [6, 3, 4, 2]

        notes = pick_pattern.get_notes_from_pick_pattern(self.six_string_shape, pattern)

        self.assertEqual(notes[0].guitar_string, 6)
        self.assertEqual(notes[1].guitar_string, 3)
        self.assertEqual(notes[2].guitar_string, 4)
        self.assertEqual(notes[3].guitar_string, 2)

    def test_pick_pattern_works_with_root_note_symbol(self):
        pattern = ['r', 1, 'r', 2]

        notes = pick_pattern.get_notes_from_pick_pattern(self.six_string_shape, pattern)

        self.assertEqual(notes[0].guitar_string, 6)
        self.assertEqual(notes[1].guitar_string, 1)
        self.assertEqual(notes[2].guitar_string, 6)
        self.assertEqual(notes[3].guitar_string, 2)

    def test_pick_pattern_works_with_alternate_root_note_symbol(self):
        pattern = ['a', 3, 'a', 4]

        notes = pick_pattern.get_notes_from_pick_pattern(self.six_string_shape, pattern)

        self.assertEqual(notes[0].guitar_string, 5)
        self.assertEqual(notes[1].guitar_string, 3)
        self.assertEqual(notes[2].guitar_string, 5)
        self.assertEqual(notes[3].guitar_string, 4)
