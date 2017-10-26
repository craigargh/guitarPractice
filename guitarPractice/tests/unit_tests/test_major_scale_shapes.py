from unittest import TestCase

from guitarPractice.guitar_shapes import major_scale_shapes


class TestMajorScaleShapes(TestCase):
    def test_e_phrygian_shape_name(self):
        shape = major_scale_shapes.e_phrygian()

        self.assertEqual('E Phrygian', shape.name)

    def test_e_phrygian_is_not_a_chord(self):
        shape = major_scale_shapes.e_phrygian()

        self.assertFalse(shape.is_chord)

    def test_e_phrygian_is_shiftable(self):
        shape = major_scale_shapes.e_phrygian()

        self.assertTrue(shape.is_shiftable)

    def test_e_phrygian_has_15_positions(self):
        shape = major_scale_shapes.e_phrygian()

        self.assertEqual(15, len(shape.positions))

    def test_f_lydian_shape_name(self):
        shape = major_scale_shapes.f_lydian()

        self.assertEqual('F Lydian', shape.name)

    def test_f_lydian_is_not_a_chord(self):
        shape = major_scale_shapes.f_lydian()

        self.assertFalse(shape.is_chord)

    def test_f_lydian_is_shiftable(self):
        shape = major_scale_shapes.f_lydian()

        self.assertTrue(shape.is_shiftable)

    def test_f_lydian_has_15_positions(self):
        shape = major_scale_shapes.f_lydian()

        self.assertEqual(15, len(shape.positions))

    def test_g_mixolydian_shape_name(self):
        shape = major_scale_shapes.g_mixolydian()

        self.assertEqual('G Mixolydian', shape.name)

    def test_g_mixolydian_is_not_a_chord(self):
        shape = major_scale_shapes.g_mixolydian()

        self.assertFalse(shape.is_chord)

    def test_g_mixolydian_is_shiftable(self):
        shape = major_scale_shapes.g_mixolydian()

        self.assertTrue(shape.is_shiftable)

    def test_g_mixolydian_has_15_positions(self):
        shape = major_scale_shapes.g_mixolydian()

        self.assertEqual(15, len(shape.positions))

    def test_a_aeolian_shape_name(self):
        shape = major_scale_shapes.a_aeolian()

        self.assertEqual('A Aeolian', shape.name)

    def test_a_aeolian_is_not_a_chord(self):
        shape = major_scale_shapes.a_aeolian()

        self.assertFalse(shape.is_chord)

    def test_a_aeolian_is_shiftable(self):
        shape = major_scale_shapes.a_aeolian()

        self.assertTrue(shape.is_shiftable)

    def test_a_aeolian_has_15_positions(self):
        shape = major_scale_shapes.a_aeolian()

        self.assertEqual(15, len(shape.positions))

    def test_b_locrian_shape_name(self):
        shape = major_scale_shapes.b_locrian()

        self.assertEqual('B Locrian', shape.name)

    def test_b_locrian_is_not_a_chord(self):
        shape = major_scale_shapes.b_locrian()

        self.assertFalse(shape.is_chord)

    def test_b_locrian_is_shiftable(self):
        shape = major_scale_shapes.b_locrian()

        self.assertTrue(shape.is_shiftable)

    def test_b_locrian_has_15_positions(self):
        shape = major_scale_shapes.b_locrian()

        self.assertEqual(15, len(shape.positions))

    def test_c_ionian_shape_name(self):
        shape = major_scale_shapes.c_ionian()

        self.assertEqual('C Ionian', shape.name)

    def test_c_ionian_is_not_a_chord(self):
        shape = major_scale_shapes.c_ionian()

        self.assertFalse(shape.is_chord)

    def test_c_ionian_is_shiftable(self):
        shape = major_scale_shapes.c_ionian()

        self.assertTrue(shape.is_shiftable)

    def test_c_ionian_has_15_positions(self):
        shape = major_scale_shapes.c_ionian()

        self.assertEqual(15, len(shape.positions))

    def test_d_dorian_shape_name(self):
        shape = major_scale_shapes.d_dorian()

        self.assertEqual('D Dorian', shape.name)

    def test_d_dorian_is_not_a_chord(self):
        shape = major_scale_shapes.d_dorian()

        self.assertFalse(shape.is_chord)

    def test_d_dorian_is_shiftable(self):
        shape = major_scale_shapes.d_dorian()

        self.assertTrue(shape.is_shiftable)

    def test_d_dorian_has_15_positions(self):
        shape = major_scale_shapes.d_dorian()

        self.assertEqual(15, len(shape.positions))
