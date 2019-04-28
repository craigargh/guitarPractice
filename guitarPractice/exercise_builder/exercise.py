class Exercise:
    def __init__(self, shapes, sequence, rhythm=None):
        if not rhythm:
            rhythm = make_default_rhythm(sequence)

        self.shapes = shapes
        self.sequence = sequence
        self.rhythm = rhythm


def make_default_rhythm(sequence):
    beats = {
        item.order
        for item in sequence
    }

    is_even_beats = len(beats) % 2 == 0

    if is_even_beats:
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
