class Rotor:
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring
        self.notch = notch
        self.position = position

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == self.notch

    def forward(self, letter):
        idx = (ord(letter) - 65 + self.position) % 26
        return self.wiring[idx]

    def backward(self, letter):
        idx = (self.wiring.index(letter) - self.position) % 26
        return chr(idx + 65)
