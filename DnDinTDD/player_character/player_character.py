import random


class PlayerCharacter:
    """The entity that is played"""

    INVALID_ATTRIBUTE_WARNING = 'Please provide a valid value (1-20).'

    def __init__(self, name, alignment='Neutral', armorclass=10, hitpoints=5, strength=10, dexterity=10, constitution=10, wisdom=10, intelligence=10, charisma=10, experience=0):
        self.name = name
        self.alignment = alignment
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.armorclass = armorclass
        self.is_alive = True
        self.hitpoints = hitpoints
        self.total_hitpoints = hitpoints
        self.experience = experience

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str):
            self.__name = new_value
        else:
            raise ValueError('Please provide a valid name (string).')

    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, new_value):
        alignments = ['Good', 'Evil', 'Neutral']
        if new_value in alignments:
            self.__alignment = new_value
        else:
            raise ValueError(f"Please provide a valid alignment. Valid alignments are {alignments}.")

    @property
    def armorclass(self):
        return self.__armorclass

    @armorclass.setter
    def armorclass(self, new_value):
        self.__armorclass = new_value

    @property
    def constitution(self):
        return self.__constitution

    @constitution.setter
    def constitution(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__constitution = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    @property
    def wisdom(self):
        return self.__wisdom

    @wisdom.setter
    def wisdom(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__wisdom = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__intelligence = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    @property
    def charisma(self):
        return self.__charisma

    @charisma.setter
    def charisma(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__charisma = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    @property
    def hitpoints(self):
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, new_value):
        self.__hitpoints = new_value
        if self.hitpoints <= 0:
            self.is_alive = False

    @property
    def total_hitpoints(self):
        return self.__total_hitpoints

    @total_hitpoints.setter
    def total_hitpoints(self, new_value):
        new_value = new_value + self.get_ability_modifier(self.constitution)
        new_value = new_value if new_value > 1 else 1
        self.__total_hitpoints = new_value
        self.hitpoints = new_value

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, new_value):
        self.__is_alive = new_value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__strength = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    @property
    def dexterity(self):
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, new_value):
        if isinstance(new_value, int) and 1 <= new_value <= 20:
            self.__dexterity = new_value
        else:
            raise ValueError(PlayerCharacter.INVALID_ATTRIBUTE_WARNING)

    def get_ability_modifier(self, value):
        distance_to_10_5 = value - 10.5
        raw_modifier = distance_to_10_5 / 2
        modifier = int(round(raw_modifier, 0))
        return modifier

    @property
    def to_hit(self):
        to_hit = self.armorclass + self.get_ability_modifier(self.dexterity)
        return to_hit

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_value):
        if isinstance(new_value, int):
            self.__experience = new_value
        else:
            raise ValueError('Please provide a valid experience amount (integer).')

    def attack(self, target):
        to_hit_natural = random.randint(1, 20)
        to_hit_modified = to_hit_natural + self.get_ability_modifier(self.strength)

        damage_amount = 1 + self.get_ability_modifier(self.strength)
        damage_amount = damage_amount if damage_amount > 1 else 1

        if to_hit_natural == 20:
            target.damage(damage_amount, critical=True)
            self.experience += 10
        elif to_hit_modified >= target.to_hit:
            target.damage(damage_amount)
            self.experience += 10

    def damage(self, amount=1, critical=False):
        if critical:
            self.hitpoints = self.hitpoints - (amount * 2)
        else:
            self.hitpoints = self.hitpoints - amount
