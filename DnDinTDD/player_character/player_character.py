import random


class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name, alignment='Neutral', armorclass=10, hitpoints=5, strength=10):
        self.name = name
        self.alignment = alignment
        self.armorclass = armorclass
        self.hitpoints = hitpoints
        self.is_alive = True
        self.strength = strength

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str):
            self.__name = new_value
        else:
            raise ValueError('Please provide a valid name (string).')

    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, new_value):
        alignments = ['Good', 'Evil', 'Neutral']
        if new_value in alignments:
            self.__alignment = new_value
        else:
            raise ValueError(f"Please provide a valid alignment. Valid alignments are {alignments}.")

    @property
    def armorclass(self):
        return self.__armorclass

    @armorclass.setter
    def armorclass(self, new_value):
        self.__armorclass = new_value

    @property
    def hitpoints(self):
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, new_value):
        self.__hitpoints = new_value
        if self.hitpoints <= 0:
            self.is_alive = False

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, new_value):
        self.__is_alive = new_value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__strength = new_value
        else:
            raise ValueError('Please provide a valid value (1-20).')

    def attack(self, target):
        to_hit = random.randint(1, 20)
        if to_hit == 20:
            target.damage(critical=True)
        elif to_hit >= target.armorclass:
            target.damage()

    def damage(self, critical=False):
        if critical:
            self.hitpoints = self.hitpoints - 2
        else:
            self.hitpoints = self.hitpoints - 1
