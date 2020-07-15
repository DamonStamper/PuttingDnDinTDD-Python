import pytest
import unittest.mock 

import PlayerCharacter

def test_PlayerCharacter_IncorrectNoParameters():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter()

def test_PlayerCharacterArmorClass_CreateCorrectName():
    PlayerCharacter.PlayerCharacter('Foo')

def test_PlayerCharacterArmorClasster_CreateIncorrectName():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter(7)

def test_PlayerCharacter_GetCorrectName():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.name == 'Foo'

def test_PlayerCharacter_RenameCorrectName():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    Player.name = 'Bar'
    assert Player.name == 'Bar'

def test_PlayerCharacter_RenameIncorrectName():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    with pytest.raises(Exception):
        Player.name = 7

def test_PlayerCharacter_CreateDefaultAlignment():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.Alignment == 'Neutral'


def test_PlayerCharacter_CreateSpecificAlignment():
    Player = PlayerCharacter.PlayerCharacter('Foo', Alignment='Good')
    assert Player.Alignment == 'Good'

def test_PlayerCharacter_CreateIncorrectAlignment():
    with pytest.raises(Exception):
        PlayerCharacter.PlayerCharacter('Foo', Alignment='Something')

def test_PlayerCharacter_CreateDefaultArmorClass():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.ArmorClass == 10

def test_PlayerCharacter_CreateSpecifictArmorClass():
    Player = PlayerCharacter.PlayerCharacter('Foo', ArmorClass=7)
    assert Player.ArmorClass == 7

def test_PlayerCharacter_CreateDefaultHitPoints():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    assert Player.HitPoints == 5

def test_PlayerCharacter_CreateSpecifictHitPoints():
    Player = PlayerCharacter.PlayerCharacter('Foo', HitPoints=7)
    assert Player.HitPoints == 7

def test_PlayerCharacter_CanAttack():
    Player = PlayerCharacter.PlayerCharacter('Foo')
    Enemy = PlayerCharacter.PlayerCharacter('Bar')
    Player.Attack(Enemy)
