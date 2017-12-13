from guitarPractice.exercise_builder.transformers.pick_pattern import ROOT, ALTERNATE_ROOT

r = ROOT
a = ALTERNATE_ROOT

pattern_one = [r, 1, 2, 1, 2, 1, 2, 1]
pattern_two = [r, 3, 2, 1, r, 3, 2, 1]
pattern_three = [r, 3, 1, 2, r, 3, 1, 2]
pattern_four = [r, 2, 1, 3, r, 2, 1, 3]
pattern_five = [r, 2, 3, 1, r, 2, 3, 1]
pattern_six = [r, 1, 2, 3, r, 1, 2, 3]
pattern_seven = [r, 1, 3, 2, r, 1, 3, 2]

alternate_pattern_one = [r, 2, 1, 3, a, 2, 1, 3]
alternate_pattern_two = [r, 3, 2, 1, a, 3, 2, 1]
alternate_pattern_three = [r, 1, 2, 3, a, 1, 2, 3]
alternate_pattern_four = [r, 2, 3, 1, a, 2, 3, 1]
alternate_pattern_five = [r, 1, 3, 2, a, 1, 3, 2]
alternate_pattern_size = [r, 1, a, 2, r, 1, a, 2]
alternate_pattern_seven = [r, 1, 2, 1, a, 1, 2, 1]
alternate_pattern_eight = [r, 2, a, 1, r, 2, a, 1]


def pick_pattern_collection_one():
    return [
        pattern_one,
        pattern_two,
        pattern_three,
        pattern_four,
        pattern_five,
        pattern_six,
        pattern_seven
    ]


def pick_pattern_collection_two():
    return [
        alternate_pattern_size,
        alternate_pattern_one,
        alternate_pattern_two,
        alternate_pattern_three,
        alternate_pattern_four,
        alternate_pattern_five,
        alternate_pattern_seven,
        alternate_pattern_eight,
    ]
