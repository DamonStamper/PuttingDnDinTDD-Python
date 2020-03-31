class PlayerCharacter:
    """The entity that is played"""

    def __init__(self, name):
        self.name = name

def test_PlayerCharacter_name():
    player = PlayerCharacter('Bob')
    assert player.name == 'Bob'