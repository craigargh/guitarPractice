from functools import partial
import random

from guitarPractice.exercise_builder.exercise_builder import ExerciseBuilder
from guitarPractice.guitar_shapes.chromatic_collections import chromatic_collection_one
from guitarPractice.exercise_builder.transformers import guitar_string, fret, order, random_order


def level_one():
    shapes = random.sample(chromatic_collection_one(), 1)

    transformers = [
        guitar_string.alternate_even,
        guitar_string.alternate_odd,
        guitar_string.spread_left,
        guitar_string.spread_right,
        fret.spread_frets,
        order.asc_and_desc,
        order.repeat_first,
        random_order.make_consistent_steps(4),
        random_order.make_root_and_consistent_steps(4)
    ]

    order_transformer = random.choice([order.ascending, order.descending])
    transformer = random.choice(transformers)

    min_fret = random.randrange(3, 11)
    fret_shifter = partial(fret.move_frets, min_fret=min_fret)

    exercise = ExerciseBuilder() \
        .set_shapes(shapes) \
        .transform(order_transformer) \
        .transform(transformer) \
        .transform(fret_shifter) \
        .build()

    return exercise
