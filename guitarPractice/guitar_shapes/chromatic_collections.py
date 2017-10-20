from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


def make_chromatic_shape(*, root_note="", guitar_string=1, start_fret=0, quantity=1):
    positions = [
        Position(
            guitar_string=guitar_string,
            fret=start_fret + index,
            finger=(index % 4) + 1
        )
        for index in range(quantity)
    ]

    return GuitarShape(root_note="", tonality="", positions=positions)

