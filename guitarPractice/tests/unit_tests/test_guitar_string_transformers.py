from unittest import TestCase

from guitarPractice.exercise_builder.transformers.guitar_string import alternate_odd, alternate_even, spread_left, \
    spread_right
from guitarPractice.guitar_shapes.position import Position


class TestAlternateOdd(TestCase):
    def test_every_other_position_has_its_string_changed(self):
        positions = [
            Position(guitar_string=1, fret=1),
            Position(guitar_string=1, fret=2),
            Position(guitar_string=1, fret=3),
            Position(guitar_string=1, fret=4),
        ]

        changed_positions = alternate_odd(positions)

        self.assertEqual(1, changed_positions[0].guitar_string)
        self.assertEqual(2, changed_positions[1].guitar_string)
        self.assertEqual(1, changed_positions[2].guitar_string)
        self.assertEqual(2, changed_positions[3].guitar_string)

    def test_max_string_will_not_be_exceeded(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = alternate_odd(positions)

        self.assertEqual(5, changed_positions[0].guitar_string)
        self.assertEqual(6, changed_positions[1].guitar_string)
        self.assertEqual(5, changed_positions[2].guitar_string)
        self.assertEqual(6, changed_positions[3].guitar_string)

    def test_can_set_max_fret(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = alternate_odd(positions, 8)

        self.assertEqual(6, changed_positions[0].guitar_string)
        self.assertEqual(7, changed_positions[1].guitar_string)
        self.assertEqual(6, changed_positions[2].guitar_string)
        self.assertEqual(7, changed_positions[3].guitar_string)


class TestAlternateEven(TestCase):
    def test_every_other_position_has_its_string_changed(self):
        positions = [
            Position(guitar_string=1, fret=1),
            Position(guitar_string=1, fret=2),
            Position(guitar_string=1, fret=3),
            Position(guitar_string=1, fret=4),
        ]

        changed_positions = alternate_even(positions)

        self.assertEqual(2, changed_positions[0].guitar_string)
        self.assertEqual(1, changed_positions[1].guitar_string)
        self.assertEqual(2, changed_positions[2].guitar_string)
        self.assertEqual(1, changed_positions[3].guitar_string)

    def test_max_string_will_not_be_exceeded(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = alternate_even(positions)

        self.assertEqual(6, changed_positions[0].guitar_string)
        self.assertEqual(5, changed_positions[1].guitar_string)
        self.assertEqual(6, changed_positions[2].guitar_string)
        self.assertEqual(5, changed_positions[3].guitar_string)

    def test_can_set_max_fret(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = alternate_even(positions, 8)

        self.assertEqual(7, changed_positions[0].guitar_string)
        self.assertEqual(6, changed_positions[1].guitar_string)
        self.assertEqual(7, changed_positions[2].guitar_string)
        self.assertEqual(6, changed_positions[3].guitar_string)


class TestSpreadLeft(TestCase):
    def test_spread_left_moves_strings(self):
        positions = [
            Position(guitar_string=1, fret=1),
            Position(guitar_string=1, fret=2),
            Position(guitar_string=1, fret=3),
            Position(guitar_string=1, fret=4),
        ]

        changed_positions = spread_left(positions)

        self.assertEqual(1, changed_positions[0].guitar_string)
        self.assertEqual(2, changed_positions[1].guitar_string)
        self.assertEqual(3, changed_positions[2].guitar_string)
        self.assertEqual(4, changed_positions[3].guitar_string)

    def test_spread_left_cannot_exceed_max_string(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = spread_left(positions)

        self.assertEqual(6, changed_positions[0].guitar_string)
        self.assertEqual(5, changed_positions[1].guitar_string)
        self.assertEqual(4, changed_positions[2].guitar_string)
        self.assertEqual(3, changed_positions[3].guitar_string)

    def test_spread_left_cannot_exceed_min_string(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
            Position(guitar_string=6, fret=5),
            Position(guitar_string=6, fret=6),
            Position(guitar_string=6, fret=7),
        ]

        changed_positions = spread_left(positions)

        self.assertEqual(6, changed_positions[0].guitar_string)
        self.assertEqual(5, changed_positions[1].guitar_string)
        self.assertEqual(4, changed_positions[2].guitar_string)
        self.assertEqual(3, changed_positions[3].guitar_string)
        self.assertEqual(2, changed_positions[4].guitar_string)
        self.assertEqual(1, changed_positions[5].guitar_string)
        self.assertEqual(2, changed_positions[6].guitar_string)


class TestSpreadRight(TestCase):
    def test_spread_right_moves_strings(self):
        positions = [
            Position(guitar_string=6, fret=1),
            Position(guitar_string=6, fret=2),
            Position(guitar_string=6, fret=3),
            Position(guitar_string=6, fret=4),
        ]

        changed_positions = spread_right(positions)

        self.assertEqual(6, changed_positions[0].guitar_string)
        self.assertEqual(5, changed_positions[1].guitar_string)
        self.assertEqual(4, changed_positions[2].guitar_string)
        self.assertEqual(3, changed_positions[3].guitar_string)

    def test_spread_right_cannot_exceed_min_string(self):
        positions = [
            Position(guitar_string=1, fret=1),
            Position(guitar_string=1, fret=2),
            Position(guitar_string=1, fret=3),
            Position(guitar_string=1, fret=4),
        ]

        changed_positions = spread_right(positions)

        self.assertEqual(1, changed_positions[0].guitar_string)
        self.assertEqual(2, changed_positions[1].guitar_string)
        self.assertEqual(3, changed_positions[2].guitar_string)
        self.assertEqual(4, changed_positions[3].guitar_string)

    def test_spread_right_cannot_exceed_max_string(self):
        positions = [
            Position(guitar_string=1, fret=1),
            Position(guitar_string=1, fret=2),
            Position(guitar_string=1, fret=3),
            Position(guitar_string=1, fret=4),
            Position(guitar_string=1, fret=5),
            Position(guitar_string=1, fret=6),
            Position(guitar_string=1, fret=7),
        ]

        changed_positions = spread_right(positions)

        self.assertEqual(1, changed_positions[0].guitar_string)
        self.assertEqual(2, changed_positions[1].guitar_string)
        self.assertEqual(3, changed_positions[2].guitar_string)
        self.assertEqual(4, changed_positions[3].guitar_string)
        self.assertEqual(5, changed_positions[4].guitar_string)
        self.assertEqual(6, changed_positions[5].guitar_string)
        self.assertEqual(5, changed_positions[6].guitar_string)
