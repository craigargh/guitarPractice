from guitarPractice.exercises.exercise import Exercise


class ExerciseBuilder:
    def __init__(self):
        self.shapes = None

    def set_shapes(self, shapes):
        if self.shapes is not None:
            raise AttributeError("You can only set the exercise shapes once")

        self.shapes = shapes
        return self

    def build(self):
        return Exercise(shapes=self.shapes, sequence=[])
