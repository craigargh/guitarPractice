from typing import List

from guitarPractice.guitar_shapes.position import Position


def move_frets(positions: List[Position], min_fret):
    lowest_fret = min(position.fret for position in positions)
    offset = min_fret - lowest_fret

    for position in positions:
        position.fret += offset

    return positions


def spread_frets(positions: List[Position], spacing: int = 1):
    lowest_fret = min(position.fret for position in positions)

    for index, position in enumerate(positions):
        offset = (position.fret - lowest_fret) * spacing
        position.fret += offset

    return positions
