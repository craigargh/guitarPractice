from functools import partial
from random import sample, choice

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.transformers.order import ascending
from guitarPractice.guitar_shapes.scale_collections import c_major_modes


def level_one():
    variations = [
        level_one_variation_one,
        level_one_variation_two
    ]

    exercise_function = choice(variations)

    return exercise_function()


def level_one_variation_one():
    selected_modes = get_c_major_modes(1)

    exercise = ExerciseBuilder() \
        .set_shapes(selected_modes) \
        .build()

    return exercise


def level_one_variation_two():
    selected_modes = get_c_major_modes(2)

    restrict_length = partial(ascending, sequence_length=8)

    exercise = ExerciseBuilder() \
        .set_shapes(selected_modes) \
        .transform(restrict_length) \
        .build()

    return exercise


def get_c_major_modes(quantity):
    modes = c_major_modes()
    return sample(modes, quantity)
