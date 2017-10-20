from unittest import TestCase

from guitarPractice.guitar_shapes.chromatic_collections import make_chromatic_shape


class TestChromaticCollections(TestCase):
    def test_make_chromatic_shape_makes_a_quantity_of_positions(self):
        shape = make_chromatic_shape(quantity=4)

        self.assertEqual(4, len(shape.positions))

    def test_make_chromatic_shape_sets_guitar_string(self):
        shape = make_chromatic_shape(quantity=2, guitar_string=3)

        self.assertEqual(2, len(shape.positions))
        self.assertEqual(3, shape.positions[0].guitar_string)
        self.assertEqual(3, shape.positions[1].guitar_string)

    def test_make_chromatic_shape_sets_fret(self):
        shape = make_chromatic_shape(quantity=4, start_fret=4)

        self.assertEqual(4, shape.positions[0].fret)
        self.assertEqual(5, shape.positions[1].fret)
        self.assertEqual(6, shape.positions[2].fret)
        self.assertEqual(7, shape.positions[3].fret)

    def test_make_chromatic_shape_sets_finger(self):
        shape = make_chromatic_shape(quantity=8)

        self.assertEqual(1, shape.positions[0].finger)
        self.assertEqual(2, shape.positions[1].finger)
        self.assertEqual(3, shape.positions[2].finger)
        self.assertEqual(4, shape.positions[3].finger)
        self.assertEqual(1, shape.positions[4].finger)
        self.assertEqual(2, shape.positions[5].finger)
        self.assertEqual(3, shape.positions[6].finger)
        self.assertEqual(4, shape.positions[7].finger)

    def test_make_chromatic_shape_sets_root_note(self):
        shape = make_chromatic_shape(root_note="A")

        self.assertEqual("A", shape.root_note)

    def test_make_chromatic_shape_sets_tonality(self):
        shape = make_chromatic_shape()

        self.assertEqual("Chromatic", shape.tonality)

    def test_make_chromatic_shape_sets_default_root_note(self):
        shape = make_chromatic_shape()

        self.assertEqual("", shape.root_note)

    def test_make_chromatic_shape_sets_default_quantity(self):
        shape = make_chromatic_shape()

        self.assertEqual(1, len(shape.positions))

    def test_make_chromatic_shape_sets_default_start_fret(self):
        shape = make_chromatic_shape()

        self.assertEqual(1, shape.positions[0].fret)

    def test_make_chromatic_shape_sets_default_guitar_string(self):
        shape = make_chromatic_shape()

        self.assertEqual(1, shape.positions[0].guitar_string)
