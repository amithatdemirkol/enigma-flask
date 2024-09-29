class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, letter):
        idx = ord(letter) - 65
        return self.wiring[idx]
