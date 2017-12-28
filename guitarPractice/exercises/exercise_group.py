class ExerciseGroup:
    """
    Class to group several guitar exercises together and generate urls for the API.
    """

    def __init__(self, group_id, name='', description=''):
        self.group_id = group_id
        self.name = name
        self.description = description

        self.exercises = {}

    def __getitem__(self, item):
        return self.exercises[item]

    def __setitem__(self, variant_id, exercise_callable):
        self.exercises[variant_id] = exercise_callable

    @property
    def url_paths(self):
        return {
            exercise_id: f'/exercise/{self.group_id}/{exercise_id}'
            for exercise_id in self.exercises.keys()
        }
