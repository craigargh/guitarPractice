from unittest import TestCase

from guitarPractice.guitar_shapes import chord_shapes


class TestChordShapes(TestCase):
    def test_c_major(self):
        chord = chord_shapes.c_major()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_c_major_seven(self):
        chord = chord_shapes.c_major_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_d_minor(self):
        chord = chord_shapes.d_minor()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_d_minor_seven(self):
        chord = chord_shapes.d_minor_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_e_minor(self):
        chord = chord_shapes.e_minor()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_e_minor_seven(self):
        chord = chord_shapes.e_minor_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_f_major(self):
        chord = chord_shapes.f_major()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_f_major_seven(self):
        chord = chord_shapes.f_major_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_g_major(self):
        chord = chord_shapes.g_major()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_g_seven(self):
        chord = chord_shapes.g_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_a_minor(self):
        chord = chord_shapes.a_minor()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_a_minor_seven(self):
        chord = chord_shapes.a_minor_seven()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_b_diminished(self):
        chord = chord_shapes.b_diminished()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_b_diminished_seven_flat_five(self):
        chord = chord_shapes.b_diminished_seven_flat_five()

        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)
