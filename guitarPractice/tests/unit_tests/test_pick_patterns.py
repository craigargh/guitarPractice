from unittest import TestCase

from guitarPractice.guitar_shapes import pick_patterns


class TestPickPatterns(TestCase):
    def test_pattern_one_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[0]

        self.assertEqual(len(pattern), 8)

    def test_pattern_two_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[1]

        self.assertEqual(len(pattern), 8)

    def test_pattern_three_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[2]

        self.assertEqual(len(pattern), 8)

    def test_pattern_four_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[3]

        self.assertEqual(len(pattern), 8)

    def test_pattern_five_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[4]

        self.assertEqual(len(pattern), 8)

    def test_pattern_six_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[5]

        self.assertEqual(len(pattern), 8)

    def test_pattern_seven_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_one()[6]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_one_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[0]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_two_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[1]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_three_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[2]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_four_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[3]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_five_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[4]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_six_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[5]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_seven_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[6]

        self.assertEqual(len(pattern), 8)

    def test_alternate_pattern_eight_has_eight_notes(self):
        pattern = pick_patterns.pick_pattern_collection_two()[7]

        self.assertEqual(len(pattern), 8)

    def test_collection_one_has_seven_patterns(self):
        collection = pick_patterns.pick_pattern_collection_one()

        self.assertEqual(len(collection), 7)

    def test_collection_two_has_eight_patterns(self):
        collection = pick_patterns.pick_pattern_collection_two()

        self.assertEqual(len(collection), 8)
