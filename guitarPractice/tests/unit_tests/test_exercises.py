from unittest import TestCase
from unittest.mock import patch

from guitarPractice.exercises.exercises import make_exercise


class TestExercises(TestCase):
    @patch('guitarPractice.exercises.arpeggio_picking.level_one')
    def test_make_exercise_returns_arpeggio_picking_exercise_level_one(self, mock):
        mock.return_value = 'this is the exercise'
        exercise = make_exercise('arpeggio-picking', 1)

        mock.assert_called_once()
        self.assertEqual(exercise, 'this is the exercise')

    @patch('guitarPractice.exercises.arpeggio_picking.level_two')
    def test_make_exercise_returns_arpeggio_picking_exercise_level_two(self, mock):
        mock.return_value = 'this is the exercise'
        exercise = make_exercise('arpeggio-picking', 2)

        mock.assert_called_once()
        self.assertEqual(exercise, 'this is the exercise')

    @patch('guitarPractice.exercises.chord_changes.level_one')
    def test_make_exercise_returns_chord_changes_exercise_level_one(self, mock):
        mock.return_value = 'this is the exercise'
        exercise = make_exercise('chord-changes', 1)

        mock.assert_called_once()
        self.assertEqual(exercise, 'this is the exercise')
