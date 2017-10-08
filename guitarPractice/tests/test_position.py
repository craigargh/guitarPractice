from unittest import TestCase

from guitarPractice.guitar_shapes.position import Position


class PositionTest(TestCase):
    def test_position_stores_string_number(self):
        position = Position(fret=2, guitar_string=6, finger=5)

        self.assertEqual(6, position.guitar_string)

    def test_position_stores_fret_number(self):
        position = Position(fret=2, guitar_string=6, finger=5)

        self.assertEqual(2, position.fret)

    def test_position_stores_finger_number(self):
        position = Position(fret=2, guitar_string=6, finger=5)

        self.assertEqual(5, position.finger)

    def test_position_is_highlighted_is_false_by_default(self):
        position = Position(fret=2, guitar_string=6, finger=5)

        self.assertEqual(False, position.is_highlighted)

    def test_position_stores_is_highlighted(self):
        position = Position(fret=2, guitar_string=6, finger=5, is_highlighted=True)

        self.assertEqual(True, position.is_highlighted)

    def test_position_fret_defaults_to_0(self):
        position = Position(guitar_string=1)

        self.assertEqual(0, position.fret)

    def test_finger_defaults_to_0(self):
        position = Position(guitar_string=1)

        self.assertEqual(0, position.finger)

    def test_duration_is_set(self):
        position = Position(guitar_string=1, duration=0.5)

        self.assertEqual(position.duration, 0.5)

    def test_default_duration_is_set(self):
        position = Position(guitar_string=1)

        self.assertEqual(position.duration, 1)

    def test_str_returns_a_description_of_the_position(self):
        position = Position(guitar_string=1, finger=2, fret=3)

        self.assertEqual("(string: 1, fret: 3, finger: 2)", str(position))

    def test_repr_returns_description_of_the_position(self):
        position = Position(guitar_string=1, finger=2, fret=3)

        expected_string = "Position(guitar_string=1, fret=3, finger=2)"

        self.assertEqual(expected_string, repr(position))
