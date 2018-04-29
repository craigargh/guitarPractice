from functools import partial
from random import choice

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.rhythms import random_choices
from guitarPractice.guitar_shapes.scale_collections import c_major_modes, c_major_pentatonic_modes


def level_one():
    selected_modes = [choice(c_major_pentatonic_modes())]

    rhythms = [
        [
            {'duration': 1, 'division': 4}
        ],
        [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8},
        ],
    ]

    rhythm_generator = partial(random_choices, beats=4, rhythms=rhythms)

    exercise = ExerciseBuilder() \
        .set_shapes(selected_modes) \
        .set_rhythm(rhythm_generator) \
        .build()

    return exercise


def level_two():
    variations = [
        level_two_variation_one,
        level_two_variation_two,
    ]

    exercise_function = choice(variations)

    return exercise_function()


def level_two_variation_one():
    selected_modes = [choice(c_major_modes())]

    rhythms = [
        [
            {'duration': 1, 'division': 4}
        ],
        [
            {'duration': 1, 'division': 8},
            {'duration': 1, 'division': 8}
        ],
    ]

    rhythm_generator = partial(random_choices, beats=4, rhythms=rhythms)

    exercise = ExerciseBuilder() \
        .set_shapes(selected_modes) \
        .set_rhythm(rhythm_generator) \
        .build()

    return exercise


def level_two_variation_two():
    selected_modes = [choice(c_major_pentatonic_modes())]

    rhythms = [
        [
            {'duration': 1, 'division': 4}
        ],
        [
            {'duration': 1, 'division': 16},
            {'duration': 1, 'division': 16},
            {'duration': 1, 'division': 16},
            {'duration': 1, 'division': 16},
        ],
    ]

    rhythm_generator = partial(random_choices, beats=4, rhythms=rhythms)

    exercise = ExerciseBuilder() \
        .set_shapes(selected_modes) \
        .set_rhythm(rhythm_generator) \
        .build()

    return exercise
