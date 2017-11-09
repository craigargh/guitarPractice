def get_guitar_string_note(guitar_shape, guitar_string):
    positions = [
        position
        for position in guitar_shape.positions
        if position.guitar_string == guitar_string
    ]

    if len(positions) == 0:
        raise ValueError('String number not found in shape')

    return positions[0]
