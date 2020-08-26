import pytest
import unittest.mock 

from .context import PlayerCharacter

def test_playercharacter_incorrect_no_parameters():
    with pytest.raises(TypeError):
        PlayerCharacter.PlayerCharacter()

def test_playercharacter_armorclass_create_correct_name():
    player = PlayerCharacter.PlayerCharacter('Foo')
    assert player.name == 'Foo'

def test_playercharacter_armorclass_create_incorrect_name():
    with pytest.raises(ValueError):
        PlayerCharacter.PlayerCharacter(7)

def test_playercharacter_get_correct_name():
    player = PlayerCharacter.PlayerCharacter('Foo')
    assert player.name == 'Foo'

def test_playercharacter_rename_correct_name():
    player = PlayerCharacter.PlayerCharacter('Foo')
    player.name = 'Bar'
    assert player.name == 'Bar'

def test_playercharacter_rename_incorrect_name():
    player = PlayerCharacter.PlayerCharacter('Foo')
    with pytest.raises(ValueError):
        player.name = 7

def test_playercharacter_create_default_alignment():
    player = PlayerCharacter.PlayerCharacter('Foo')
    assert player.alignment == 'Neutral'


def test_playercharacter_create_specific_alignment():
    player = PlayerCharacter.PlayerCharacter('Foo', alignment='Good')
    assert player.alignment == 'Good'

def test_playercharacter_create_incorrect_alignment():
    with pytest.raises(ValueError) as exp:
        PlayerCharacter.PlayerCharacter('Foo', alignment='Something')

def test_playercharacter_create_default_armorclass():
    player = PlayerCharacter.PlayerCharacter('Foo')
    assert player.armorclass == 10

def test_playercharacter_create_specific_armorclass():
    player = PlayerCharacter.PlayerCharacter('Foo', armorclass=7)
    assert player.armorclass == 7

def test_playercharacter_create_default_hitpoints():
    player = PlayerCharacter.PlayerCharacter('Foo')
    assert player.hitpoints == 5

def test_playercharacter_create_specifict_hitpoints():
    player = PlayerCharacter.PlayerCharacter('Foo', hitpoints=7)
    assert player.hitpoints == 7

def test_playercharacter_can_attack():
    player = PlayerCharacter.PlayerCharacter('Foo')
    enemy = PlayerCharacter.PlayerCharacter('Bar')
    player.attack(enemy)
