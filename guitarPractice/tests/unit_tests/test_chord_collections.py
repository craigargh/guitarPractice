from unittest import TestCase

from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords, c_major_scale_seven_chords, \
    c_major_scale_add_9_chords


class TestCMajorTriads(TestCase):
    def setUp(self):
        self.chords = c_major_scale_triad_chords()

    def test_collection_contains_seven_chords(self):
        self.assertEqual(len(self.chords), 7)

    def test_first_chord_is_c_major(self):
        self.assertEqual(self.chords[0].name, 'C Major')

    def test_second_chord_is_d_minor(self):
        self.assertEqual(self.chords[1].name, 'D Minor')

    def test_third_chord_is_e_minor(self):
        self.assertEqual(self.chords[2].name, 'E Minor')

    def test_fourth_chord_is_f_major(self):
        self.assertEqual(self.chords[3].name, 'F Major')

    def test_fifth_chord_is_g_major(self):
        self.assertEqual(self.chords[4].name, 'G Major')

    def test_sixth_chord_is_a_minor(self):
        self.assertEqual(self.chords[5].name, 'A Minor')

    def test_seventh_chord_is_b_diminished(self):
        self.assertEqual(self.chords[6].name, 'B Diminished')


class TestCMajorSeventh(TestCase):
    def setUp(self):
        self.chords = c_major_scale_seven_chords()

    def test_collection_contains_seven_chords(self):
        self.assertEqual(len(self.chords), 7)

    def test_first_chord_is_c_major_7(self):
        self.assertEqual(self.chords[0].name, 'C Major 7')

    def test_second_chord_is_d_minor_7(self):
        self.assertEqual(self.chords[1].name, 'D Minor 7')

    def test_third_chord_is_e_minor_7(self):
        self.assertEqual(self.chords[2].name, 'E Minor 7')

    def test_fourth_chord_is_f_major_7(self):
        self.assertEqual(self.chords[3].name, 'F Major 7')

    def test_fifth_chord_is_g_7(self):
        self.assertEqual(self.chords[4].name, 'G 7')

    def test_sixth_chord_is_a_minor_7(self):
        self.assertEqual(self.chords[5].name, 'A Minor 7')

    def test_seventh_chord_is_b_minor_7_flat_5(self):
        self.assertEqual(self.chords[6].name, 'B Minor 7 Flat 5')


class TestCMajorAdd9(TestCase):
    def setUp(self):
        self.chords = c_major_scale_add_9_chords()

    def test_collection_contains_seven_chords(self):
        self.assertEqual(len(self.chords), 7)

    def test_first_chord_is_c_major_add_9(self):
        self.assertEqual(self.chords[0].name, 'C Major add 9')

    def test_second_chord_is_d_minor_add_9(self):
        self.assertEqual(self.chords[1].name, 'D Minor add 9')

    def test_third_chord_is_e_minor_add_9(self):
        self.assertEqual(self.chords[2].name, 'E Minor flat 9')

    def test_fourth_chord_is_f_major_add_9(self):
        self.assertEqual(self.chords[3].name, 'F Major add 9')

    def test_fifth_chord_is_g_add_9(self):
        self.assertEqual(self.chords[4].name, 'G Major add 9')

    def test_sixth_chord_is_a_minor_add_9(self):
        self.assertEqual(self.chords[5].name, 'A Minor add 9')

    def test_seventh_chord_is_b_diminished(self):
        self.assertEqual(self.chords[6].name, 'B Diminished flat 9')
