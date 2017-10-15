from unittest import TestCase

from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


class GuitarShapeTest(TestCase):
    def test_root_note_is_set(self):
        c_major = GuitarShape('C', 'major', [])

        self.assertEqual('C', c_major.root_note)

    def test_tonality_is_set(self):
        c_major = GuitarShape('C', 'major', [])

        self.assertEqual('major', c_major.tonality)

    def test_name_is_built_from_root_note_and_tonality(self):
        c_major = GuitarShape('C', 'major', [])

        self.assertEqual('C major', c_major.name)

    def test_chord_length_is_set_from_number_of_positions(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertEqual(3, len(c_major))

    def test_can_access_chord_positions(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertEqual(1, c_major[0])
        self.assertEqual(2, c_major[1])
        self.assertEqual(3, c_major[2])

    def test_iterating_over_chord_returns_positions_in_order(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        results = []

        for value in c_major:
            results.append(value)

        self.assertEqual(1, results[0])
        self.assertEqual(2, results[1])
        self.assertEqual(3, results[2])

    def test_apply_transformation_changes_positions(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        transformed_shape = c_major.transform(reversed)

        self.assertEqual(transformed_shape.positions, [3, 2, 1])

    def test_apply_transformation_does_not_modify_original_shape(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        c_major.transform(reversed)

        self.assertEqual(c_major.positions, [1, 2, 3])

    def test_str_returns_chord_name(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertEqual('C major', str(c_major))

    def test_repr_returns_description_of_chord(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertEqual("GuitarShape('C', 'major', [1, 2, 3])", repr(c_major))

    def test_is_picked_defaults_to_true(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertTrue(c_major.is_picked)

    def test_is_strummed_defaults_to_false(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        self.assertFalse(c_major.is_strummed)

    def test_can_set_picked_to_false(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        c_major.is_picked = False

        self.assertFalse(c_major.is_picked)
        self.assertTrue(c_major.is_strummed)

    def test_can_set_is_strummed_to_true(self):
        c_major = GuitarShape('C', 'major', [1, 2, 3])

        c_major.is_strummed = True

        self.assertFalse(c_major.is_picked)
        self.assertTrue(c_major.is_strummed)

    def test_transform_creates_deep_copies_of_positions(self):
        position = Position(guitar_string=6)
        c_major = GuitarShape('C', 'major', [position])

        transformed_shape = c_major.transform(lambda positions: positions * 2)

        self.assertEqual(len(transformed_shape.positions), 2)
        self.assertIsNot(transformed_shape[0], transformed_shape[1])

    def test_transform_does_not_change_original_list(self):
        def test_transformer(positions):
            positions.pop(0)
            return positions

        position = Position(guitar_string=6)
        c_major = GuitarShape('C', 'major', [position])

        transformed_shape = c_major.transform(test_transformer)

        self.assertEqual(len(c_major.positions), 1)
        self.assertEqual(len(transformed_shape.positions), 0)

    def test_transform_does_not_change_positions_in_original_list(self):
        def test_transformer(positions):
            positions[0].guitar_string = 5
            return positions

        position = Position(guitar_string=6)
        c_major = GuitarShape('C', 'major', [position])

        transformed_shape = c_major.transform(test_transformer)

        self.assertEqual(c_major.positions[0].guitar_string, 6)
        self.assertEqual(transformed_shape.positions[0].guitar_string, 5)

    def test_is_chord(self):
        positions = [
            Position(guitar_string=6),
            Position(guitar_string=5)
        ]
        shape = GuitarShape('C', 'major', positions)

        self.assertTrue(shape.is_chord)

    def test_is_not_chord_when_only_one_position(self):
        positions = [
            Position(guitar_string=6),
        ]
        shape = GuitarShape('C', 'major', positions)

        self.assertFalse(shape.is_chord)

    def test_is_not_chord_when_two_positions_on_same_string(self):
        positions = [
            Position(guitar_string=6),
            Position(guitar_string=6),
        ]
        shape = GuitarShape('C', 'major', positions)

        self.assertFalse(shape.is_chord)

    def test_is_not_chord_when_more_than_two_positions_on_same_string(self):
        positions = [
            Position(guitar_string=6),
            Position(guitar_string=6),
            Position(guitar_string=6),
        ]
        shape = GuitarShape('C', 'major', positions)

        self.assertFalse(shape.is_chord)
