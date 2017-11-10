from functools import partial
from random import sample, choice, randrange

from guitarPractice.exercise_builder.transformers import order
from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.transformers import random_order
from guitarPractice.exercise_builder.transformers.pick_pattern import get_notes_from_pick_pattern
from guitarPractice.exercises.exercise_utils import choose_transformer
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords, c_major_scale_seven_chords
from guitarPractice.guitar_shapes.pick_patterns import pick_pattern_collection_one


def level_one():
    chords = get_level_one_chords(2)
    transformer = get_level_one_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    return exercise


def get_level_one_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)


def get_level_one_transformer():
    all_transformers = [
        order.ascending,
        order.asc_and_desc,
        order.ascending_skip,
        order.asc_and_desc_skip
    ]

    notes_per_arpeggio = choice([4, 6, 8])

    return choose_transformer(all_transformers, notes_per_arpeggio)


def level_two():
    version = randrange(2)
    if version == 1:
        chords = get_level_two_chords(2)
        transformer = get_pick_pattern()
    else:
        chords = get_level_two_chords(4)
        transformer = get_level_one_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    return exercise


def get_level_two_chords(quantity):
    all_chords = c_major_scale_triad_chords() + c_major_scale_seven_chords()
    return sample(all_chords, quantity)


def get_pick_pattern():
    patterns = pick_pattern_collection_one()
    pattern = choice(patterns)

    return partial(get_notes_from_pick_pattern, pick_pattern=pattern)
