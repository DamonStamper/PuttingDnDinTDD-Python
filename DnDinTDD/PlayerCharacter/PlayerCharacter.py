import random

class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name, alignment = 'Neutral', armorclass = 10, hitpoints = 5):
        self.name = name
        self.alignment = alignment
        self.armorclass = armorclass
        self.hitpoints = hitpoints
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if (isinstance(new_name, str)):
            self.__name = new_name
        else: 
            raise ValueError('Please provide a valid name (string).')

    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, new_alignment):
        alignments = ['Good', 'Evil', 'Neutral']
        if (new_alignment in alignments):
            self.__alignment = new_alignment
        else: 
            raise ValueError(f"Please provide a valid alignment. Valid alignments are {alignments}.")

    @property
    def armorclass(self):
        return self.__armorclass

    @armorclass.setter
    def armorclass(self, new_armorclass):
        self.__armorclass = new_armorclass

    @property
    def hitpoints(self):
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, new_hitpoints):
        self.__hitpoints = new_hitpoints
    
    def attack(self, target):
        to_hit = random.randint(1,20)
        if to_hit >= target.armorclass:
            return True
            #target.Damage()