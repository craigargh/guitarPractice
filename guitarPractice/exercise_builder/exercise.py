class Exercise:
    def __init__(self, shapes, sequence, rhythm=None):
        if not rhythm:
            rhythm = make_default_rhythm(sequence)

        self.shapes = shapes
        self.sequence = sequence
        self.rhythm = rhythm


def make_beat_tab(sequence, beat, guitar_string):
    found_value = "--"
    for item in sequence:
        if item.order == beat and item.guitar_string == guitar_string:
            found_value = f"{item.fret}-"

    return found_value


def make_default_rhythm(sequence):
    beats = {
        item.order
        for item in sequence
    }

    if len(beats) % 2 == 0:
        length = len(beats)
        last_beat = []
    else:
        length = len(beats) - 1
        last_beat = [{'duration': 1, 'division': 4}]

    eighth_beats = [
        {'duration': 1, 'division': 8}
        for _ in range(length)
    ]

    return eighth_beats + last_beat
