from copy import deepcopy
from itertools import chain
from operator import attrgetter

from guitarPractice.exercise_builder.exercise import Exercise


class ExerciseBuilder:
    def __init__(self):
        self._shapes = None
        self._sequencers = []

        self._transformers = []
        self._display_modified_shapes = False

        self._rhythm = None

    def set_shapes(self, shapes):
        if self._shapes is not None:
            raise AttributeError("Can only set the exercises shapes once")

        self._shapes = shapes
        return self

    def set_rhythm(self, rhythm):
        if self._rhythm is not None:
            raise AttributeError("Can only set rhythm once")

        self._rhythm = rhythm
        return self

    def transform(self, transformer):
        self._transformers.append(transformer)

        return self

    def sequence(self, sequencer):
        self._sequencers.append(sequencer)
        return self

    def display_modified_shapes(self, display):
        self._display_modified_shapes = display

        return self

    def build(self):
        modified_shapes = self._try_get_shapes()
        modified_shapes = self._apply_sequencers(modified_shapes, self._sequencers)
        modified_shapes = self._apply_transformations(modified_shapes, self._transformers)
        modified_shapes = self._set_order_of_positions(modified_shapes)

        sequence = list(self._combine_sequences(modified_shapes))

        rhythm = self._make_rhythm(self._rhythm, sequence)

        shapes = self._shapes
        if self._display_modified_shapes:
            shapes = modified_shapes

        return Exercise(shapes=shapes, sequence=sequence, rhythm=rhythm)

    def _try_get_shapes(self):
        try:
            return list(self._shapes[:])

        except TypeError:
            raise AttributeError("shapes must be set with set_shapes()")

    @staticmethod
    def _apply_sequencers(shapes, sequencers):
        if not sequencers:
            return shapes

        copied_shapes = [
            deepcopy(shape)
            for shape in shapes
        ]

        for sequencer in sequencers:
            copied_shapes = sequencer(copied_shapes)

        return [
            deepcopy(shape)
            for shape in copied_shapes
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

    @staticmethod
    def _make_rhythm(rhythm_generator, sequence):
        if rhythm_generator is None:
            return None

        beats = max(sequence, key=attrgetter('order'))
        return rhythm_generator(beats.order + 1)
