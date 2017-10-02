from guitarPractice.exercises import position


class Chord:
    def __init__(self, root_note: str, voicing: str, positions: list):
        self.root_note = root_note
        self.voicing = voicing
        self.positions = positions

    def __len__(self) -> int:
        return len(self.positions)

    def __getitem__(self, item) -> position:
        return self.positions[item]

    def __iter__(self) -> position:
        for position in self.positions:
            yield position

    @property
    def name(self) -> str:
        return '{} {}'.format(self.root_note, self.voicing)
