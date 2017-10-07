from itertools import chain

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
        positions = [
            shape.positions
            for shape in self.shapes
        ]

        sequence = chain.from_iterable(positions)

        return Exercise(shapes=self.shapes, sequence=list(sequence))
