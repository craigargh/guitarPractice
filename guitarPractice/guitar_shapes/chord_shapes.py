from guitarPractice.guitar_shapes.guitar_shape import GuitarShape

from guitarPractice.guitar_shapes.position import Position


def c_major() -> GuitarShape:
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return GuitarShape('C', 'Major', positions)


def c_major_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=3, finger=4),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return GuitarShape('C', 'Major 7', positions)


def c_major_add_9() -> GuitarShape:
    positions = [
        Position(guitar_string=5, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=1),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=3, finger=3),
        Position(guitar_string=1)
    ]

    return GuitarShape('C', 'Major add 9', positions)


def d_minor() -> GuitarShape:
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return GuitarShape('D', 'Minor', positions)


def d_minor_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return GuitarShape('D', 'Minor 7', positions)


def d_minor_add_9() -> GuitarShape:
    positions = [
        Position(guitar_string=4, fret=3, finger=2),
        Position(guitar_string=3, fret=2, finger=1),
        Position(guitar_string=2, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return GuitarShape('D', 'Minor add 9', positions)


def e_minor() -> GuitarShape:
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return GuitarShape('E', 'Minor', positions)


def e_minor_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return GuitarShape('E', 'Minor 7', positions)


def e_minor_flat_nine() -> GuitarShape:
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return GuitarShape('E', 'Minor flat 9', positions)


def f_major() -> GuitarShape:
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1, is_highlighted=True),
    ]

    return GuitarShape('F', 'Major', positions)


def f_major_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1),
    ]

    return GuitarShape('F', 'Major 7', positions)


def f_major_add_9() -> GuitarShape:
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=3, finger=4, is_highlighted=True),
    ]

    return GuitarShape('F', 'Major add 9', positions)


def g_major() -> GuitarShape:
    positions = [
        Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=3, finger=3, is_highlighted=True),
    ]

    return GuitarShape('G', 'Major', positions)


def g_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=6, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return GuitarShape('G', '7', positions)


def g_major_add_9() -> GuitarShape:
    positions = [
        Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=5),
        Position(guitar_string=4),
        Position(guitar_string=3, fret=2, finger=1),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=3, finger=4, is_highlighted=True),
    ]

    return GuitarShape('G', 'Major add 9', positions)


def a_minor() -> GuitarShape:
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return GuitarShape('A', 'Minor', positions)


def a_minor_seven() -> GuitarShape:
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return GuitarShape('A', 'Minor 7', positions)


def a_minor_add_9() -> GuitarShape:
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=4, finger=4),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return GuitarShape('A', 'Minor add 9', positions)


def b_diminished() -> GuitarShape:
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=4, finger=4, is_highlighted=True),
        Position(guitar_string=2, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return GuitarShape('B', 'Diminished', positions)


def b_minor_seven_flat_five() -> GuitarShape:
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return GuitarShape('B', 'Minor 7 Flat 5', positions)


def b_diminished_flat_9() -> GuitarShape:
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=4, finger=4, is_highlighted=True),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return GuitarShape('B', 'Diminished flat 9', positions)
