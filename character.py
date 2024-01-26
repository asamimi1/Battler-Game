from weapons import *
from health_bar import *
from inventory import Inventory
from shop import *
from config import *

class Character:

    def __init__(self, name: str, health: int, strength: int, weakness: list, resists: list) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = DEFAULT_PLAYER_WEAPON
        self.strength = strength
        self.weakness = weakness
        self.resists = resists
        self.inventory = Inventory()

    def attack(self, target) -> None:
        is_critical = random.random() < self.weapon.crit_chance
        base_damage = self.weapon.calculate_damage() + self.strength
        damage_dealt = base_damage * self.weapon.crit_multiplier if is_critical else base_damage
        initial_damage = damage_dealt
        modifier = ""

        if self.weapon.weapon_type in target.weakness:
            damage_dealt *= 1.25
            modifier = (f"\033[92m({round(damage_dealt-initial_damage)} vulnerability damage)\033[0m")

        if self.weapon.weapon_type in target.resists:
            damage_dealt *= 0.75
            modifier = (f"\033[91m({round(initial_damage-damage_dealt)} damage resisted)\033[0m")

        target.health -= damage_dealt
        target.health = max(target.health, 0)
        target.health_bar.update()

        if is_critical:
            print(f"\033[93mCRITICAL HIT!\033[0m {self.name} dealt {round(damage_dealt)} damage" + modifier + f" to {target.name} with {self.weapon.name}!")
        else:
            print(f"{self.name} dealt {round(damage_dealt)} damage to {target.name}" + modifier + f" with {self.weapon.name}!")

class Hero(Character):

    def __init__(self, name: str, health: int, strength: int, weakness: list, resists: list, gold: int) -> None:
        super().__init__(name=name, health=health, strength=strength, weakness=weakness, resists=resists)

        self.default_weapon = self.weapon
        self.default_strength = strength
        self.default_health = health
        self.health_bar = HealthBar(self, color="green")
        self.default_gold = gold
        self.gold = gold
        self.shop = Shop()
        
    def add_to_inventory(self, item):
        while True:
            if len(self.inventory.items) < self.inventory.max_capacity and item not in self.inventory.items:
                self.inventory.items.append(item)
                input(f"{colors['cyan']}{item.name} added to inventory!{colors['reset']}\n[Press Enter to Continue]\n")
                break
            else:
                user_input = input(f"Inventory Full. Please drop or sell an item.\n[1. Open Inventory, 2. Continue]\n")
                if user_input == "1":
                    self.inventory.display_inventory(self)
                else:
                    break

    def remove_from_inventory(self, item):
        if item == self.weapon:
            self.drop()
        return self.inventory.remove_from_inventory(item)

    def display_inventory(self):
        self.inventory.display_inventory(self)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        input(f"{colors['cyan']}{self.name} equipped {self.weapon.name}!{colors['reset']}\n[Press Enter to Continue]\n")

    def drop(self) -> None:
        input(f"{colors['red']}{self.name} dropped {self.weapon.name}!{colors['reset']}\n[Press Enter to Continue]\n")
        self.weapon = self.default_weapon

    def level_up(self) -> None:
        self.strength += 2
        self.health_max += 15
        input(f"{self.name} \033[93mleveled up!\033[0m You gained +15 HP +2 Strength!\n[Press Enter to Continue]\n")

    def open_shop(self):
        while True:
            clear_screen()
            print(f"{colors['cyan']}Welcome to the shop, {self.name}!{colors['reset']}")
            print(f"{colors['yellow']}Gold: {self.gold}{colors['reset']}")

            choice = input("[1. Buy Items, 2. Sell Items, 0. Exit]\n")

            if choice == "1":
                self.shop.buy_from_shop(self)
            elif choice == "2":
                self.shop.sell_to_shop(self)
            else:
                input(f"{colors['cyan']}Exiting Shop.{colors['reset']}\n[Press Enter to Continue]\n")
                break

    def reset_to_default(self) -> None:
        self.health = self.default_health
        self.health_max = self.default_health
        self.weapon = self.default_weapon
        self.strength = self.default_strength
        self.inventory.reset_inventory()
        self.gold = self.default_gold

class Enemy(Character):
    
    def __init__(self, name: str, health: int, weapon, strength: int, weakness: list, resists: list, gold: list, boss: bool) -> None:
        super().__init__(name=name, health=health, strength=strength, weakness=weakness, resists=resists)
        self.weapon = weapon
        self.strength = strength
        self.weakness = weakness
        self.resists = resists
        self.health_bar = HealthBar(self, color="red")
        self.gold = gold
        self.boss = boss
