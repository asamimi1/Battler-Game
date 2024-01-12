import os
import time
import random
from character import *
from weapons import *
from levels import *
from enemies import *
from config import *

PAUSE_DURATION = 0.5

def get_random_enemy(level):
    enemies = level.enemies
    enemy = random.choice(enemies)
    enemy_weapon = random.choice(enemy.weapon)
    return enemy, enemy_weapon

def get_random_weapon(level, hero):
    available_weapons = [weapon for weapon in level.weapon_drops if weapon not in hero.inventory.items and weapon != hero.weapon]

    if available_weapons:
        random_weapon = random.choice(available_weapons)
        return random_weapon
    else:
        return None

def run_battle(hero, enemy):
    while hero.health > 0 and enemy.health > 0:
        clear_screen()

        hero.attack(enemy)
        enemy.attack(hero)

        hero.health_bar.draw()
        enemy.health_bar.draw()

        time.sleep(PAUSE_DURATION)

def display_stats(hero):
    return f"\n{colors['cyan']}({hero.name.title()} Stats: {hero.health_max} HP, {hero.strength} Strength, Weapon: {hero.weapon.name}: Damage: {hero.weapon.damage}, Type: {hero.weapon.weapon_type}, Crit Chance: {hero.weapon.crit_chance*10}%)){colors['reset']}"

def main():
    clear_screen()
    name = input("Hello, what is your name?\n[Please enter your name.]\n")
    if name.replace(" ", "") == "":
        name = "Hero"
    hero = Hero(name=name.title(), health=100, strength=5, weakness=[], resists=[])

    current_level = 0
    battle_counter = 0

    while current_level <= len(current_levels):
        clear_screen()
        level = get_level(current_level)
        stats = display_stats(hero)
        if battle_counter == 0:
            level_description = level.get_description(hero.name)
            input(f"{level_description}\n[Press Enter to continue]\n")
        clear_screen()

        hero.health = hero.health_max
        enemy, enemy_weapon = get_random_enemy(level)
        enemy = Enemy(name=enemy.name, health=enemy.health, weapon=enemy_weapon, strength=enemy.strength, weakness=list(enemy.weakness), resists=list(enemy.resists))

        if enemy.name[0] in ["a", "e", "i", "o", "u"]:
            article = "an"
        else:
            article = "a"

        user_input = input(f"{hero.name} encountered {article} {colors['red']}{enemy.name}{colors['reset']}: Health: {enemy.health}, Strength: {enemy.strength}, Weapon: {enemy.weapon.name} (Damage: {enemy.weapon.damage}, Type: {enemy.weapon.weapon_type}).{stats}\n[1. Open Inventory, 2. Continue]\n")

        if user_input == "1":
            hero.display_inventory()
            run_battle(hero, enemy)
        else:
            run_battle(hero, enemy)

        if hero.health > 0:
            replay = input(f"{colors['cyan']}{hero.name} defeated the {enemy.name}!{colors['reset']}\n[Press Enter to Continue]\n")
            clear_screen()

            random_weapon = get_random_weapon(level, hero)
            if random_weapon is not None:
                equip_weapon = input(f"{hero.name} found item: {random_weapon.name} (Damage: {random_weapon.damage}, Type: {random_weapon.weapon_type}, Crit Chance: {random_weapon.crit_chance*10}%). Would you like to add to inventory?\n{colors['cyan']}(Current Weapon is {hero.weapon.name}: Damage: {hero.weapon.damage}, Type: {hero.weapon.weapon_type}, Crit Chance: {hero.weapon.crit_chance*10}%){colors['reset']}\n['Yes' or 'No']\n")
                if equip_weapon.lower() in ["y", "yes", ""]:
                    hero.add_to_inventory(random_weapon)
                if replay.lower() not in ["y", "yes", ""]:
                    break

            battle_counter += 1
            if battle_counter == 3:
                clear_screen()
                hero.level_up()
                current_level += 1
                battle_counter = 0

        else:
            replay = input(f"GAME OVER! Try again?\n['Yes' or 'No']\n")
            if replay.lower() not in ["y", "yes", ""]:
                break
            else:
                hero.reset_to_default()
            current_level = 0
            battle_counter = 0

if __name__ == "__main__":
    main()