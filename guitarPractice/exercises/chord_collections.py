from guitarPractice.exercises.chord import Chord
from guitarPractice.exercises.position import Position

"""
major scale nine chords
Cmaj9-Dm9-Em7b9-Fmaj9-G9-Am9-Bm7b9b5
"""


def get_major_scale_triad_chords() -> iter:
    return [
        c_major(),
        d_minor(),
        e_minor(),
        f_major(),
        g_major(),
        a_minor(),
        b_diminished(),
    ]


def get_major_scale_seven_chords() -> iter:
    return [
        c_major_seven(),
        d_minor_seven(),
        e_minor_seven(),
        f_major_seven(),
        g_seven(),
        a_minor_seven(),
        b_diminished_seven_flat_five()
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


def c_major_seven():
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=3, finger=4),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return Chord('C', 'Major 7', positions)


def d_minor():
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return Chord('D', 'Minor', positions)


def d_minor_seven():
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return Chord('D', 'Minor 7', positions)


def e_minor():
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return Chord('E', 'Minor', positions)


def e_minor_seven():
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return Chord('E', 'Minor 7', positions)


def f_major():
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1, is_highlighted=True),
    ]

    return Chord('F', 'Major', positions)


def f_major_seven():
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1),
    ]

    return Chord('F', 'Major', positions)


def g_major():
    positions = [
        Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=3, finger=3, is_highlighted=True),
    ]

    return Chord('G', 'Major', positions)


def g_seven():
    positions = [
        Position(guitar_string=6, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return Chord('G', '7', positions)


def a_minor():
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return Chord('A', 'Minor', positions)


def a_minor_seven():
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return Chord('A', 'Minor 7', positions)


def b_diminished():
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=4, finger=4, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=2, fret=1, finger=1),
    ]

    return Chord('B', 'Diminished', positions)


def b_diminished_seven_flat_five():
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=2, finger=2, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=2, fret=1, finger=1),
    ]

    return Chord('B', 'Diminished', positions)
