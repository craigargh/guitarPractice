def get_notes_from_pick_pattern(guitar_shape, pick_pattern):
    notes = []

    for guitar_string in pick_pattern:
        if guitar_string == 'r':
            note = get_root_note(guitar_shape)
        elif guitar_string == 'a':
            note = get_alternate_root_note(guitar_shape)
        else:
            note = get_guitar_string_note(guitar_shape, guitar_string)

        notes.append(note)

    return notes


def get_guitar_string_note(guitar_shape, guitar_string):
    positions = [
        position
        for position in guitar_shape.positions
        if position.guitar_string == guitar_string
    ]

    if len(positions) == 0:
        raise ValueError('String number not found in shape')

    return positions[0]


def get_root_note(guitar_shape):
    root_guitar_string = get_lowest_string(guitar_shape)
    return get_guitar_string_note(guitar_shape, root_guitar_string)


def get_alternate_root_note(guitar_shape):
    root_guitar_string = get_lowest_string(guitar_shape)

    alternate_root = None
    possible_strings = range(1, root_guitar_string)

    for possible_string in reversed(possible_strings):
        try:
            alternate_root = get_guitar_string_note(guitar_shape, possible_string)
            break
        except ValueError:
            pass

    if alternate_root is None:
        raise ValueError('Could not find alternate root note')

    return alternate_root


def get_lowest_string(guitar_shape):
    return max(
        position.guitar_string
        for position in guitar_shape.positions
    )
