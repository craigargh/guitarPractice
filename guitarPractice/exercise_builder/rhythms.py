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

    return round_rhythm(chosen_rhythm)


def round_rhythm(rhythms):
    rhythms = rhythms[:]

    excess_beats = calculate_remiander(rhythms)
    is_odd_rhythm = excess_beats != 0

    if is_odd_rhythm:
        excess_rhythm = collect_excess_beats(excess_beats, rhythms)
        round_rhythms = round_excess(excess_beats, excess_rhythm)

        rhythms[-len(round_rhythms):] = round_rhythms

    return rhythms


def collect_excess_beats(excess_size, rhythms):
    backwards = reversed(rhythms)

    rhythm_sum = 0

    excess_rhythm = []

    while rhythm_sum < excess_size:
        rhythm = next(backwards)
        rhythm_sum += calculate_size(rhythm)

        excess_rhythm.append(rhythm)

    return list(reversed(excess_rhythm))


def round_excess(excess_size, rhythms):
    rhythms = list(reversed(rhythms))

    remainder = excess_size

    while remainder != 0:
        for rhythm in rhythms:
            size = calculate_size(rhythm)

            if size == remainder:
                rhythm['division'] = int(rhythm['division'] / 2)
                break

            elif size * 2 <= remainder:
                rhythm['division'] = int(rhythm['division'] / 2)
                break

        remainder = calculate_remiander(rhythms)

    return list(reversed(rhythms))


def calculate_size(rhythm):
    return rhythm['duration'] / rhythm['division'] * 4


def calculate_remiander(rhythms):
    total_length = sum(
        calculate_size(rhythm)
        for rhythm in rhythms
    )

    return total_length % 1
