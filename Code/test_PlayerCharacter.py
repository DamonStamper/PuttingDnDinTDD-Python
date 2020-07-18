import pytest
import unittest.mock 

import PlayerCharacter

def test_playercharacter_incorrect_no_parameters():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter()

def test_playercharacter_armorclass_create_correct_name():
    PlayerCharacter.PlayerCharacter('Foo')

def test_playercharacter_armorclass_create_incorrect_name():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter(7)

def test_playercharacter_get_correct_name():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.name == 'Foo'

def test_playercharacter_rename_correct_name():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    Player.name = 'Bar'
    assert Player.name == 'Bar'

def test_playercharacter_rename_incorrect_name():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    with pytest.raises(Exception):
        Player.name = 7

def test_playercharacter_create_default_alignment():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.alignment == 'Neutral'


def test_playercharacter_create_specific_alignment():
    Player = PlayerCharacter.PlayerCharacter('Foo', alignment='Good')
    assert Player.alignment == 'Good'

def test_playercharacter_create_incorrect_alignment():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter('Foo', alignment='Something')

def test_playercharacter_create_default_armorclass():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.armorclass == 10

def test_playercharacter_create_specific_armorclass():
    Player = PlayerCharacter.PlayerCharacter('Foo', armorclass=7)
    assert Player.armorclass == 7

def test_playercharacter_create_default_hitpoints():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.hitpoints == 5

def test_playercharacter_create_specifict_hitpoints():
    Player = PlayerCharacter.PlayerCharacter('Foo', hitpoints=7)
    assert Player.hitpoints == 7

def test_playercharacter_can_attack():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    Enemy = PlayerCharacter.PlayerCharacter('Bar')
    Player.attack(Enemy)
