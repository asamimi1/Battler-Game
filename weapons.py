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
        

# Enemy Specific Weapons

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

fire_breath = Weapon(name="Fire Breath",
                    weapon_type="Magic",
                    damage=[10,13],
                    value=100,
                    crit_chance=0.30,
                    crit_multiplier=1.5)

# Enemy and Level Weapons

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

war_pick = Weapon(name="War Pick",
                    weapon_type="Sharp",
                    damage=[6,9],
                    value=10,
                    crit_chance=0.15,
                    crit_multiplier=1.7)

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

battle_axe = Weapon(name="Battle Axe",
                    weapon_type="Sharp",
                    damage=[8,11],
                    value=14,
                    crit_chance=0.25,
                    crit_multiplier=1.8)

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

curved_sword = Weapon(name="Curved Sword",
                    weapon_type="Sharp",
                    damage=[7,10],
                    value=15,
                    crit_chance=0.35,
                    crit_multiplier=1.5)

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

# Vendor Specific Weapons

battle_hammer = Weapon(name="Battle Hammer",
                    weapon_type="Blunt",
                    damage=[9,12],
                    value=22,
                    crit_chance=0.22,
                    crit_multiplier=1.3)

steel_fists = Weapon(name="Steel Fists",
                    weapon_type="Blunt",
                    damage=[10,12],
                    value=23,
                    crit_chance=0.26,
                    crit_multiplier=1.6)

pistol = Weapon(name="Pistol",
                    weapon_type="Ranged",
                    damage=[9,11],
                    value=20,
                    crit_chance=0.3,
                    crit_multiplier=1.5)

crossbow = Weapon(name="Crossbow",
                    weapon_type="Ranged",
                    damage=[10,12],
                    value=19,
                    crit_chance=0.23,
                    crit_multiplier=1.3)

sickle = Weapon(name="Sickle",
                    weapon_type="Sharp",
                    damage=[12,14],
                    value=25,
                    crit_chance=0.18,
                    crit_multiplier=1.8)

dragon_slayer_sword = Weapon(name="Dragon Slayer Sword",
                    weapon_type="Sharp",
                    damage=[15,18],
                    value=50,
                    crit_chance=0.25,
                    crit_multiplier=1.3)


vendor_items = [iron_sword, fire_wand, ice_staff, great_sword, daggers, pike, short_bow, long_bow, mace, flail, barbarian_axe, curved_sword, spiked_mace, void_scepter, battle_hammer, steel_fists, pistol, crossbow, sickle, dragon_slayer_sword]