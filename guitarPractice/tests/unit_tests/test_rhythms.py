import random
from unittest import TestCase
from unittest.mock import patch

from guitarPractice.exercise_builder.rhythms import random_choices


class TestRandomFromSelection(TestCase):
    def setUp(self):
        self.choice_patch = patch('guitarPractice.exercise_builder.rhythms.choice')
        self.choice_mock = self.choice_patch.start()

        random.seed(0)
        self.choice_mock.side_effect = random.choice

    def tearDown(self):
        self.choice_patch.stop()

    def test_returns_a_number_of_beats(self):
        choices = [
            [
                {'duration': 1, 'division': 4}
            ],
            [
                {'duration': 1, 'division': 8},
                {'duration': 1, 'division': 8}
            ],
        ]

        result = random_choices(4, choices, 7)

        self.assertEqual(7, len(result))

    def test_returns_rhythms(self):
        choices = [
            [
                {'duration': 1, 'division': 4}
            ],
            [
                {'duration': 1, 'division': 8},
                {'duration': 1, 'division': 8}
            ],
        ]

        result = random_choices(4, choices, 7)

        expected_result = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 4},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8}
        ]

        self.assertEqual(expected_result, result)

    def test_longer_sequence_length_extends_rhythm(self):
        choices = [
            [
                {'duration': 1, 'division': 8},
                {'duration': 1, 'division': 8}
            ],
        ]

        result = random_choices(2, choices, 8)

        expected_result = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
        ]

        self.assertEqual(8, len(result))
        self.assertEqual(expected_result, result)

    def test_shorter_sequence_length_shortens_rhythm(self):
        choices = [
            [
                {'duration': 1, 'division': 8},
                {'duration': 1, 'division': 8}
            ],
        ]

        result = random_choices(4, choices, 2)

        expected_result = [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
        ]

        self.assertEqual(2, len(result))
        self.assertEqual(expected_result, result)
