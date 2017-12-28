from unittest import TestCase
from unittest.mock import Mock

from guitarPractice.exercises.exercise_group import ExerciseGroup


class TestExerciseGroup(TestCase):
    def test_can_set_exercise_group_id(self):
        group = ExerciseGroup('picking-speed')

        self.assertEqual(group.group_id, 'picking-speed')

    def test_can_add_a_exercise_to_the_exercise_group(self):
        group = ExerciseGroup('picking-speed')

        group[1] = Mock()

        self.assertEqual(len(group.exercises), 1)
        self.assertIn(1, group.exercises)

    def test_callable_is_set_for_exercises(self):
        group = ExerciseGroup('picking-speed')

        exercise_callable = Mock()
        group[1] = exercise_callable

        self.assertEqual(group[1], exercise_callable)

    def test_can_set_human_readable_name(self):
        group = ExerciseGroup('picking-speed', name='Picking Speed')

        self.assertEqual(group.name, 'Picking Speed')

    def test_can_set_group_description(self):
        group = ExerciseGroup('picking-speed', description='Pick Faster')

        self.assertEqual(group.description, 'Pick Faster')
