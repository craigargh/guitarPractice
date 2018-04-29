from guitarPractice.exercise_builder.transformers.pick_pattern import ROOT, ALTERNATE_ROOT

r = ROOT
a = ALTERNATE_ROOT


def pick_pattern_collection_one():
    return [
        [r, 1, 2, 1, 2, 1, 2, 1],
        [r, 3, 2, 1, r, 3, 2, 1],
        [r, 3, 1, 2, r, 3, 1, 2],
        [r, 2, 1, 3, r, 2, 1, 3],
        [r, 2, 3, 1, r, 2, 3, 1],
        [r, 1, 2, 3, r, 1, 2, 3],
        [r, 1, 3, 2, r, 1, 3, 2],
    ]


def pick_pattern_collection_two():
    return [
        [r, 2, 1, 3, a, 2, 1, 3],
        [r, 3, 2, 1, a, 3, 2, 1],
        [r, 1, 2, 3, a, 1, 2, 3],
        [r, 2, 3, 1, a, 2, 3, 1],
        [r, 1, 3, 2, a, 1, 3, 2],
        [r, 1, a, 2, r, 1, a, 2],
        [r, 1, 2, 1, a, 1, 2, 1],
        [r, 2, a, 1, r, 2, a, 1],
    ]
