from weapons import *
from character import *
from health_bar import *

class EnemyType():
    def __init__(self, name: str, health: int, strength: int, weapon: list, resists: list, weakness: list) -> None:
        self.name = name
        self.strength = strength
        self.health = health
        self.weapon = weapon
        self.resists = resists
        self.weakness = weakness

boar = EnemyType(name="Boar",
                    health=60,
                    strength=3,
                    resists=[],
                    weakness=["Sharp", "Ranged"],
                    weapon=[claws])

goblin = EnemyType(name="Goblin",
                    health=75,
                    strength=4,
                    resists=["Blunt"],
                    weakness=["Sharp"],
                    weapon=[fists, bronze_sword, iron_sword])

giant_rat = EnemyType(name="Giant Rat",
                    health=145,
                    strength=5,
                    resists=[],
                    weakness=["Sharp", "Ranged"],
                    weapon=[claws])
        
skeleton = EnemyType(name="Skeleton",
                    health=125,
                    strength=3,
                    resists=["Sharp", "Ranged", "Magic"],
                    weakness=["Blunt"],
                    weapon=[short_bow, flail, mace])

orc = EnemyType(name="Orc",
                    health=145,
                    strength=6,
                    resists=["Blunt"],
                    weakness=["Ranged"],
                    weapon=[long_bow, mace, iron_sword, great_sword])

wolf = EnemyType(name="Wolf",
                    health=130,
                    strength=10,
                    resists=["Blunt"],
                    weakness=["Sharp", "Ranged"],
                    weapon=[claws])

giant_ooze = EnemyType(name="Giant Ooze",
                    health=150,
                    strength=11,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    weapon=[spit])

giant_spider = EnemyType(name="Giant Spider",
                    health=135,
                    strength=14,
                    resists=["Blunt"],
                    weakness=["Sharp", "Magic"],
                    weapon=[claws])

swamp_zombie = EnemyType(name="Swamp Zombie",
                    health=125,
                    strength=12,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    weapon=[pike, great_sword, long_bow])

knight = EnemyType(name="Knight",
                    health=150,
                    strength=14,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    weapon=[spiked_mace, barbarian_axe])

dark_wizard = EnemyType(name="Dark Wizard",
                    health=115,
                    strength=18,
                    resists=["Magic"],
                    weakness=["Sharp", "Ranged"],
                    weapon=[ice_staff, void_scepter])

dragon = EnemyType(name="Dragon",
                    health=300,
                    strength=10,
                    resists=["Blunt", "Ranged", "Magic"],
                    weakness=[],
                    weapon=[fire_breath])