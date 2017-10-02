class Chord:
    def __init__(self, root_note, voicing, positions):
        self.root_note = root_note
        self.voicing = voicing

    @property
    def name(self):
        return '{} {}'.format(self.root_note, self.voicing)
