import copy
from typing import List

from guitarPractice.guitar_shapes.position import Position


class GuitarShape:
    def __init__(self, root_note: str, tonality: str, positions: List[Position]):
        self.root_note = root_note
        self.tonality = tonality
        self.positions = positions
        self.is_picked = True

    def __len__(self) -> int:
        return len(self.positions)

    def __getitem__(self, item) -> Position:
        return self.positions[item]

    def __iter__(self) -> Position:
        for position in self.positions:
            yield position

    def __str__(self) -> str:
        return f"{self.root_note} {self.tonality}"

    def __repr__(self):
        return f"GuitarShape('{self.root_note}', '{self.tonality}', {self.positions})"

    @property
    def name(self) -> str:
        return '{} {}'.format(self.root_note, self.tonality)

    @property
    def is_strummed(self):
        return not self.is_picked

    @is_strummed.setter
    def is_strummed(self, value):
        self.is_picked = not value

    def transform(self, transformer):
        transformed_shape = copy.deepcopy(self)
        transformed_shape.positions = list(transformer(self.positions))

        return transformed_shape



# TODO: Add property that converts full name into abbreviation e.g. C Major 7 to Cmaj7
# TODO: Add constants for voicings e.g. MAJOR for 'Major', MAJOR_7 for 'Major 7'
