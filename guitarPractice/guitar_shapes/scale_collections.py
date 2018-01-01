from guitarPractice.guitar_shapes import major_scale_shapes, pentatonic_scale_shapes


def c_major_modes():
    return [
        major_scale_shapes.c_ionian(),
        major_scale_shapes.d_dorian(),
        major_scale_shapes.e_phrygian(),
        major_scale_shapes.f_lydian(),
        major_scale_shapes.g_mixolydian(),
        major_scale_shapes.a_aeolian(),
        major_scale_shapes.b_locrian(),
    ]


def c_major_pentatonic_modes():
    return [
        pentatonic_scale_shapes.c_major(),
        pentatonic_scale_shapes.d_dorian(),
        pentatonic_scale_shapes.e_phrygian(),
        pentatonic_scale_shapes.g_mixolydian(),
        pentatonic_scale_shapes.a_minor(),
    ]
