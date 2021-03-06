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

    def test_url_is_generated_for_each_exercise(self):
        group = ExerciseGroup('picking-speed')

        group[1] = Mock()
        group[2] = Mock()
        group[6] = Mock()
        group[3] = Mock()

        urls = group.url_paths

        self.assertEqual(len(urls), 4)

    def test_url_paths_are_generated_with_group_id(self):
        group = ExerciseGroup('picking-speed')

        group[1] = Mock()
        group[2] = Mock()
        group[6] = Mock()
        group[3] = Mock()

        url_paths = group.url_paths

        self.assertEqual(url_paths[1], '/exercise/picking-speed/1')
        self.assertEqual(url_paths[2], '/exercise/picking-speed/2')
        self.assertEqual(url_paths[6], '/exercise/picking-speed/6')
        self.assertEqual(url_paths[3], '/exercise/picking-speed/3')

    def test_to_dict_sets_group_id(self):
        group = ExerciseGroup('picking-speed')
        group_dict = group.to_dict()

        self.assertEqual(group_dict['group_id'], 'picking-speed')

    def test_to_dict_sets_name(self):
        group = ExerciseGroup('picking-speed', name='Picking Speed')
        group_dict = group.to_dict()

        self.assertEqual(group_dict['name'], 'Picking Speed')

    def test_to_dict_sets_description(self):
        group = ExerciseGroup('picking-speed', description='Pick some speed')
        group_dict = group.to_dict()

        self.assertEqual(group_dict['description'], 'Pick some speed')

    def test_to_dict_sets_urls(self):
        group = ExerciseGroup('picking-speed')

        group[1] = Mock()
        group[2] = Mock()

        group_dict = group.to_dict()

        expected_urls = [
            {'key': 1, 'path': '/exercise/picking-speed/1'},
            {'key': 2, 'path': '/exercise/picking-speed/2'},
        ]

        self.assertEqual(group_dict['urls'], expected_urls)
