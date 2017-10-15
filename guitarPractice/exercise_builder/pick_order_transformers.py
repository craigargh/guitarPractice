from typing import List

from guitarPractice.exercise_builder.transformer_utils import resize_sequence
from guitarPractice.guitar_shapes.position import Position


def ascending_transformer(positions: List[Position], sequence_length: int = None):
    sequence = resize_sequence(positions, sequence_length)

    return sequence


def ascending_and_descending_transformer(positions: List[Position], sequence_length: int = None):
    if sequence_length:
        half_sequence_length = int(sequence_length / 2)
    else:
        half_sequence_length = int(((len(positions) * 2) - 2) / 2)

    sequence_part_1 = positions[:half_sequence_length]
    sequence_part_2 = list(reversed(positions[-half_sequence_length:]))

    sequence = sequence_part_1 + sequence_part_2

    return resize_sequence(sequence, sequence_length)


def ascending_skip_transformer(positions: List[Position], sequence_length: int = None):
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
