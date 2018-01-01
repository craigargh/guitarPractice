def resize_sequence(positions, sequence_length):
    sequence_length_is_set = sequence_length is not None and sequence_length > 0

    if sequence_length_is_set and sequence_length < len(positions):
        positions = shorten_positions(positions, sequence_length)

    elif sequence_length_is_set and sequence_length > len(positions):
        positions = lengthen_sequence(positions, sequence_length)

    return positions


def shorten_positions(positions, sequence_length):
    return positions[:sequence_length]


def lengthen_sequence(positions, sequence_length):
    full_sequence_repeats = repeat_full_sequence(positions, sequence_length)
    partial_sequence_repeats = repeat_partial_sequence_to_end(positions, sequence_length)

    return full_sequence_repeats + partial_sequence_repeats


def repeat_full_sequence(positions, sequence_length):
    full_repeats_count = sequence_length // len(positions)
    return positions * full_repeats_count


def repeat_partial_sequence_to_end(positions, sequence_length):
    partial_repeats_length = sequence_length % len(positions)

    if partial_repeats_length != 0:
        return positions[-partial_repeats_length:]
    else:
        return []
