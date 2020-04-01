import pytest

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

def test_PlayerCharacter_IncorrectNoParameters():
    with pytest.raises(Exception):
        PlayerCharacter()

def test_PlayerCharacterArmorClass_CreateCorrectName():
    PlayerCharacter('Foo')

def test_PlayerCharacterArmorClasster_CreateIncorrectName():
    with pytest.raises(Exception):
        PlayerCharacter(7)

def test_PlayerCharacter_GetCorrectName():
    Player = PlayerCharacter('Foo')
    assert Player.name == 'Foo'

def test_PlayerCharacter_RenameCorrectName():
    Player = PlayerCharacter('Foo')
    Player.name = 'Bar'
    assert Player.name == 'Bar'

def test_PlayerCharacter_RenameIncorrectName():
    Player = PlayerCharacter('Foo')
    with pytest.raises(Exception):
        Player.name = 7

def test_PlayerCharacter_CreateDefaultAlignment():
    Player = PlayerCharacter('Foo')
    assert Player.Alignment == 'Neutral'


def test_PlayerCharacter_CreateSpecificAlignment():
    Player = PlayerCharacter('Foo', Alignment='Good')
    assert Player.Alignment == 'Good'

def test_PlayerCharacter_CreateIncorrectAlignment():
    with pytest.raises(Exception):
        PlayerCharacter('Foo', Alignment='Something')

def test_PlayerCharacter_CreateDefaultArmorClass():
    Player = PlayerCharacter('Foo')
    assert Player.ArmorClass == 10

def test_PlayerCharacter_CreateSpecifictArmorClass():
    Player = PlayerCharacter('Foo', ArmorClass=7)
    assert Player.ArmorClass == 7

def test_PlayerCharacter_CreateDefaultHitPoints():
    Player = PlayerCharacter('Foo')
    assert Player.HitPoints == 5

def test_PlayerCharacter_CreateSpecifictHitPoints():
    Player = PlayerCharacter('Foo', HitPoints=7)
    assert Player.HitPoints == 7