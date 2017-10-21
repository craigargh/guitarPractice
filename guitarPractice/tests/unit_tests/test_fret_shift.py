from unittest import TestCase

from guitarPractice.exercise_builder.transformers.fret_shift import move_frets
from guitarPractice.guitar_shapes.position import Position


class TestMoveFrets(TestCase):
    def test_move_frets_moves_fret(self):
        positions = [
            Position(guitar_string=1, fret=5)
        ]

        moved_positions = move_frets(positions, 1)

        self.assertEqual(1, moved_positions[0].fret)

    def test_move_frets_shifts_frets_of_multiple_positions(self):
        positions = [
            Position(guitar_string=1, fret=5),
            Position(guitar_string=1, fret=6),
            Position(guitar_string=1, fret=7),
            Position(guitar_string=1, fret=8),
        ]

        moved_positions = move_frets(positions, 3)

        self.assertEqual(3, moved_positions[0].fret)
        self.assertEqual(4, moved_positions[1].fret)
        self.assertEqual(5, moved_positions[2].fret)
        self.assertEqual(6, moved_positions[3].fret)

    def test_move_frets_shifts_frets_of_out_of_order_multiple_positions(self):
        positions = [
            Position(guitar_string=1, fret=6),
            Position(guitar_string=1, fret=7),
            Position(guitar_string=1, fret=5),
            Position(guitar_string=1, fret=8),
        ]

        moved_positions = move_frets(positions, 1)

        self.assertEqual(2, moved_positions[0].fret)
        self.assertEqual(3, moved_positions[1].fret)
        self.assertEqual(1, moved_positions[2].fret)
        self.assertEqual(4, moved_positions[3].fret)

    def test_move_frets_shifts_frets_up(self):
        positions = [
            Position(guitar_string=1, fret=6),
            Position(guitar_string=1, fret=7),
            Position(guitar_string=1, fret=5),
            Position(guitar_string=1, fret=8),
        ]

        moved_positions = move_frets(positions, 10)

        self.assertEqual(11, moved_positions[0].fret)
        self.assertEqual(12, moved_positions[1].fret)
        self.assertEqual(10, moved_positions[2].fret)
        self.assertEqual(13, moved_positions[3].fret)
