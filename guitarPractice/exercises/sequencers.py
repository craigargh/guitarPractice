from typing import List

from guitarPractice.exercises.guitar_shape import GuitarShape


def in_order_sequencer(*shapes: List[GuitarShape]) -> List[GuitarShape]:
    return list(shapes)


def repeat_first_shape_sequencer(*shapes) -> List[GuitarShape]:
    shapes_list = list(shapes)
    first_shape = shapes_list.pop(0)

    sequence = []

    for shape in shapes_list:
        sequence.append(first_shape)
        sequence.append(shape)

    return sequence
