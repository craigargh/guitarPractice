from functools import partial
from random import sample, choice

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.pick_order_transformers import ascending_transformer
from guitarPractice.guitar_shapes.chord_collections import c_major_scale_triad_chords


def level_one():
    chords = get_chords(2)
    transformer = get_level_one_transformer()

    exercise = ExerciseBuilder() \
        .set_shapes(chords) \
        .transform(transformer) \
        .build()

    print(exercise)


def get_chords(quantity):
    all_chords = c_major_scale_triad_chords()
    return sample(all_chords, quantity)


def get_level_one_transformer():
    notes_per_arpeggio = choice([4, 6, 8, 12])

    print(notes_per_arpeggio)

    all_transformers = [
        partial(ascending_transformer, sequence_length=notes_per_arpeggio)
    ]

    return choice(all_transformers)


level_one()
