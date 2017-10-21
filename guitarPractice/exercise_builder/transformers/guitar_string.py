from typing import List

from guitarPractice.guitar_shapes.position import Position


def alternate_odd(positions: List[Position], max_string: int = 6):
    return alternate(positions, max_string, 1)


def alternate_even(positions: List[Position], max_string: int = 6):
    return alternate(positions, max_string, 0)


def alternate(positions: List[Position], max_string, alternate_value):
    highest_string = max(position.guitar_string for position in positions)

    if highest_string == max_string:
        for position in positions:
            position.guitar_string -= 1

    for index, position in enumerate(positions):
        if index % 2 == alternate_value:
            position.guitar_string += 1

    return positions
