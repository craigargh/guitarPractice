class Position:
    def __init__(self, *, guitar_string: int, fret: int = 0, finger: int = 0, is_highlighted: bool = False,
                 duration: float = 1):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
        self.is_highlighted = is_highlighted
        self.duration = duration

    def __str__(self):
        return f"(string: {self.guitar_string}, fret: {self.fret}, finger: {self.finger})"

    def __repr__(self):
        return f"Position(guitar_string={self.guitar_string}, fret={self.fret}, finger={self.finger})"

# TODO: Add label/annotation to Position to output shape name for chord changes when printing a sequence
