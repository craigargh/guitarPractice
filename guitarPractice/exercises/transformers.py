from itertools import cycle
from typing import List

from guitarPractice.exercises.chord import Chord


def ascending_transformer(shape: List[Chord], sequence_length: int = None):
    sequence_length_is_set = sequence_length is not None and sequence_length > 0

    if sequence_length_is_set and sequence_length <= len(shape):
        sequence = shorten_shape(shape, sequence_length)

    elif sequence_length_is_set and sequence_length > len(shape):
        sequence = lengthen_shape(shape, sequence_length)

    else:
        sequence = shape[:]

    return sequence


def shorten_shape(shape, sequence_length):
    return shape[:sequence_length]


def lengthen_shape(shape, sequence_length):
    shape_repeater = cycle(shape)

    partial_repeats_length = sequence_length % len(shape)
    partial_repeats_sequence = shape[-partial_repeats_length:]

    full_repeats_length = sequence_length - partial_repeats_length

    full_repeats_sequence = []

    for _ in range(full_repeats_length):
        full_repeats_sequence.append(next(shape_repeater))

    return full_repeats_sequence + partial_repeats_sequence
