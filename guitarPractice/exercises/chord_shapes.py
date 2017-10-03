from guitarPractice.exercises.chord import Chord
from guitarPractice.exercises.position import Position


def c_major() -> Chord:
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return Chord('C', 'Major', positions)


def c_major_seven() -> Chord:
    positions = [
        Position(guitar_string=5, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=3, finger=4),
        Position(guitar_string=2, fret=1, finger=1, is_highlighted=True),
        Position(guitar_string=1)
    ]

    return Chord('C', 'Major 7', positions)


def d_minor() -> Chord:
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return Chord('D', 'Minor', positions)


def d_minor_seven() -> Chord:
    positions = [
        Position(guitar_string=4, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1)
    ]

    return Chord('D', 'Minor 7', positions)


def e_minor() -> Chord:
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return Chord('E', 'Minor', positions)


def e_minor_seven() -> Chord:
    positions = [
        Position(guitar_string=6, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3),
        Position(guitar_string=2),
        Position(guitar_string=1, is_highlighted=True),
    ]

    return Chord('E', 'Minor 7', positions)


def f_major() -> Chord:
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, fret=1, finger=1, is_highlighted=True),
    ]

    return Chord('F', 'Major', positions)


def f_major_seven() -> Chord:
    positions = [
        Position(guitar_string=4, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=3, fret=2, finger=2),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1),
    ]

    return Chord('F', 'Major', positions)


def g_major() -> Chord:
    positions = [
        Position(guitar_string=6, fret=3, finger=2, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=1),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=3, finger=3, is_highlighted=True),
    ]

    return Chord('G', 'Major', positions)


def g_seven() -> Chord:
    positions = [
        Position(guitar_string=6, fret=3, finger=3, is_highlighted=True),
        Position(guitar_string=5, fret=2, finger=2),
        Position(guitar_string=4),
        Position(guitar_string=3, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=1, fret=1, finger=1),
    ]

    return Chord('G', '7', positions)


def a_minor() -> Chord:
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3, fret=2, finger=3, is_highlighted=True),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return Chord('A', 'Minor', positions)


def a_minor_seven() -> Chord:
    positions = [
        Position(guitar_string=5, is_highlighted=True),
        Position(guitar_string=4, fret=2, finger=2),
        Position(guitar_string=3),
        Position(guitar_string=2, fret=1, finger=1),
        Position(guitar_string=1, is_highlighted=True)
    ]

    return Chord('A', 'Minor 7', positions)


def b_diminished() -> Chord:
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=4, finger=4, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=2, fret=1, finger=1),
    ]

    return Chord('B', 'Diminished', positions)


def b_diminished_seven_flat_five() -> Chord:
    positions = [
        Position(guitar_string=4),
        Position(guitar_string=3, fret=2, finger=2, is_highlighted=True),
        Position(guitar_string=2),
        Position(guitar_string=2, fret=1, finger=1),
    ]

    return Chord('B', 'Diminished', positions)
