from random import choice


def random_choices(beats, rhythms):
    chosen_rhythm = [
        rhythm
        for _ in range(beats)
        for rhythm in choice(rhythms)
    ]

    return chosen_rhythm
