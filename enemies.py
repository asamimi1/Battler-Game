from weapons import *
from character import *
from health_bar import *

class EnemyType():
    def __init__(self, name: str, health: int, strength: int, weapon: list, resists: list, gold: list, weakness: list, boss: bool) -> None:
        self.name = name
        self.strength = strength
        self.health = health
        self.weapon = weapon
        self.resists = resists
        self.weakness = weakness
        self.gold = gold
        self.boss = boss

#Forest Enemies
        
boar = EnemyType(name="Boar",
                    boss = False,
                    health=60,
                    strength=3,
                    resists=[],
                    weakness=["Sharp", "Ranged"],
                    gold = [3, 5],
                    weapon=[claws])

goblin = EnemyType(name="Goblin",
                    boss = False,
                    health=75,
                    strength=4,
                    resists=["Blunt"],
                    weakness=["Sharp"],
                    gold = [4, 6],
                    weapon=[fists, bronze_sword])

bandit = EnemyType(name="Bandit",
                    boss = False,
                    health=80,
                    strength=3,
                    resists=[""],
                    weakness=["Sharp", "Ranged"],
                    gold = [4, 6],
                    weapon=[bronze_sword])

#Cave Enemies

giant_rat = EnemyType(name="Giant Rat",
                    boss = False,
                    health=145,
                    strength=5,
                    resists=[],
                    weakness=["Sharp", "Ranged"],
                    gold = [5, 7],
                    weapon=[claws])

bat = EnemyType(name="Bat",
                    boss = False,
                    health=120,
                    strength=6,
                    resists=[],
                    weakness=["Sharp", "Ranged", "Magic"],
                    gold = [5, 7],
                    weapon=[claws])
        
skeleton = EnemyType(name="Skeleton",
                    boss = False,
                    health=125,
                    strength=3,
                    resists=["Sharp", "Ranged", "Magic"],
                    weakness=["Blunt"],
                    gold = [6, 8],
                    weapon=[short_bow, flail, mace])

#Plains Enemies

orc = EnemyType(name="Orc",
                    boss = False,
                    health=145,
                    strength=6,
                    resists=["Blunt"],
                    weakness=["Ranged"],
                    gold = [8, 10],
                    weapon=[long_bow, mace, iron_sword, great_sword])

wolf = EnemyType(name="Wolf",
                    boss = False,
                    health=130,
                    strength=10,
                    resists=["Blunt"],
                    weakness=["Sharp", "Ranged"],
                    gold = [7, 9],
                    weapon=[claws])

troll = EnemyType(name="Troll",
                    boss = False,
                    health=150,
                    strength=8,
                    resists=["Sharp"],
                    weakness=["Magic", "Ranged"],
                    gold = [9, 11],
                    weapon=[war_pick, great_sword])

#Swamp Enemies

giant_ooze = EnemyType(name="Giant Ooze",
                    boss = False,
                    health=150,
                    strength=11,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    gold = [9, 12],
                    weapon=[spit])

giant_spider = EnemyType(name="Giant Spider",
                    boss = False,
                    health=135,
                    strength=14,
                    resists=["Blunt"],
                    weakness=["Sharp", "Magic"],
                    gold = [8, 11],
                    weapon=[claws])

swamp_zombie = EnemyType(name="Swamp Zombie",
                    boss = False,
                    health=125,
                    strength=12,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    gold = [10, 12],
                    weapon=[pike, long_bow, battle_axe])

#Castle Enemies

knight = EnemyType(name="Knight",
                    boss = False,
                    health=150,
                    strength=14,
                    resists=["Sharp", "Ranged"],
                    weakness=["Blunt", "Magic"],
                    gold = [12, 14],
                    weapon=[spiked_mace, barbarian_axe])

dark_wizard = EnemyType(name="Dark Wizard",
                    boss = False,
                    health=115,
                    strength=18,
                    resists=["Magic"],
                    weakness=["Sharp", "Ranged"],
                    gold = [11, 13],
                    weapon=[ice_staff, void_scepter])

armored_soldier = EnemyType(name="Armored Soldier",
                    boss = False,
                    health=160,
                    strength=13,
                    resists=["Magic", "Sharp"],
                    weakness=["Blunt"],
                    gold = [11, 13],
                    weapon=[curved_sword, spiked_mace])

#Final Boss

dragon = EnemyType(name="Dragon",
                    boss = True,
                    health=300,
                    strength=10,
                    resists=["Blunt", "Ranged", "Magic"],
                    weakness=[],
                    gold = [50],
                    weapon=[fire_breath])