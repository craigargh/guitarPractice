from itertools import cycle


class Beat:
    def __init__(self, duration, note_subdivision):
        self.duration = duration
        self.note_subdivision = note_subdivision


def set_rhythm(positions, rhythm):
    rhythm_cycle = cycle(rhythm)

    for position, beat in zip(positions, rhythm_cycle):
        position.duration = beat.duration
        position.note_subdivision = beat.note_subdivision

    return positions
