class Exercise:
    def __init__(self, shapes, sequence, rhythm=None):
        if not rhythm:
            rhythm = make_default_rhythm(sequence)

        self.shapes = shapes
        self.sequence = sequence
        self.rhythm = rhythm

    def __str__(self):
        sorted_sequence = sorted(self.sequence, key=lambda x: x.order)

        unique_order_indexes = set(position.order for position in sorted_sequence)

        tab_list = []
        for guitar_string in range(1, 7):
            guitar_string_tab = []

            for beat in range(len(unique_order_indexes)):
                tab_value = make_beat_tab(sorted_sequence, beat, guitar_string)
                guitar_string_tab.append(tab_value)

            tab_list.append("".join(guitar_string_tab))

        return "\n".join(tab_list)


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

    return [
        {'duration': 1, 'division': 8}
        for _ in beats
    ]
