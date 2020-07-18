import random

class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name, alignment = 'Neutral', armorClass = 10, hitPoints = 5):
        self.name = name
        self.alignment = alignment
        self.armorClass = armorClass
        self.hitPoints = hitPoints
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if (isinstance(new_name, str)):
            self.__name = new_name
        else: 
            raise Exception('Please provide a valid name (string).')

    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, new_alignment):
        alignments = ['Good', 'Evil', 'Neutral']
        if (new_alignment in alignments):
            self.__alignment = new_alignment
        else: 
            raise Exception(f"Please provide a valid alignment. Valid alignments are {alignments}.")

    @property
    def armorClass(self):
        return self.__armorClass

    @armorClass.setter
    def armorClass(self, new_armorClass):
        self.__armorClass = new_armorClass

    @property
    def hitPoints(self):
        return self.__hitPoints

    @hitPoints.setter
    def hitPoints(self, new_hitPoints):
        self.__hitPoints = new_hitPoints
    
    def Attack(self, Target):
        ToHit = random.randint(1,20)
        if ToHit >= Target.armorClass:
            return True
            #Target.Damage()