from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard

class EnigmaMachine:
    def __init__(self, initial_rotor_positions):
        self.rotors = [
            Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16, initial_rotor_positions[0]),
            Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 4, initial_rotor_positions[1]),
            Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 21, initial_rotor_positions[2]),
        ]
        self.reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.plugboard = Plugboard({'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'})

    def encrypt_letter(self, letter):
        letter = self.plugboard.swap(letter)

        for rotor in self.rotors:
            letter = rotor.forward(letter)

        letter = self.reflector.reflect(letter)

        for rotor in reversed(self.rotors):
            letter = rotor.backward(letter)

        letter = self.plugboard.swap(letter)
        return letter

    def encrypt_message(self, message):
        encrypted_message = []
        for letter in message:
            if letter.isalpha():
                if self.rotors[0].rotate():
                    if self.rotors[1].rotate():
                        self.rotors[2].rotate()
                encrypted_message.append(self.encrypt_letter(letter))
            else:
                encrypted_message.append(letter)
        return ''.join(encrypted_message)
