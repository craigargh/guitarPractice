from copy import deepcopy
from itertools import chain

from guitarPractice.exercise_builder.exercise import Exercise


class ExerciseBuilder:
    def __init__(self):
        self.shapes = None
        self.rhythm = None
        self.sequencer = None

        self.transformers = []

    def set_shapes(self, shapes):
        if self.shapes is not None:
            raise AttributeError("Can only set the exercises shapes once")

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
        shapes = self._apply_sequencer(shapes, self.sequencer)
        shapes = self._apply_transformations(shapes, self.transformers)
        shapes = self._set_order_of_positions(shapes)

        sequence = list(self._combine_sequences(shapes))

        return Exercise(shapes=self.shapes, sequence=sequence)

    def _try_get_shapes(self):
        try:
            return list(self.shapes[:])

        except TypeError:
            raise AttributeError("shapes must be set with set_shapes()")

    @staticmethod
    def _apply_sequencer(shapes, sequencer):
        if not sequencer:
            return shapes

        copied_shapes = [
            deepcopy(shape)
            for shape in shapes
        ]

        sequenced_shapes = sequencer(copied_shapes)

        return [
            deepcopy(shape)
            for shape in sequenced_shapes
        ]


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
    def _set_order_of_positions(shapes):
        shapes = list(deepcopy(shapes))

        index = 0
        for shape in shapes:
            positions = deepcopy(shape.positions)

            if shape.is_picked:
                for position in positions:
                    position.order = index
                    index += 1
            else:
                for position in positions:
                    position.order = index
                index += 1

            shape.positions = positions
        return shapes

    @staticmethod
    def _combine_sequences(shapes):
        positions = [
            shape.positions
            for shape in shapes
        ]

        return chain.from_iterable(positions)
