from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


def make_chromatic_shape(*, root_note="", guitar_string=1, start_fret=1, quantity=1):
    positions = []

    for index in range(quantity):
        fret = start_fret + index
        finger = (index % 4) + 1

        position = Position(guitar_string=guitar_string, fret=fret, finger=finger)
        positions.append(position)

    return GuitarShape(root_note=root_note, tonality="Chromatic", positions=positions)


def chromatic_collection_one():
    return [
        make_chromatic_shape(quantity=4, guitar_string=6),
        make_chromatic_shape(quantity=4, guitar_string=5),
        make_chromatic_shape(quantity=4, guitar_string=4),
        make_chromatic_shape(quantity=4, guitar_string=3),
        make_chromatic_shape(quantity=4, guitar_string=2),
        make_chromatic_shape(quantity=4, guitar_string=1),
    ]
