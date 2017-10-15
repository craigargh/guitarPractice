import random

from guitarPractice.exercise_builder.transformer_utils import resize_sequence


def make_consistent_order_random_transformer(length):
    order = random.sample(range(length), length)

    def specific_sequence_transformer(positions, sequence_length=None):
        if sequence_length is None:
            sequence_length = len(positions)

        notes = []

        for index in order:
            try:
                note = positions[index]
            except IndexError:
                note = positions[-1]

            notes.append(note)

        return resize_sequence(notes, sequence_length)

    return specific_sequence_transformer


def make_root_consistent_order_random_transformer(length):
    order = random.sample(range(length - 1), length - 1)

    def specific_sequence_transformer(positions, sequence_length=None):
        if sequence_length is None:
            sequence_length = len(positions)

        first_note = [positions.pop(0)]
        random_notes = []

        for index in order:
            try:
                note = positions[index]
            except IndexError:
                note = positions[-1]

            random_notes.append(note)

        return resize_sequence(first_note + random_notes, sequence_length)

    return specific_sequence_transformer


def make_consistent_string_random_transformer(length):
    order = random.sample(range(length), length)

    def specific_sequence_transformer(positions, sequence_length=None):
        if sequence_length is None:
            sequence_length = len(positions)

        notes = []

        for index in order:
            try:
                note = positions[-index]
            except IndexError:
                note = positions[-1]

            notes.append(note)

        return resize_sequence(notes, sequence_length)

    return specific_sequence_transformer


def make_root_consistent_string_random_transformer(length):
    order = random.sample(range(length - 1), length - 1)

    def specific_sequence_transformer(positions, sequence_length=None):
        if sequence_length is None:
            sequence_length = len(positions)

        first_note = [positions.pop(0)]
        random_notes = []

        for index in order:
            try:
                note = positions[-index]
            except IndexError:
                note = positions[-1]

            random_notes.append(note)

        return resize_sequence(first_note + random_notes, sequence_length)

    return specific_sequence_transformer
