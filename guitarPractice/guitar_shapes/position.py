class Position:
    def __init__(self, *, guitar_string: int, fret: int = 0, finger: int = 0, is_highlighted: bool = False,
                 order: int = None):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
        self.is_highlighted = is_highlighted
        self.order = order

    def __str__(self):
        return f"(string: {self.guitar_string}, fret: {self.fret}, finger: {self.finger})"

    def __repr__(self):
        return f"Position(guitar_string={self.guitar_string}, fret={self.fret}, finger={self.finger})"

    def __eq__(self, other):
        same_string = self.guitar_string == other.guitar_string
        same_fret = self.fret == other.fret
        same_finger = self.finger == other.finger

        return same_string and same_fret and same_finger

    def as_dict(self):
        return {
            'fret': self.fret,
            'guitar_string': self.guitar_string,
            'finger': self.finger,
            'is_highlighted': self.is_highlighted,
        }
