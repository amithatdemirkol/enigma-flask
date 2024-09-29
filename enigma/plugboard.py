class Plugboard:
    def __init__(self, settings):
        self.settings = settings

    def swap(self, letter):
        return self.settings.get(letter, letter)
