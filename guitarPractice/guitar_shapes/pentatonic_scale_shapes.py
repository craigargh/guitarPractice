from guitarPractice.guitar_shapes.position import Position
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape


def c_major():
    positions = [
        Position(guitar_string=6, fret=8, finger=2),
        Position(guitar_string=6, fret=10, finger=4),
        Position(guitar_string=5, fret=7, finger=1),
        Position(guitar_string=5, fret=10, finger=4),
        Position(guitar_string=4, fret=7, finger=1),
        Position(guitar_string=4, fret=10, finger=4),
        Position(guitar_string=3, fret=7, finger=1),
        Position(guitar_string=3, fret=9, finger=3),
        Position(guitar_string=2, fret=8, finger=2),
        Position(guitar_string=2, fret=10, finger=4),
        Position(guitar_string=1, fret=8, finger=2),
    ]

    return GuitarShape('C', 'Major Pentatonic', positions)


def d_dorian():
    positions = [
        Position(guitar_string=6, fret=10, finger=1),
        Position(guitar_string=6, fret=12, finger=3),
        Position(guitar_string=5, fret=10, finger=1),
        Position(guitar_string=5, fret=12, finger=3),
        Position(guitar_string=4, fret=10, finger=1),
        Position(guitar_string=4, fret=12, finger=3),
        Position(guitar_string=3, fret=9, finger=1),
        Position(guitar_string=3, fret=12, finger=3),
        Position(guitar_string=2, fret=10, finger=1),
        Position(guitar_string=2, fret=13, finger=4),
        Position(guitar_string=1, fret=10, finger=1),
    ]

    return GuitarShape('D', 'Dorian Pentatonic', positions)


def e_phrygian():
    positions = [
        Position(guitar_string=6, fret=12, finger=1),
        Position(guitar_string=6, fret=15, finger=4),
        Position(guitar_string=5, fret=12, finger=1),
        Position(guitar_string=5, fret=15, finger=4),
        Position(guitar_string=4, fret=12, finger=1),
        Position(guitar_string=4, fret=14, finger=3),
        Position(guitar_string=3, fret=12, finger=1),
        Position(guitar_string=3, fret=14, finger=3),
        Position(guitar_string=2, fret=13, finger=2),
        Position(guitar_string=2, fret=15, finger=4),
        Position(guitar_string=1, fret=12, finger=1),
    ]

    return GuitarShape('E', 'Phrygian Pentatonic', positions)


def g_mixolydian():
    positions = [
        Position(guitar_string=6, fret=3, finger=2),
        Position(guitar_string=6, fret=5, finger=4),
        Position(guitar_string=5, fret=3, finger=2),
        Position(guitar_string=5, fret=5, finger=4),
        Position(guitar_string=4, fret=2, finger=1),
        Position(guitar_string=4, fret=5, finger=4),
        Position(guitar_string=3, fret=2, finger=1),
        Position(guitar_string=3, fret=5, finger=4),
        Position(guitar_string=2, fret=3, finger=2),
        Position(guitar_string=2, fret=5, finger=4),
        Position(guitar_string=1, fret=3, finger=2),
    ]

    return GuitarShape('G', 'Mixolydian Pentatonic', positions)


def a_minor():
    positions = [
        Position(guitar_string=6, fret=5, finger=1),
        Position(guitar_string=6, fret=8, finger=4),
        Position(guitar_string=5, fret=5, finger=1),
        Position(guitar_string=5, fret=7, finger=3),
        Position(guitar_string=4, fret=5, finger=1),
        Position(guitar_string=4, fret=7, finger=3),
        Position(guitar_string=3, fret=5, finger=1),
        Position(guitar_string=3, fret=7, finger=3),
        Position(guitar_string=2, fret=5, finger=1),
        Position(guitar_string=2, fret=8, finger=4),
        Position(guitar_string=1, fret=5, finger=1),
    ]

    return GuitarShape('A', 'Minor Pentatonic', positions)
