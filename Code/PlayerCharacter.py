import pytest

class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if (isinstance(new_name, str)):
            self.__name = new_name
        else: 
            raise Exception('Please provide a valid name (string).')

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