from unittest import TestCase

from guitarPractice.guitar_shapes import scale_collections


class TestScaleCollections(TestCase):
    def test_c_major_modes_contains_8_shapes(self):
        shapes = scale_collections.c_major_modes()

        self.assertEqual(7, len(shapes))
