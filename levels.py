from weapons import *
from enemies import *
from character import Hero
from config import *

class Level:
    def __init__(self, name: str, enemies: list, weapon_drops: list, description: str):
        self.name = name
        self.enemies = enemies
        self.weapon_drops = weapon_drops
        self.description = description

    def get_description(self, player_name):
        return self.description.format(player_name=player_name)

level1 = Level(name="Forest", enemies=[goblin, boar], weapon_drops=[iron_sword, short_bow, mace], description="{player_name} stumbles upon a "+colors['yellow']+"Forest"+colors['reset']+". Whispers are heard among the trees. {player_name} moves towards the sounds.")
level2 = Level(name="Cave", enemies=[skeleton, giant_rat], weapon_drops=[flail, long_bow], description="{player_name} sees a "+colors['yellow']+"Cave"+colors['reset']+" ahead. {player_name} runs in for shelter.")
level3 = Level(name="Plains", enemies=[orc, wolf], weapon_drops=[great_sword, daggers, fire_wand], description="{player_name} finds a path leading out and discovers the "+colors['yellow']+"Plains"+colors['reset']+". {player_name} ventures forward.")
level4 = Level(name="Swamp", enemies=[giant_ooze, giant_spider, swamp_zombie], weapon_drops=[pike, ice_staff], description="{player_name} discovers a "+colors['yellow']+"Swamp"+colors['reset']+" ahead. Smells foul!")
level5 = Level(name="Castle", enemies=[knight, dark_wizard], weapon_drops=[barbarian_axe, spiked_mace, void_scepter], description="{player_name} sees a "+colors['yellow']+"Castle"+colors['reset']+" upon the hill. {player_name} moves towards it.")
level6 = Level(name="Dragon's Lair", enemies=[dragon], weapon_drops=[], description="{player_name} hears a roar. Ahead is "+colors['yellow']+"The Dragon's Lair"+colors['reset']+". {player_name} readies their weapon.")

current_levels = [level1, level2, level3, level4, level5, level6]

def get_level(level_number):
    return current_levels[level_number]