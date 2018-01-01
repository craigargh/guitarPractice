from unittest import TestCase

from guitarPractice.guitar_shapes import scale_collections


class TestScaleCollections(TestCase):
    def test_c_major_modes_contains_8_shapes(self):
        shapes = scale_collections.c_major_modes()

        self.assertEqual(7, len(shapes))

    def test_c_major_pentatonic_modes_contains_5_shapes(self):
        shapes = scale_collections.c_major_pentatonic_modes()

        self.assertEqual(5, len(shapes))
