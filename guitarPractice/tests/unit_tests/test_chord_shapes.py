from unittest import TestCase

from guitarPractice.guitar_shapes import chord_shapes


class TestChordShapes(TestCase):
    def test_c_major(self):
        chord = chord_shapes.c_major()

        self.assertEqual(chord.name, 'C Major')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_c_major_seven(self):
        chord = chord_shapes.c_major_seven()

        self.assertEqual(chord.name, 'C Major 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_d_minor(self):
        chord = chord_shapes.d_minor()

        self.assertEqual(chord.name, 'D Minor')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_d_minor_seven(self):
        chord = chord_shapes.d_minor_seven()

        self.assertEqual(chord.name, 'D Minor 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_e_minor(self):
        chord = chord_shapes.e_minor()

        self.assertEqual(chord.name, 'E Minor')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_e_minor_seven(self):
        chord = chord_shapes.e_minor_seven()

        self.assertEqual(chord.name, 'E Minor 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_f_major(self):
        chord = chord_shapes.f_major()

        self.assertEqual(chord.name, 'F Major')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_f_major_seven(self):
        chord = chord_shapes.f_major_seven()

        self.assertEqual(chord.name, 'F Major 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_g_major(self):
        chord = chord_shapes.g_major()

        self.assertEqual(chord.name, 'G Major')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_g_seven(self):
        chord = chord_shapes.g_seven()

        self.assertEqual(chord.name, 'G 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 6)

    def test_a_minor(self):
        chord = chord_shapes.a_minor()

        self.assertEqual(chord.name, 'A Minor')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_a_minor_seven(self):
        chord = chord_shapes.a_minor_seven()

        self.assertEqual(chord.name, 'A Minor 7')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 5)

    def test_b_diminished(self):
        chord = chord_shapes.b_diminished()

        self.assertEqual(chord.name, 'B Diminished')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)

    def test_b_minor_seven_flat_five(self):
        chord = chord_shapes.b_minor_seven_flat_five()

        self.assertEqual(chord.name, 'B Minor 7 Flat 5')
        self.assertTrue(chord.is_chord)
        self.assertEqual(len(chord.positions), 4)
