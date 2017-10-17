from unittest import TestCase

from flask import json

from guitarPractice.api.api import app


class TestExerciseApi(TestCase):
    def setUp(self):
        self.api = app.test_client()

    def test_get_rhythm_arpeggio_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_rhythm_arpeggio_one_contains_two_shapes(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')
        data = json.loads(response.data)

        self.assertEqual(len(data['shapes']), 2)

    def test_get_rhythm_arpeggio_one_contains_sequence_items(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')
        data = json.loads(response.data)

        self.assertGreater(len(data['sequence']), 0)

    def test_invalid_exercise_name_returns_404(self):
        response = self.api.get('/exercise/spooky-skeletons/1/')

        self.assertEqual(response.status_code, 404)
