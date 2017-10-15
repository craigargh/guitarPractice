from typing import List

from guitarPractice.exercise_builder.transformers.transformer_utils import resize_sequence
from guitarPractice.guitar_shapes.position import Position


def ascending(positions: List[Position], sequence_length: int = None):
    sequence = resize_sequence(positions, sequence_length)

    return sequence


def asc_and_desc(positions: List[Position], sequence_length: int = None):
    asc_length, desc_length = calculate_asc_desc_sequence_length(positions, sequence_length)

    ascending_sequence = positions[:asc_length]
    descending_sequence = list(reversed(positions[-desc_length:]))

    sequence = ascending_sequence + descending_sequence

    return resize_sequence(sequence, sequence_length)


def calculate_asc_desc_sequence_length(positions, sequence_length):
    if sequence_length:
        asc_length = int(sequence_length / 2)
        desc_length = asc_length

        is_even_split = sequence_length % 2 == 0

        if not is_even_split:
            desc_length += 1
    else:
        asc_length = int(((len(positions) * 2) - 2) / 2)
        desc_length = asc_length

    return asc_length, desc_length


def ascending_skip(positions: List[Position], sequence_length: int = None):
    first_note = [positions.pop(0)]

    if sequence_length:
        last_notes_length = sequence_length - 1
    else:
        last_notes_length = len(positions)

    if sequence_length and len(positions) > last_notes_length:
        last_notes = positions[-last_notes_length:]
    else:
        last_notes = resize_sequence(positions, last_notes_length)

    return first_note + last_notes


def asc_and_desc_skip(positions: List[Position], sequence_length: int = None):
    if not sequence_length or len(positions) <= sequence_length / 2:
        return asc_and_desc(positions, sequence_length)

    first_note = [positions.pop(0)]
    sequence = positions[:]

    half_sequence_length = sequence_length / 2

    if len(sequence) > int(half_sequence_length):
        last_notes_length = int(half_sequence_length)
        sequence = sequence[-last_notes_length:]

    last_notes = asc_and_desc(sequence, sequence_length - 1)

    return first_note + last_notes
