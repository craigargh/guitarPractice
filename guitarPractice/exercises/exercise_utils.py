from functools import partial
from random import choice


def choose_transformer(choices, notes_length):
    transformer = choice(choices)
    return partial(transformer, sequence_length=notes_length)
