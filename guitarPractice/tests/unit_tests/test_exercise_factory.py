from unittest import TestCase
from unittest.mock import patch

from guitarPractice.exercises.exercise_factory import make_exercise, list_exercises


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

    @patch('guitarPractice.exercises.chord_changes.level_two')
    def test_make_exercise_returns_chord_changes_exercise_level_two(self, mock):
        mock.return_value = 'this is the exercise'
        exercise = make_exercise('chord-changes', 2)

        mock.assert_called_once()
        self.assertEqual(exercise, 'this is the exercise')

    @patch('guitarPractice.exercises.dexterity.level_one')
    def test_make_exercise_returns_chord_changes_exercise_level_one(self, mock):
        mock.return_value = 'this is the exercise'
        exercise = make_exercise('dexterity', 1)

        mock.assert_called_once()
        self.assertEqual(exercise, 'this is the exercise')

    @patch('guitarPractice.exercises.major_scale.level_one')
    def test_make_exercise_returns_major_scale_level_one(self, mock):
        mock.return_value = 'major scale exercise'
        exercise = make_exercise('major-scale', 1)

        mock.assert_called_once()
        self.assertEqual(exercise, 'major scale exercise')

    @patch('guitarPractice.exercises.pentatonic_scale.level_one')
    def test_make_exercise_returns_pentatonic_scale_level_one(self, mock):
        mock.return_value = 'pentatonic scale exercise'
        exercise = make_exercise('pentatonic-scale', 1)

        mock.assert_called_once()
        self.assertEqual(exercise, 'pentatonic scale exercise')

    def test_list_exercises_returns_a_list_of_exercises(self):
        exercises = list_exercises()

        self.assertEqual(len(exercises), 6)

    def test_list_exercises_returns_each_exercise(self):
        exercises = list_exercises()

        self.assertEqual(exercises[0].group_id, 'arpeggio-picking')
        self.assertEqual(exercises[1].group_id, 'chord-changes')
        self.assertEqual(exercises[2].group_id, 'dexterity')
        self.assertEqual(exercises[3].group_id, 'major-scale')
        self.assertEqual(exercises[4].group_id, 'pentatonic-scale')

    def test_make_exercise_returns_exception_for_invalid_exercise_name(self):
        with self.assertRaises(ValueError):
            make_exercise('spooky-skeletons', 1)

    def test_make_exercise_returns_exception_for_invalid_exercise_difficulty(self):
        with self.assertRaises(ValueError):
            make_exercise('arpeggio-picking', 1000000000)

