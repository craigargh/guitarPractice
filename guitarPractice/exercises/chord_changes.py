from functools import partial
from random import sample, choice

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.sequencers import repeat_shapes, repeat_first_shape_sequencer
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords, c_major_scale_seven_chords, \
    c_major_scale_add_9_chords


def level_one():
    shapes = get_level_one_chords(2)

    for shape in shapes:
        shape.is_strummed = True

    repeater = partial(repeat_shapes, times=4)

    exercise = ExerciseBuilder() \
        .set_sequencer(repeater) \
        .set_shapes(shapes) \
        .build()

    return exercise


def get_level_one_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)


def level_two():
    variation = choice([level_two_variation_1, level_two_variation_2])

    return variation()


def level_two_variation_1():
    chords = get_level_two_chords(3)

    for chord in chords:
        chord.is_strummed = True

    repeater = partial(repeat_shapes, times=4)

    return ExerciseBuilder() \
        .set_shapes(chords) \
        .set_sequencer(repeat_first_shape_sequencer) \
        .set_sequencer(repeater) \
        .build()


def level_two_variation_2():
    chords = get_level_two_chords(4)

    for chord in chords:
        chord.is_strummed = True

    repeater = partial(repeat_shapes, times=4)

    return ExerciseBuilder() \
        .set_shapes(chords) \
        .set_sequencer(repeater) \
        .build()


def get_level_two_chords(quantity):
    all_chords = c_major_scale_triad_chords() + \
                 c_major_scale_seven_chords() + \
                 c_major_scale_add_9_chords()

    return sample(all_chords, quantity)
