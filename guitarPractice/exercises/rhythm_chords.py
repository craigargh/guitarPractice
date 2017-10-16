from functools import partial
from random import sample

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.sequencers import repeat_shapes
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords


def level_one():
    shapes = get_level_one_chords(2)

    for shape in shapes:
        shape.is_strummed = True

    repeater = partial(repeat_shapes, times=4)

    exercise = ExerciseBuilder() \
        .set_sequencer(repeater) \
        .set_shapes(shapes) \
        .build()

    print(exercise)

    return exercise


def get_level_one_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)
