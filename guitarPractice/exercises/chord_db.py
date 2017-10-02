from guitarPractice.exercises.chord import Chord
from guitarPractice.exercises.position import Position


def get_major_scale_chords() -> iter:
    return [
        c_major(),
        d_minor(),
        e_minor(),
        f_major(),
        g_major()
    ]


def c_major():
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return Chord('C', 'Major', positions)


def d_minor():
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return Chord('D', 'Minor', positions)


def e_minor():
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1),
    ]

    return Chord('E', 'Minor', positions)


def f_major():
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1, is_highlighted=True),
    ]

    return Chord('F', 'Major', positions)


def g_major():
    positions = [
        Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=3, finger=3),
    ]

    return Chord('G', 'Major', positions)
