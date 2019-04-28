from copy import deepcopy
from itertools import groupby
from operator import attrgetter

from guitarPractice.exercise_builder.rhythms import make_default_rhythm


class Exercise:
    def __init__(self, shapes, sequence, rhythm=None):
        if not rhythm:
            rhythm = make_default_rhythm(sequence)

        self.shapes = shapes
        self.sequence = sequence
        self.rhythm = rhythm

    def as_dict(self):
        grouped_positions = self.group_positions(self.sequence)
        positions_with_rhythm = self.combine_rhythm(self.rhythm, grouped_positions)

        return {
            'sequence': positions_with_rhythm,
            'shapes': [shape.as_dict() for shape in self.shapes],
        }

    @staticmethod
    def group_positions(sequence):
        sorted_sequence = sorted(sequence, key=attrgetter('order'))
        grouped_sequence = groupby(sorted_sequence, key=attrgetter('order'))

        grouped_positions = []
        for index, positions in grouped_sequence:
            positions = [
                position.as_dict()
                for position in positions
            ]

            grouped_positions.append(
                {
                    'order': index,
                    'positions': positions
                }
            )
        return grouped_positions

    @staticmethod
    def combine_rhythm(rhythms, grouped_positions):
        grouped_positions = deepcopy(grouped_positions)

        for group, rhythm in zip(grouped_positions, rhythms):
            group['rhythm'] = rhythm

        return grouped_positions
