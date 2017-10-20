from random import sample

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.guitar_shapes.chromatic_collections import chromatic_collection_one


def level_one():
    shapes = sample(chromatic_collection_one(), 1)

    exercise = ExerciseBuilder() \
        .set_shapes(shapes) \
        .build()

    # apply one transformer
    # shift shape up/down fretboard with transformer within fret 1-16

    return exercise
