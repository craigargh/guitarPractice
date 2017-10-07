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
        shapes = self._try_get_shapes()
        shapes = self._apply_transformations(shapes, self.transformers)

        sequence = list(self._combine_sequences(shapes))

        return Exercise(shapes=self.shapes, sequence=sequence)

    def _try_get_shapes(self):
        try:
            return self.shapes[:]

        except TypeError:
            raise AttributeError("shapes must be set with set_shapes()")

    @staticmethod
    def _apply_transformations(shapes, transformers):
        if transformers:
            updated_shapes = []

            for shape in shapes:
                for transformer in transformers:
                    shape = shape.transform(transformer)

                updated_shapes.append(shape)

            return updated_shapes
        else:
            return shapes

    @staticmethod
    def _combine_sequences(shapes):
        positions = [
            shape.positions
            for shape in shapes
        ]

        return chain.from_iterable(positions)
