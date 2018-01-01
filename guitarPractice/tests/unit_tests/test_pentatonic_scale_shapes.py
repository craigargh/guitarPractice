from unittest import TestCase

from guitarPractice.guitar_shapes import pentatonic_scale_shapes


class TestPentatonicShapes(TestCase):
    def test_c_pentatonic_shape_name(self):
        shape = pentatonic_scale_shapes.c_major()

        self.assertEqual(shape.name, 'C Major Pentatonic')

    def test_c_pentatonic_is_not_a_chord(self):
        shape = pentatonic_scale_shapes.c_major()

        self.assertFalse(shape.is_chord)

    def test_c_pentatonic_is_shiftable(self):
        shape = pentatonic_scale_shapes.c_major()

        self.assertTrue(shape.is_shiftable)

    def test_c_pentatonic_has_eleven_positions(self):
        shape = pentatonic_scale_shapes.c_major()

        self.assertEqual(len(shape.positions), 11)

    def test_d_dorian_pentatonic_shape_name(self):
        shape = pentatonic_scale_shapes.d_dorian()

        self.assertEqual(shape.name, 'D Dorian Pentatonic')

    def test_d_dorian_pentatonic_is_not_a_chord(self):
        shape = pentatonic_scale_shapes.d_dorian()

        self.assertFalse(shape.is_chord)

    def test_d_dorian_pentatonic_is_shiftable(self):
        shape = pentatonic_scale_shapes.d_dorian()

        self.assertTrue(shape.is_shiftable)

    def test_d_dorian_pentatonic_has_eleven_positions(self):
        shape = pentatonic_scale_shapes.d_dorian()

        self.assertEqual(len(shape.positions), 11)

    def test_e_phrygian_pentatonic_shape_name(self):
        shape = pentatonic_scale_shapes.e_phrygian()

        self.assertEqual(shape.name, 'E Phrygian Pentatonic')

    def test_e_phrygian_pentatonic_is_not_a_chord(self):
        shape = pentatonic_scale_shapes.e_phrygian()

        self.assertFalse(shape.is_chord)

    def test_e_phrygian_pentatonic_is_shiftable(self):
        shape = pentatonic_scale_shapes.e_phrygian()

        self.assertTrue(shape.is_shiftable)

    def test_e_phrygian_pentatonic_has_eleven_positions(self):
        shape = pentatonic_scale_shapes.e_phrygian()

        self.assertEqual(len(shape.positions), 11)

    def test_g_mixolydian_pentatonic_shape_name(self):
        shape = pentatonic_scale_shapes.g_mixolydian()

        self.assertEqual(shape.name, 'G Mixolydian Pentatonic')

    def test_g_mixolydian_pentatonic_is_not_a_chord(self):
        shape = pentatonic_scale_shapes.g_mixolydian()

        self.assertFalse(shape.is_chord)

    def test_g_mixolydian_pentatonic_is_shiftable(self):
        shape = pentatonic_scale_shapes.g_mixolydian()

        self.assertTrue(shape.is_shiftable)

    def test_g_mixolydian_pentatonic_has_eleven_positions(self):
        shape = pentatonic_scale_shapes.g_mixolydian()

        self.assertEqual(len(shape.positions), 11)

    def test_a_minor_pentatonic_shape_name(self):
        shape = pentatonic_scale_shapes.a_minor()

        self.assertEqual(shape.name, 'A Minor Pentatonic')

    def test_a_minor_pentatonic_is_not_a_chord(self):
        shape = pentatonic_scale_shapes.a_minor()

        self.assertFalse(shape.is_chord)

    def test_a_minor_pentatonic_is_shiftable(self):
        shape = pentatonic_scale_shapes.a_minor()

        self.assertTrue(shape.is_shiftable)

    def test_a_minor_pentatonic_has_eleven_positions(self):
        shape = pentatonic_scale_shapes.a_minor()

        self.assertEqual(len(shape.positions), 11)
