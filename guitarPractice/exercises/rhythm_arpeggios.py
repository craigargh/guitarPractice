from functools import partial
from random import sample, choice

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.pick_order_transformers import ascending_transformer, \
    ascending_and_descending_transformer
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords


def level_one():
    chords = get_chords(2)
    transformer = get_level_one_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    return exercise


def get_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)


def get_level_one_transformer():
    all_transformers = [
        ascending_transformer
        ascending_and_descending_transformer,
    ]

    transformer = choice(all_transformers)

    notes_per_arpeggio = choice([4, 6, 8])
    return partial(transformer, sequence_length=notes_per_arpeggio)
