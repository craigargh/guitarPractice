from guitarPractice.exercises.chord import Chord
from guitarPractice.exercises.position import Position


def get_major_scale_chords() -> iter:
    return [
        c_major(),
        d_minor(),
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
