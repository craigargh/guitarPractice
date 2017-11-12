r = 'r'  # root
a = 'a'  # alternate root

pattern_one = [r, 1, 2, 1, 2, 1, 2, 1]
pattern_two = [r, 1, 2, 1, a, 1, 2, 1]
pattern_three = [r, 2, a, 1, r, 2, a, 1]
pattern_four = [r, 1, a, 2, r, 1, a, 2]
pattern_five = [r, 3, 1, 2, r, 3, 1, 2]
pattern_six = [r, 2, 1, 3, a, 2, 1, 3]
pattern_seven = [r, 3, 2, 1, a, 3, 2, 1]
pattern_eight = [r, 1, 2, 3, a, 1, 2, 3]
pattern_nine = [r, 2, 3, 1, a, 2, 3, 1]
pattern_ten = [r, 1, 3, 2, a, 1, 3, 2]


def pick_pattern_collection_one():
    return [
        pattern_one,
        pattern_two,
        pattern_three,
        pattern_four,
        pattern_five,
        pattern_six,
        pattern_seven,
        pattern_eight,
        pattern_nine,
        pattern_ten,
    ]
