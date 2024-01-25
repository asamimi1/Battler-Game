import os
import time
import random
from character import *
from weapons import *
from levels import *
from enemies import *
from config import *

def get_random_enemy(level):
    enemies = level.enemies
    enemy = random.choice(enemies)
    enemy_weapon = random.choice(enemy.weapon)
    dropped_gold = random.choice(enemy.gold)
    return enemy, enemy_weapon, dropped_gold

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
    return f"\n{colors['cyan']}{hero.name.title()} Stats:{colors['reset']}\n Health: {hero.health_max}\n Strength: {hero.strength}\n Weapon: {hero.weapon.name} (Damage: {hero.weapon.damage}, Type: {hero.weapon.weapon_type}, Crit Chance: {hero.weapon.crit_chance*10}%)\n{colors['yellow']}Gold: {hero.gold}{colors['reset']}"

def main():
    clear_screen()
    name = input("Hello, what is your name?\n[Please enter your name.]\n")
    if name.replace(" ", "") == "":
        name = "Hero"
    hero = Hero(name=name.title(), health=DEFAULT_PLAYER_HEALTH, strength=DEFAULT_PLAYER_STRENGTH, weakness=[], resists=[], gold=DEFAULT_GOLD)

    current_level = 0
    battle_counter = 0

    while current_level <= len(current_levels):
        clear_screen()
        level = get_level(current_level)
        stats = display_stats(hero)
        if battle_counter == 0:
            level_description = level.get_description(hero.name)
            user_input = input(f"{level_description}\nWould you like to access shop?\n[1. Open Shop, 2. Continue]\n")

            if user_input == "1":
                hero.open_shop()

        clear_screen()

        hero.health = hero.health_max
        enemy, enemy_weapon, dropped_gold = get_random_enemy(level)
        enemy = Enemy(name=enemy.name, health=enemy.health, weapon=enemy_weapon, strength=enemy.strength, weakness=list(enemy.weakness), resists=list(enemy.resists), gold=dropped_gold, boss=bool(enemy.boss))

        if enemy.name[0] in ["a", "e", "i", "o", "u"]:
            article = "an"
        else:
            article = "a"

        enemy_stats = f"\n{colors['red']}{enemy.name} Stats:{colors['reset']}\n Health: {enemy.health}\n Strength: {enemy.strength}\n Weapon: {enemy.weapon.name} (Damage: {enemy.weapon.damage}, Type: {enemy.weapon.weapon_type})."
        user_input = input(f"{hero.name} encountered {article} {colors['red']}{enemy.name}{colors['reset']}:{enemy_stats}{stats}\n[1. Open Inventory, 2. Continue]\n")

        if user_input == "1":
            hero.display_inventory()

        run_battle(hero, enemy)

        if hero.health > 0:
            replay = input(f"{colors['cyan']}{hero.name} defeated the {enemy.name}! {colors['yellow']}{enemy.gold} gold added to inventory!\n{colors['reset']}[Press Enter to Continue]\n")
            hero.gold += enemy.gold
            clear_screen()

            random_weapon = get_random_weapon(level, hero)
            if random_weapon is not None:
                equip_weapon = input(f"{hero.name} found item: {random_weapon.name} (Damage: {random_weapon.damage}, Type: {random_weapon.weapon_type}, Crit Chance: {random_weapon.crit_chance*10}%). Would you like to add to inventory?\n{colors['cyan']}Current Weapon is {hero.weapon.name}: Damage: {hero.weapon.damage}, Type: {hero.weapon.weapon_type}, Crit Chance: {hero.weapon.crit_chance*10}%{colors['reset']}\n['Yes' or 'No']\n")
                if equip_weapon.lower() in ["y", "yes", ""]:
                    hero.add_to_inventory(random_weapon)
                if replay.lower() not in ["y", "yes", ""]:
                    break

            if enemy.boss == True: # Check if enemy is boss
                input(f"{colors['green']}YOU WIN!{colors['reset']} Play again?\n[Press Enter to Continue]\n")
                hero.reset_to_default()
                current_level = 0
                battle_counter = 0
                
            else:
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