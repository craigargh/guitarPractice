from functools import partial
from random import sample, choice, randrange

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.higher_order_transformers import (
    make_consistent_order_random_transformer,
    make_root_consistent_order_random_transformer,
    make_root_consistent_string_random_transformer,
    make_consistent_string_random_transformer
)
from guitarPractice.exercise_builder.pick_order_transformers import (
    ascending_transformer,
    ascending_and_descending_transformer,
    ascending_skip_transformer, ascending_and_descending_skip_transformer
)
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords, c_major_scale_seven_chords


def level_one():
    chords = get_level_one_chords(2)
    transformer = get_level_one_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    return exercise


def level_two():
    version = randrange(2)
    if version == 1:
        chords = get_level_one_chords(2)
        transformer = get_randomised_transformer()
    else:
        chords = get_level_two_chords(4)
        transformer = get_level_two_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    return exercise


def get_level_one_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)


def get_level_two_chords(quantity):
    all_chords = c_major_scale_triad_chords() + c_major_scale_seven_chords()
    return sample(all_chords, quantity)


def get_level_one_transformer():
    all_transformers = [
        ascending_transformer,
        ascending_and_descending_transformer
    ]

    transformer = choice(all_transformers)

    notes_per_arpeggio = choice([4, 6, 8])

    return partial(transformer, sequence_length=notes_per_arpeggio)


def get_level_two_transformer():
    all_transformers = [
        ascending_transformer,
        ascending_and_descending_transformer,
        ascending_skip_transformer,
        ascending_and_descending_skip_transformer
    ]

    transformer = choice(all_transformers)

    notes_per_arpeggio = choice([4, 6, 8])

    return partial(transformer, sequence_length=notes_per_arpeggio)


def get_randomised_transformer():
    notes_per_arpeggio = choice([4, 6])

    all_transformers = [
        make_consistent_order_random_transformer(notes_per_arpeggio),
        make_root_consistent_order_random_transformer(notes_per_arpeggio),
        make_consistent_string_random_transformer(notes_per_arpeggio),
        make_root_consistent_string_random_transformer(notes_per_arpeggio),
    ]

    transformer = choice(all_transformers)

    return partial(transformer, sequence_length=notes_per_arpeggio)
