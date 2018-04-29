from unittest import TestCase

from flask import json

from guitarPractice.api.flask_api import app


class TestExerciseApi(TestCase):
    def setUp(self):
        self.api = app.test_client()

    def test_invalid_exercise_name_returns_404(self):
        response = self.api.get('/exercise/spooky-skeletons/1/')

        self.assertEqual(response.status_code, 404)

    def test_invalid_exercise_name_returns_error_message(self):
        response = self.api.get('/exercise/spooky-skeletons/1/')

        self.assertEqual(response.data, b'Invalid exercise name or difficulty')

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

    def test_get_arpeggio_picking_one_has_rhythm(self):
        response = self.api.get('/exercise/arpeggio-picking/1/')
        data = json.loads(response.data)

        self.assertGreater(len(data['rhythm']), 0)

    def test_get_arpeggio_picking_two_exercise_returns_ok(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')

        self.assertEqual(response.status_code, 200)

    def test_get_arpeggio_picking_two_has_shapes(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['shapes'])

    def test_get_arpeggio_picking_two_has_sequence(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])

    def test_get_arpeggio_picking_two_has_rhythm(self):
        response = self.api.get('/exercise/arpeggio-picking/2/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['rhythm'])

    def test_get_chords_changes_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/chord-changes/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_chords_changes_one_has_shapes(self):
        response = self.api.get('/exercise/chord-changes/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['shapes'])

    def test_get_chords_changes_one_has_sequence(self):
        response = self.api.get('/exercise/chord-changes/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])

    def test_get_chords_changes_one_has_rhythm(self):
        response = self.api.get('/exercise/chord-changes/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['rhythm'])

    def test_get_major_scale_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/major-scale/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_major_scale_one_has_shapes(self):
        response = self.api.get('/exercise/major-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['shapes'])

    def test_get_major_scale_one_has_sequence(self):
        response = self.api.get('/exercise/major-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])

    def test_get_major_scale_one_has_rhythm(self):
        response = self.api.get('/exercise/major-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['rhythm'])

    def test_get_pentatonic_scale_one_exercise_returns_ok(self):
        response = self.api.get('/exercise/pentatonic-scale/1/')

        self.assertEqual(response.status_code, 200)

    def test_get_pentatonic_scale_one_has_shapes(self):
        response = self.api.get('/exercise/pentatonic-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['shapes'])

    def test_get_pentatonic_scale_one_has_sequence(self):
        response = self.api.get('/exercise/pentatonic-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['sequence'])

    def test_get_pentatonic_scale_one_has_rhythm(self):
        response = self.api.get('/exercise/pentatonic-scale/1/')
        data = json.loads(response.data)

        self.assertIsNotNone(data['rhythm'])

    def test_get_exercises_returns_list_of_exercises(self):
        response = self.api.get('/exercises/')
        response_json = json.loads(response.data)

        self.assertEqual(len(response_json), 6)

    def test_get_exercises_have_group_id_property(self):
        response = self.api.get('/exercises/')
        response_json = json.loads(response.data)

        self.assertEqual(response_json[0]['group_id'], 'arpeggio-picking')

    def test_get_exercises_have_name_property(self):
        response = self.api.get('/exercises/')
        response_json = json.loads(response.data)

        self.assertEqual(response_json[0]['name'], 'Arpeggio Picking')

    def test_get_exercises_have_description_property(self):
        response = self.api.get('/exercises/')
        response_json = json.loads(response.data)

        self.assertEqual(response_json[0]['description'], 'Pick some arpeggios')

    def test_get_exercises_have_urls_for_levels(self):
        response = self.api.get('/exercises/')
        response_json = json.loads(response.data)

        expected_urls = [
            {'key': 1, 'path': '/exercise/arpeggio-picking/1'},
            {'key': 2, 'path': '/exercise/arpeggio-picking/2'},
        ]

        self.assertEqual(response_json[0]['urls'], expected_urls)
