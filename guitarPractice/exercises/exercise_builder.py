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
        sequence = list(self.combine_sequences())

        return Exercise(shapes=self.shapes, sequence=sequence)

    def combine_sequences(self):
        positions = [
            shape.positions
            for shape in self.shapes
        ]

        return chain.from_iterable(positions)

