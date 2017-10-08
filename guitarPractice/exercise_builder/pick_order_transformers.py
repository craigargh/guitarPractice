from copy import deepcopy
from itertools import cycle
from typing import List

from guitarPractice.guitar_shapes.position import Position


def ascending_transformer(positions: List[Position], sequence_length: int = None):
    sequence = positions[:]

    sequence_length_is_set = sequence_length is not None and sequence_length > 0

    if sequence_length_is_set and sequence_length < len(positions):
        sequence = shorten_positions(positions, sequence_length)

    elif sequence_length_is_set and sequence_length > len(positions):
        sequence = lengthen_shape(positions, sequence_length)

    return sequence


def shorten_positions(positions, sequence_length):
    return positions[:sequence_length]


def lengthen_shape(positions, sequence_length):
    shape_repeater = cycle(positions)

    partial_repeats_length = sequence_length % len(positions)
    if partial_repeats_length != 0:
        partial_repeats_sequence = deepcopy(positions[-partial_repeats_length:])
    else:
        partial_repeats_sequence = []

    full_repeats_length = sequence_length - partial_repeats_length

    full_repeats_sequence = []

    for _ in range(full_repeats_length):
        full_repeats_sequence.append(deepcopy(next(shape_repeater)))

    return full_repeats_sequence + partial_repeats_sequence
