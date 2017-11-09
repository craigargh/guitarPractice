def get_notes_from_pick_pattern(positions, pick_pattern):
    notes = []

    for guitar_string in pick_pattern:
        if guitar_string == 'r':
            note = get_root_note(positions)
        elif guitar_string == 'a':
            note = get_alternate_root_note(positions)
        else:
            note = get_guitar_string_note(positions, guitar_string)

        notes.append(note)

    return notes


def get_guitar_string_note(positions, guitar_string):
    notes = [
        position
        for position in positions
        if position.guitar_string == guitar_string
    ]

    if len(notes) == 0:
        raise ValueError('String number not found in shape')

    return notes[0]


def get_root_note(positions):
    root_guitar_string = get_lowest_string(positions)
    return get_guitar_string_note(positions, root_guitar_string)


def get_alternate_root_note(positions):
    root_guitar_string = get_lowest_string(positions)

    alternate_root = None
    possible_strings = range(1, root_guitar_string)

    for possible_string in reversed(possible_strings):
        try:
            alternate_root = get_guitar_string_note(positions, possible_string)
            break
        except ValueError:
            pass

    if alternate_root is None:
        raise ValueError('Could not find alternate root note')

    return alternate_root


def get_lowest_string(positions):
    return max(
        position.guitar_string
        for position in positions
    )
