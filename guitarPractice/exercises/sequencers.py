def in_order_sequencer(*shapes):
    return [
        note
        for shape in shapes
        for note in shape
    ]


def repeat_first_shape_sequencer(*shapes):
    shapes_list = list(shapes)
    first_shape = shapes_list.pop(0)

    sequence = []

    for shape in shapes_list:
        sequence.extend(first_shape)
        sequence.extend(shape)

    return sequence
