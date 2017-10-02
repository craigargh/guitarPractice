from unittest import TestCase

from guitarPractice.exercises.position import Position


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
