class Chord:
    def __init__(self, root_note, voicing, positions):
        self.root_note = root_note
        self.voicing = voicing
        self.positions = positions

    def __len__(self):
        return len(self.positions)

    def __getitem__(self, item):
        return self.positions[item]

    def __iter__(self):
        for position in self.positions:
            yield position

    @property
    def name(self):
        return '{} {}'.format(self.root_note, self.voicing)
