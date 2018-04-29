from itertools import cycle
from random import choice


def random_choices(beats, rhythms, sequence_length):
    rhythm_cycle = cycle(
        rhythm
        for _ in range(beats)
        for rhythm in choice(rhythms)
    )

    chosen_rhythm = [
        next(rhythm_cycle)
        for _ in range(sequence_length)
    ]

    return chosen_rhythm
