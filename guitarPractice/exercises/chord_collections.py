from guitarPractice.exercises import chord_shapes

"""
major scale nine chords
Cmaj9-Dm9-Em7b9-Fmaj9-G9-Am9-Bm7b9b5
"""


def get_major_scale_triad_chords() -> iter:
    return [
        chord_shapes.c_major(),
        chord_shapes.d_minor(),
        chord_shapes.e_minor(),
        chord_shapes.f_major(),
        chord_shapes.g_major(),
        chord_shapes.a_minor(),
        chord_shapes.b_diminished(),
    ]


def get_major_scale_seven_chords() -> iter:
    return [
        chord_shapes.c_major_seven(),
        chord_shapes.d_minor_seven(),
        chord_shapes.e_minor_seven(),
        chord_shapes.f_major_seven(),
        chord_shapes.g_seven(),
        chord_shapes.a_minor_seven(),
        chord_shapes.b_diminished_seven_flat_five(),
    ]
