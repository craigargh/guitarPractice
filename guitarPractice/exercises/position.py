class Position:
    def __init__(self, *, fret: int, guitar_string: int, finger: int, is_highlighted: bool = False):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
        self.is_highlighted = is_highlighted
