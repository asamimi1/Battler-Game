import random

class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: list, value: int, crit_chance: float, crit_multiplier: float) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier

    def calculate_damage(self) -> float:
        return random.choice(range(self.damage[0], self.damage[1]+1))
        
fists = Weapon(name="Fists",
                    weapon_type="Blunt",
                    damage=[2,5],
                    value=0,
                    crit_chance=0.05,
                    crit_multiplier=1.8)

claws = Weapon(name="Claws",
                    weapon_type="Sharp",
                    damage=[3,6],
                    value=0,
                    crit_chance=0.08,
                    crit_multiplier=1.8)

spit = Weapon(name="Spit",
                    weapon_type="Ranged",
                    damage=[7,10],
                    value=0,
                    crit_chance=0.15,
                    crit_multiplier=1.3)

bronze_sword = Weapon(name="Bronze Sword",
                    weapon_type="Sharp",
                    damage=[3,6],
                    value=8,
                    crit_chance=0.12,
                    crit_multiplier=1.5)

iron_sword = Weapon(name="Iron Sword",
                    weapon_type="Sharp",
                    damage=[5,8],
                    value=10,
                    crit_chance=0.2,
                    crit_multiplier=1.5)

fire_wand = Weapon(name="Fire Wand",
                    weapon_type="Magic",
                    damage=[6,9],
                    value=11,
                    crit_chance=0.2,
                    crit_multiplier=1.5)

ice_staff = Weapon(name="Ice Staff",
                    weapon_type="Magic",
                    damage=[8,11],
                    value=11,
                    crit_chance=0.15,
                    crit_multiplier=1.8)

great_sword = Weapon(name="Great Sword",
                    weapon_type="Sharp",
                    damage=[8,11],
                    value=12,
                    crit_chance=0.12,
                    crit_multiplier=1.5)

daggers = Weapon(name="Daggers",
                    weapon_type="Sharp",
                    damage=[5,8],
                    value=11,
                    crit_chance=0.45,
                    crit_multiplier=2)

pike = Weapon(name="Pike",
                    weapon_type="Sharp",
                    damage=[9,12],
                    value=14,
                    crit_chance=0.25,
                    crit_multiplier=1.2)

short_bow = Weapon(name="Short Bow",
                    weapon_type="Ranged",
                    damage=[4,7],
                    value=7,
                    crit_chance=0.25,
                    crit_multiplier=2.5)

long_bow = Weapon(name="Long Bow",
                    weapon_type="Ranged",
                    damage=[6,9],
                    value=9,
                    crit_chance=0.15,
                    crit_multiplier=2.0)

mace = Weapon(name="Mace",
                    weapon_type="Blunt",
                    damage=[6,9],
                    value=10,
                    crit_chance=0.15,
                    crit_multiplier=1.8)

flail = Weapon(name="Flail",
                    weapon_type="Blunt",
                    damage=[7,10],
                    value=11,
                    crit_chance=0.16,
                    crit_multiplier=1.6)

barbarian_axe = Weapon(name="Barbarian Axe",
                    weapon_type="Sharp",
                    damage=[8,11],
                    value=15,
                    crit_chance=0.25,
                    crit_multiplier=1.9)

spiked_mace = Weapon(name="Spiked Mace",
                    weapon_type="Blunt",
                    damage=[9,12],
                    value=14,
                    crit_chance=0.20,
                    crit_multiplier=1.5)

void_scepter = Weapon(name="Void Scepter",
                    weapon_type="Magic",
                    damage=[10,13],
                    value=14,
                    crit_chance=0.15,
                    crit_multiplier=1.7)

fire_breath = Weapon(name="Fire Breath",
                    weapon_type="Magic",
                    damage=[10,13],
                    value=100,
                    crit_chance=0.30,
                    crit_multiplier=1.5)