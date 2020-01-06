# Reason
To follow https://github.com/PuttingTheDnDInTDD/EverCraft-Kata

#Iteration 1 - Core
##Above this line is completed, below is todo
Feature: Create a Character

    As a character I want to have a name so that I can be distinguished from other characters

    can get and set Name

Feature: Alignment

    As a character I want to have an alignment so that I have something to guide my actions

    can get and set alignment
    alignments are Good, Evil, and Neutral

Feature: Armor Class & Hit Points

    As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies

    has an Armor Class that defaults to 10
    has 5 Hit Points by default

Feature: Character Can Attack

    As a combatant I want to be able to attack other combatants so that I can survive to fight another day

    roll a 20 sided die (don't code the die)
    roll must meet or beat opponents armor class to hit

Feature: Character Can Be Damaged

    As an attacker I want to be able to damage my enemies so that they will die and I will live

    If attack is successful, other character takes 1 point of damage when hit
    If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
    when hit points are 0 or fewer, the character is dead

Feature: Character Has Abilities Scores

    As a character I want to have several abilities so that I am not identical to other characters except in name

    Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
    Abilities range from 1 to 20 and default to 10
    Abilities have modifiers according to the following table

Score 	Modifier 	Score 	Modifier 	Score 	Modifier 	Score 	Modifier
1 	-5 	6 	-2 	11 	0 	16 	+3
2 	-4 	7 	-2 	12 	+1 	17 	+3
3 	-4 	8 	-1 	13 	+1 	18 	+4
4 	-3 	9 	-1 	14 	+2 	19 	+4
5 	-3 	10 	0 	15 	+2 	20 	+5
Feature: Character Ability Modifiers Modify Attributes

    As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

    add Strength modifier to:
        attack roll and damage dealt
        double Strength modifier on critical hits
        minimum damage is always 1 (even on a critical hit)
    add Dexterity modifier to armor class
    add Constitution modifier to hit points (always at least 1 hit point)

Feature: A Character can gain experience when attacking

    As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

    When a successful attack occurs, the character gains 10 experience points

Feature: A Character Can Level

    As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

    Level defaults to 1
    After 1000 experience points, the character gains a level
        0 xp -> 1st Level
        1000 xp -> 2nd Level
        2000 xp -> 3rd Level
        etc.
    For each level:
        hit points increase by 5 plus Con modifier
        1 is added to attack roll for every even level achieved
