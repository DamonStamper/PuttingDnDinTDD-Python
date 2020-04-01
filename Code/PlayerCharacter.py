import pytest

class PlayerCharArmorClasster:
    """The entity that is played"""

    def __init__(self, name, alignment = 'Neutral', ArmorClass = 10):
        self.name = name
        self.alignment = alignment
        self.ArmorClass = ArmorClass
    
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
    def ArmorClass(self):
        return self.__ArmorClass

    @ArmorClass.setter
    def ArmorClass(self, new_ArmorClass):
        self.__ArmorClass = new_ArmorClass


def test_PlayerCharArmorClasster_CreateCorrectName():
    PlayerCharArmorClasster('Foo')

def test_PlayerCharArmorClasster_CreateIncorrectName():
    with pytest.raises(Exception):
        PlayerCharArmorClasster(7)

def test_PlayerCharArmorClasster_GetCorrectName():
    player = PlayerCharArmorClasster('Foo')
    assert player.name == 'Foo'

def test_PlayerCharArmorClasster_RenameCorrectName():
    player = PlayerCharArmorClasster('Foo')
    player.name = 'Bar'
    assert player.name == 'Bar'

def test_PlayerCharArmorClasster_RenameIncorrectName():
    player = PlayerCharArmorClasster('Foo')
    with pytest.raises(Exception):
        player.name = 7

def test_PlayerCharArmorClasster_CreateDefaultAlignment():
    player = PlayerCharArmorClasster('Foo')
    assert player.alignment == 'Neutral'


def test_PlayerCharArmorClasster_CreateSpecificAlignment():
    player = PlayerCharArmorClasster('Foo', alignment='Good')
    assert player.alignment == 'Good'

def test_PlayerCharArmorClasster_CreateIncorrectAlignment():
    with pytest.raises(Exception):
        PlayerCharArmorClasster('Foo', alignment='Something')

def test_PlayerCharArmorClasster_CreateDefaultArmorClass():
    player = PlayerCharArmorClasster('Foo')
    assert player.ArmorClass == 10

def test_PlayerCharArmorClasster_CreateSpecifictArmorClass():
    player = PlayerCharArmorClasster('Foo', ArmorClass=7)
    assert player.ArmorClass == 7