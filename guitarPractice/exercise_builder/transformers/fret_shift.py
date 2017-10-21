from typing import List

from guitarPractice.guitar_shapes.position import Position


def move_frets(positions: List[Position], min_fret):
    lowest_fret = min(position.fret for position in positions)
    offset = min_fret - lowest_fret

    for position in positions:
        position.fret = position.fret + offset

    return positions
