import pytest

class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name, alignment='Neutral'):
        self.name = name
        self.alignment = alignment
    
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


def test_PlayerCharacter_CreateCorrectName():
    PlayerCharacter('Foo')

def test_PlayerCharacter_CreateIncorrectName():
    with pytest.raises(Exception):
        PlayerCharacter(7)

def test_PlayerCharacter_GetCorrectName():
    player = PlayerCharacter('Foo')
    assert player.name == 'Foo'

def test_PlayerCharacter_RenameCorrectName():
    player = PlayerCharacter('Foo')
    player.name = 'Bar'
    assert player.name == 'Bar'

def test_PlayerCharacter_RenameIncorrectName():
    player = PlayerCharacter('Foo')
    with pytest.raises(Exception):
        player.name = 7

def test_PlayerCharacter_CreateDefaultAlignment():
    player = PlayerCharacter('Foo')
    assert player.alignment == 'Neutral'


def test_PlayerCharacter_CreateSpecificAlignment():
    player = PlayerCharacter('Foo', 'Good')
    assert player.alignment == 'Good'

def test_PlayerCharacter_CreateIncorrectAlignment():
    with pytest.raises(Exception):
        PlayerCharacter('Foo', 'Something')