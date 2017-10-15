import random
from functools import partial

from guitarPractice.exercise_builder.transformers.transformer_utils import resize_sequence


def consistent_steps(length):
    order = create_random_order(length)
    return partial(specific_sequence_transformer, order=order)


def root_and_consistent_steps(length):
    order = create_random_order(length - 1)
    return partial(specific_sequence_transformer, order=order, pop_first=True)


def consistent_strings(length):
    order = create_random_order(length)
    return partial(specific_sequence_transformer, order=order, index_multiplier=-1)


def root_and_consistent_strings(length):
    order = create_random_order(length - 1)
    return partial(specific_sequence_transformer, order=order, pop_first=True, index_multiplier=-1)


def create_random_order(length):
    return random.sample(range(length), length)


def specific_sequence_transformer(positions, sequence_length=None, order=None, pop_first=False, index_multiplier=1):
    if sequence_length is None:
        sequence_length = len(positions)

    if pop_first:
        first_note = [positions.pop(0)]
    else:
        first_note = []

    random_notes = get_shapes_in_specific_order(positions, order, index_multiplier)

    return resize_sequence(first_note + random_notes, sequence_length)


def get_shapes_in_specific_order(positions, order, index_multiplier):
    random_notes = []

    for index in order:
        try:
            note = positions[index * index_multiplier]
        except IndexError:
            note = positions[-1]

        random_notes.append(note)
    return random_notes
