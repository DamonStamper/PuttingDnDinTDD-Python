import pytest

from player_character import player_character


class Test_Playercharacter():
    def test_playercharacter_incorrect_no_parameters(self):
        with pytest.raises(TypeError) as exp:
            player_character.PlayerCharacter()
        assert str(exp.value) == "__init__() missing 1 required positional argument: 'name'"

    def test_playercharacter_armorclass_create_incorrect_name(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter(7)
        assert str(exp.value) == 'Please provide a valid name (string).'

    def test_playercharacter_get_correct_name(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.name == 'Foo'

    def test_playercharacter_rename_correct_name(self):
        player = player_character.PlayerCharacter('Foo')
        player.name = 'Bar'
        assert player.name == 'Bar'

    def test_playercharacter_rename_incorrect_name(self):
        player = player_character.PlayerCharacter('Foo')
        with pytest.raises(ValueError) as exp:
            player.name = 7
        assert str(exp.value) == 'Please provide a valid name (string).'

    def test_playercharacter_create_default_alignment(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.alignment == 'Neutral'

    def test_playercharacter_create_specific_alignment(self):
        player = player_character.PlayerCharacter('Foo', alignment='Good')
        assert player.alignment == 'Good'

    def test_playercharacter_create_incorrect_alignment(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', alignment='Something')
        assert str(exp.value).startswith("Please provide a valid alignment. Valid alignments are")

    def test_playercharacter_create_default_armorclass(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.armorclass == 10

    def test_playercharacter_create_specific_armorclass(self):
        player = player_character.PlayerCharacter('Foo', armorclass=7)
        assert player.armorclass == 7

    def test_playercharacter_create_default_hitpoints(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.hitpoints == 5

    def test_playercharacter_create_specific_hitpoints(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=7)
        assert player.hitpoints == 7

    def test_playercharacter_can_attack(self):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        player.attack(enemy)
