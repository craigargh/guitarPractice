from unittest import TestCase

from flask import json

from guitarPractice.api.api import app


class TestExerciseApi(TestCase):
    def setUp(self):
        self.api = app.test_client()

    def test_get_arpeggio_picking_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_arpeggio_picking_one_contains_two_shapes(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')
        data = json.loads(response.data)

        self.assertEqual(len(data['shapes']), 2)

    def test_get_arpeggio_picking_one_contains_sequence_items(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')
        data = json.loads(response.data)

        self.assertGreater(len(data['sequence']), 0)

    def test_invalid_exercise_name_returns_404(self):
        response = self.api.get('/exercise/spooky-skeletons/1/')

        self.assertEqual(response.status_code, 404)

    def test_invalid_exercise_name_returns_error_message(self):
        response = self.api.get('/exercise/spooky-skeletons/1/')

        self.assertEqual(response.data, b'Invalid exercise name or difficulty')

    def test_get_arpeggio_picking_two_exercise_returns_ok(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')

        self.assertEqual(response.status_code, 200)

    def test_get_arpeggio_picking_two_has_shapes_and_sequence(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])
        self.assertIsNotNone(data['shapes'])

    def test_get_chords_changes_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/chord-changes/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_chords_changes_one_has_shapes_and_sequence(self):
        response = self.api.get('/exercise/chord-changes/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])
        self.assertIsNotNone(data['shapes'])

    def test_get_major_scale_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/major-scale/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_major_scale_one_has_shapes_and_sequence(self):
        response = self.api.get('/exercise/major-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])
        self.assertIsNotNone(data['shapes'])
