from functools import partial

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.exercise_builder.transformers.rhythm import random_rhythm_factory, Beat, set_rhythm
from guitarPractice.exercise_builder.transformers.transformer_utils import resize_sequence
from guitarPractice.guitar_shapes.guitar_shape import GuitarShape
from guitarPractice.guitar_shapes.position import Position


def level_one():
    positions = [
        Position(guitar_string=6, fret=5, finger=1)
        for _ in range(16)
    ]

    shapes = [
        GuitarShape('', '', positions)
    ]

    rhythm = make_rhythm_transformer()
    sequence_length = len(rhythm) * 2

    rhythm_transformer = partial(set_rhythm, rhythm=rhythm)
    length_transformer = partial(resize_sequence, sequence_length=sequence_length)

    exercise = ExerciseBuilder() \
        .set_shapes(shapes) \
        .transform(rhythm_transformer) \
        .transform(length_transformer) \
        .build()

    return exercise


def make_rhythm_transformer():
    beats = [
        [
            Beat(1, 1)
        ],
        [
            Beat(1, 2),
            Beat(1, 2)
        ]
    ]

    return random_rhythm_factory(4, beats)
