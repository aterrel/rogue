from random import randint


class Dice:
    def __init__(self, d4:int=0, d6:int = 0, d10:int = 0, d20:int = 0, mod=0):
        self.d4, self.d6, self.d10, self.d20, self.mod = d4, d6, d10, d20, mod

    def roll(self):
        cumm_sum = 0
        for _ in range(self.d4):
            cumm_sum += randint(1,4)
        for _ in range(self.d6):
            cumm_sum += randint(1, 6)
        for _ in range(self.d10):
            cumm_sum += randint(1,10)
        for _ in range(self.d20):
            cumm_sum += randint(1, 20)
        return cumm_sum + self.mod


class Armor:
    def __init__(self, name:str, armor_class:int, weight:int) -> None:
        self.name = name
        self.armor_class = armor_class
        self.weight = weight


class Weapon:
    def __init__(self, name:str, damage_dice:Dice, damage_attribute:str, weight:int) -> None:
        self.name = name
        self.damage_dice = damage_dice
        self.damage_attribute = damage_attribute
        self.weight = weight

    def damage(self, character)->int:
        return self.damage_dice.roll() + character.__getattribute__(self.damage_attribute) % 4


class Character:
    """Character class

    Represents all characters in the game.

    >>> moe = Character(health=10, armor=2, weapons=[], num_attack=1, playable=True)
    """
    def __init__(self, strength:int, dexterity:int, health:int, armor:Armor, weapons:list[Weapon], num_attack, playable=False) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.health = health
        self.armor = armor
        self.weapons = weapons
        self.num_attack = num_attack
        self.playable = playable


if __name__ == "__main__":
    # Create a world 
    armor_stash = {
        "leather": Armor("leather", armor_class=13, weight=3),
        "studded leather": Armor("studded leather", armor_class=15, weight=5),
    }
    weapon_stash = {
        "longsword": Weapon("longsword", damage_attribute="strength", damage_dice=Dice(d6=2, mod=3), weight=1)
    }
    npc_stash = {
        "moe": Character(strength=12, dexterity=5, health=10, armor=armor_stash['leather'], weapons=[weapon_stash['longsword']], num_attack=1, playable=False)
    }