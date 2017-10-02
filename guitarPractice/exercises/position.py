class Position:
    def __init__(self, *, guitar_string: int, fret: int = 0, finger: int = 0, is_highlighted: bool = False):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
        self.is_highlighted = is_highlighted
