from unittest import TestCase

from guitarPractice.guitar_shapes import pick_patterns


class TestPickPatterns(TestCase):
    def test_pattern_one_has_eight_notes(self):
        pattern = pick_patterns.pattern_one

        self.assertEqual(len(pattern), 8)

    def test_pattern_two_has_eight_notes(self):
        pattern = pick_patterns.pattern_two

        self.assertEqual(len(pattern), 8)

    def test_pattern_three_has_eight_notes(self):
        pattern = pick_patterns.pattern_three

        self.assertEqual(len(pattern), 8)

    def test_pattern_four_has_eight_notes(self):
        pattern = pick_patterns.pattern_four

        self.assertEqual(len(pattern), 8)

    def test_pattern_five_has_eight_notes(self):
        pattern = pick_patterns.pattern_five

        self.assertEqual(len(pattern), 8)

    def test_pattern_six_has_eight_notes(self):
        pattern = pick_patterns.pattern_six

        self.assertEqual(len(pattern), 8)

    def test_pattern_seven_has_eight_notes(self):
        pattern = pick_patterns.pattern_seven

        self.assertEqual(len(pattern), 8)

    def test_pattern_eight_has_eight_notes(self):
        pattern = pick_patterns.pattern_eight

        self.assertEqual(len(pattern), 8)

    def test_pattern_nine_has_eight_notes(self):
        pattern = pick_patterns.pattern_nine

        self.assertEqual(len(pattern), 8)

    def test_pattern_ten_has_eight_notes(self):
        pattern = pick_patterns.pattern_ten

        self.assertEqual(len(pattern), 8)

    def test_collection_one_has_ten_patterns(self):
        collection = pick_patterns.pick_pattern_collection_one()

        self.assertEqual(len(collection), 10)
