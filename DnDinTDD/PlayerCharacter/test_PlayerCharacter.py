import pytest
# import unittest

from PlayerCharacter import PlayerCharacter


class Test_playercharacter():
    def test_playercharacter_incorrect_no_parameters(self):
        with pytest.raises(TypeError):
            PlayerCharacter.PlayerCharacter()

    def test_playercharacter_armorclass_create_correct_name(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        assert player.name == 'Foo'

    def test_playercharacter_armorclass_create_incorrect_name(self):
        with pytest.raises(ValueError):
            PlayerCharacter.PlayerCharacter(7)

    def test_playercharacter_get_correct_name(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        assert player.name == 'Foo'

    def test_playercharacter_rename_correct_name(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        player.name = 'Bar'
        assert player.name == 'Bar'

    def test_playercharacter_rename_incorrect_name(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        with pytest.raises(ValueError):
            player.name = 7

    def test_playercharacter_create_default_alignment(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        assert player.alignment == 'Neutral'

    def test_playercharacter_create_specific_alignment(self):
        player = PlayerCharacter.PlayerCharacter('Foo', alignment='Good')
        assert player.alignment == 'Good'

    def test_playercharacter_create_incorrect_alignment(self):
        with pytest.raises(ValueError):
            PlayerCharacter.PlayerCharacter('Foo', alignment='Something')

    def test_playercharacter_create_default_armorclass(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        assert player.armorclass == 10

    def test_playercharacter_create_specific_armorclass(self):
        player = PlayerCharacter.PlayerCharacter('Foo', armorclass=7)
        assert player.armorclass == 7

    def test_playercharacter_create_default_hitpoints(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        assert player.hitpoints == 5

    def test_playercharacter_create_specifict_hitpoints(self):
        player = PlayerCharacter.PlayerCharacter('Foo', hitpoints=7)
        assert player.hitpoints == 7

    def test_playercharacter_can_attack(self):
        player = PlayerCharacter.PlayerCharacter('Foo')
        enemy = PlayerCharacter.PlayerCharacter('Bar')
        player.attack(enemy)
