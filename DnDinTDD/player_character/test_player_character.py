import pytest
from unittest import mock
from mock import Mock
from unittest.mock import MagicMock

from player_character import player_character

INVALID_ATTRIBUTE_WARNING = 'Please provide a valid value (1-20).'


@pytest.fixture
def mock_player_character():
    return Mock(spec=player_character.PlayerCharacter)


class TestPlayercharacter():
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

    @mock.patch("random.randint", return_value=19, autospec=True)
    def test_playercharacter_can_attack(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        player.attack(enemy)
        assert enemy.hitpoints == 4
        mock_randint.assert_called_once_with(1, 20)

    @mock.patch("random.randint", return_value=20, autospec=True)
    def test_playercharacter_critical_attack_doubles_damage(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        player.attack(enemy)
        assert enemy.hitpoints == 3
        mock_randint.assert_called_once_with(1, 20)

    @mock.patch("random.randint", return_value=2, autospec=True)
    def test_playercharacter_attack_can_miss(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        player.attack(enemy)
        assert enemy.hitpoints == 5
        mock_randint.assert_called_once_with(1, 20)

    def test_playercharacter_attack_can_die(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=1)
        player.damage()
        player.damage()
        assert player.is_alive is False

    def test_playercharacter_ability_modifier_positive(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.get_ability_modifier(12) == 1

    def test_playercharacter_ability_modifier_positive_large(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.get_ability_modifier(17) == 3

    def test_playercharacter_ability_modifier_negative(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.get_ability_modifier(8) == -1

    def test_playercharacter_ability_modifier_negative_large(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.get_ability_modifier(7) == -2


class TestPlayercharacterStrength():
    def test_playercharacter_define_default_strength(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.strength == 10

    def test_playercharacter_define_correct_strength(self):
        player = player_character.PlayerCharacter('Foo', strength=13)
        assert player.strength == 13

    def test_playercharacter_define_incorrect_strength(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', strength='thirteen')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING

    @mock.patch("random.randint", return_value=10, autospec=True)
    def test_playercharacter_strength_modifies_to_hit(self, mock_randint):
        player = player_character.PlayerCharacter('Foo', strength=13)
        enemy = player_character.PlayerCharacter('Bar', armorclass=10, hitpoints=5)
        player.attack(enemy)
        assert enemy.hitpoints < 5

    @mock.patch("random.randint", return_value=19, autospec=True)
    def test_playercharacter_strength_modifies_to_hit_doesnt_trigger_critical(self, mock_randint):
        player = player_character.PlayerCharacter('Foo', strength=13)
        enemy = player_character.PlayerCharacter('Bar', armorclass=10, hitpoints=5)
        player.attack(enemy)
        assert enemy.hitpoints == 3

    @mock.patch("random.randint", return_value=19, autospec=True)
    def test_playercharacter_strength_modifies_damage(self, mock_randint):
        player = player_character.PlayerCharacter('Foo', strength=13)
        enemy = player_character.PlayerCharacter('Bar', armorclass=10, hitpoints=5)
        player.attack(enemy)
        assert enemy.hitpoints == 3

    @mock.patch("random.randint", return_value=19, autospec=True)
    def test_playercharacter_strength_modifier_never_less_than_1_damage(self, mock_randint):
        player = player_character.PlayerCharacter('Foo', strength=1)
        enemy = player_character.PlayerCharacter('Bar', armorclass=1, hitpoints=5)
        enemy.damage = MagicMock()
        player.attack(enemy)
        enemy.damage.assert_called_once_with(1)

    @mock.patch("random.randint", return_value=20, autospec=True)
    def test_playercharacter_strength_modifier_never_less_than_1_damage_on_critical_hit(self, mock_randint, mock_player_character):
        player = player_character.PlayerCharacter('Foo', strength=1)
        enemy = player_character.PlayerCharacter('Bar', armorclass=1, hitpoints=5)
        enemy.damage = MagicMock()
        player.attack(enemy)
        enemy.damage.assert_called_once_with(1, critical=True)

    @mock.patch("random.randint", return_value=19, autospec=True)
    def test_playercharacter_successful_attack_earns_experience(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        enemy.damage = MagicMock()
        player.attack(enemy)
        enemy.damage.assert_called()
        assert player.experience == 10

    @mock.patch("random.randint", return_value=20, autospec=True)
    def test_playercharacter_critical_attack_earns_experience(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        enemy.damage = MagicMock()
        player.attack(enemy)

        enemy.damage.assert_called()
        assert player.experience == 10

    @mock.patch("random.randint", return_value=2, autospec=True)
    def test_playercharacter_failed_attack_doesnt_earn_experience(self, mock_randint):
        player = player_character.PlayerCharacter('Foo')
        enemy = player_character.PlayerCharacter('Bar')
        enemy.damage = MagicMock()
        player.attack(enemy)

        enemy.damage.assert_not_called()
        assert player.experience == 0

    def test_playercharacter_create_with_invalid_experience(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', experience='a')
            assert str(exp.value) == 'Please provide a valid experience amount (integer).'


class TestPlayercharacterDexterity():
    def test_playercharacter_define_default_dexterity(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.dexterity == 10

    def test_playercharacter_define_correct_dexterity(self):
        player = player_character.PlayerCharacter('Foo', dexterity=13)
        assert player.dexterity == 13

    def test_playercharacter_define_incorrect_dexterity(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', dexterity='thirteen')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING

    def test_playercharacter_dexterity_modifies_armorclass(self):
        player = player_character.PlayerCharacter('Foo', dexterity=13)
        assert player.to_hit == 11


class TestPlayercharacterConstitution():
    def test_playercharacter_define_default_constitution(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.constitution == 10

    def test_playercharacter_define_correct_constitution(self):
        player = player_character.PlayerCharacter('Foo', constitution=13)
        assert player.constitution == 13

    def test_playercharacter_define_incorrect_constitution(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', constitution='thirteen')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING

    def test_playercharacter_constitution_modifier_negative(self):
        player = player_character.PlayerCharacter('Foo', constitution=8)
        assert player.get_ability_modifier(player.constitution) == -1

    def test_playercharacter_constitution_modifies_hitpoints(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=5, constitution=13)
        assert player.hitpoints == 6

    def test_playercharacter_constitution_modifies_hitpoints_not_less_than_one(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=3, constitution=2)
        assert player.hitpoints == 1

    def test_playercharacter_constitution_modifies_total_hitpoints(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=5, constitution=13)
        assert player.total_hitpoints == 6

    def test_playercharacter_constitution_modifies_total_hitpoints_not_less_than_one(self):
        player = player_character.PlayerCharacter('Foo', hitpoints=3, constitution=2)
        assert player.total_hitpoints == 1


class TestPlayercharacterWisdom():
    def test_playercharacter_define_default_wisdom(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.wisdom == 10

    def test_playercharacter_define_incorrect_wisdom(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', wisdom='a')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING


class TestPlayercharacterIntelligence():
    def test_playercharacter_define_default_intelligence(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.intelligence == 10

    def test_playercharacter_define_incorrect_intelligence(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', intelligence='a')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING


class TestPlayercharacterCharisma():
    def test_playercharacter_define_default_charisma(self):
        player = player_character.PlayerCharacter('Foo')
        assert player.charisma == 10

    def test_playercharacter_define_incorrect_charisma(self):
        with pytest.raises(ValueError) as exp:
            player_character.PlayerCharacter('Foo', charisma='a')
        assert str(exp.value) == INVALID_ATTRIBUTE_WARNING
