from typing import List

from guitarPractice.exercises.chord import Chord
from guitarPractice.exercises.position import Position


def in_order_sequencer(*shapes: List[Chord]) -> List[Position]:
    sequence = [
        position
        for shape in shapes
        for position in shape
    ]
    return sequence


def repeat_first_shape_sequencer(*shapes) -> List[Position]:
    shapes_list = list(shapes)
    first_shape = shapes_list.pop(0)

    sequence = []

    for shape in shapes_list:
        sequence.extend(first_shape)
        sequence.extend(shape)

    return sequence

# TODO: Add label/annotation to first position when chord is changed
