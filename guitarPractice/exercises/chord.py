from typing import List

from guitarPractice.exercises.position import Position


class Chord:
    def __init__(self, root_note: str, voicing: str, positions: List[Position]):
        self.root_note = root_note
        self.voicing = voicing
        self.positions = positions

    def __len__(self) -> int:
        return len(self.positions)

    def __getitem__(self, item) -> Position:
        return self.positions[item]

    def __iter__(self) -> Position:
        for position in self.positions:
            yield position

    @property
    def name(self) -> str:
        return '{} {}'.format(self.root_note, self.voicing)

# TODO: Add property that converts full name into abbreviation e.g. C Major 7 to Cmaj7
# TODO: Add constants for voicings e.g. MAJOR for 'Major', MAJOR_7 for 'Major 7'
