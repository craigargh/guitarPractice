class ExerciseGroup:
    def __init__(self, group_id, name='', description=''):
        self.group_id = group_id
        self.name = name
        self.description = description

        self.exercises = {}

    def __getitem__(self, item):
        return self.exercises[item]

    def __setitem__(self, variant_id, exercise_callable):
        self.exercises[variant_id] = exercise_callable
