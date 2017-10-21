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


def spread_left(positions: List[Position], max_string: int = 6):
    return spread(positions, max_string, 1)


def spread_right(positions: List[Position], max_string: int = 6):
    return spread(positions, max_string, -1)


def spread(positions, max_string, start_direction):
    direction = start_direction
    index = positions[0].guitar_string

    for position in positions:
        position.guitar_string = index

        if index >= max_string:
            direction = -1
        if index == 1:
            index = 1
            direction = 1

        index += direction

    return positions
