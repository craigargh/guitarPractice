from itertools import chain

from guitarPractice.exercises.exercise import Exercise


class ExerciseBuilder:
    def __init__(self):
        self.shapes = None
        self.rhythm = None
        self.sequencer = None

        self.transformers = []

    def set_shapes(self, shapes):
        if self.shapes is not None:
            raise AttributeError("Can only set the exercise shapes once")

        self.shapes = shapes
        return self

    def transform(self, transformer):
        self.transformers.append(transformer)

        return self

    def set_rhythm(self, rhythm):
        if self.rhythm is not None:
            raise AttributeError("Can only set the rhythm once")

        self.rhythm = rhythm
        return self

    def set_sequencer(self, sequencer):
        if self.sequencer is not None:
            raise AttributeError("Can only set sequencer once")

        self.sequencer = sequencer
        return self

    def build(self):
        sequence = list(self.combine_sequences())

        return Exercise(shapes=self.shapes, sequence=sequence)

    def combine_sequences(self):
        try:
            positions = [
                shape.positions
                for shape in self.shapes
            ]

        except TypeError:
            raise AttributeError("shapes must be set with set_shapes()")

        return chain.from_iterable(positions)

