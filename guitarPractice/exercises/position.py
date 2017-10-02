class Position:
    def __init__(self, *, fret, guitar_string, finger, is_highlighted=False):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
        self.is_highlighted = is_highlighted
