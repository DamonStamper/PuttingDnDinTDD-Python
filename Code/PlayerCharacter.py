import random

class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name, Alignment = 'Neutral', ArmorClass = 10, HitPoints = 5):
        self.name = name
        self.Alignment = Alignment
        self.ArmorClass = ArmorClass
        self.HitPoints = HitPoints
    
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
    def Alignment(self):
        return self.__Alignment

    @Alignment.setter
    def Alignment(self, new_Alignment):
        Alignments = ['Good', 'Evil', 'Neutral']
        if (new_Alignment in Alignments):
            self.__Alignment = new_Alignment
        else: 
            raise Exception(f"Please provide a valid Alignment. Valid Alignments are {Alignments}.")

    @property
    def ArmorClass(self):
        return self.__ArmorClass

    @ArmorClass.setter
    def ArmorClass(self, new_ArmorClass):
        self.__ArmorClass = new_ArmorClass

    @property
    def HitPoints(self):
        return self.__HitPoints

    @HitPoints.setter
    def HitPoints(self, new_HitPoints):
        self.__HitPoints = new_HitPoints
    
    def Attack(self, Target):
        ToHit = random.randint(1,20)
        if ToHit >= Target.ArmorClass:
            return True
            #Target.Damage()