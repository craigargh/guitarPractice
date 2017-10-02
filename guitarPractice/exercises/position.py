class Position:
    def __init__(self, *, fret, guitar_string, finger, is_highlighted=True):
        self.fret = fret
        self.guitar_string = guitar_string
        self.finger = finger
