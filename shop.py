from config import *
from weapons import *
import math

class Shop():
    def __init__(self, max_capacity=MAX_CAPACITY):
        self.max_capacity = max_capacity
        self.items = []

    def get_weapons(self, hero, max_items=10):
        available_weapons = [weapon for weapon in vendor_items if weapon not in hero.inventory.items]
        return random.sample(available_weapons, min(max_items, len(available_weapons)))

    def buy_from_shop(self, hero):
        exit = f"{colors['cyan']}Exiting Buy Menu.{colors['reset']}\n[Press Enter to Continue]\n"
        clear_screen()
        print(f"{colors['yellow']}Shop Items:{colors['reset']}")

        random_items = self.get_weapons(hero)

        for num, item in enumerate(random_items, start=1):
            listed_value = math.ceil(item.value*1.25)
            lined_item = f" {num}. {item.name} (Damage: {item.damage}, Type: {item.weapon_type}, Crit Chance: {item.crit_chance*10}%, Value: {listed_value})"
            print(lined_item)

        user_input = input("Select an item to buy. '0' to exit.\n")

        if user_input.isdigit() and 1 <= (num := int(user_input)) <= len(random_items):
            clear_screen()
            item_to_buy = random_items[num - 1]

            if hero.gold >= item_to_buy.value:
                if len(hero.inventory.items) < hero.inventory.max_capacity:
                    input(f"{colors['cyan']}{hero.name} bought {item_to_buy.name} for {listed_value} gold.{colors['reset']}")
                    hero.gold -= listed_value
                    hero.add_to_inventory(item_to_buy)
                else:
                    input(f"{colors['red']}Inventory is Full! Cannot buy {item_to_buy.name}. Please sell an item.{colors['reset']}\n[Press Enter to Continue]\n")
            else:
                input(f"Not enough gold.\n[Press Enter to Continue]")
        else:
            input(exit)


    def sell_to_shop(self, hero):
        clear_screen()
        exit = f"{colors['cyan']}Exiting Sell Menu.{colors['reset']}\n[Press Enter to Continue]\n"

        if not hero.inventory.items:
            input("No items in Inventory.\n[Press Enter to Continue]\n")
            input(exit)
            return
        else:
            print(f"{colors['yellow']}Inventory:{colors['reset']}")
            for num, item in enumerate(hero.inventory.items, start=1):

                if item.name == hero.weapon.name:
                    equipped = f"{colors['yellow']}[EQUIPPED]{colors['reset']}"
                else:
                    equipped = ""

                lined_item=(f" {num}. {item.name} (Damage: {item.damage}, Type: {item.weapon_type}, Crit Chance: {item.crit_chance*10}%) {equipped}")
                print(lined_item)

        user_input = input("Select an item to buy. '0' to exit.\n")

        if user_input.isdigit() and 1 <= (num := int(user_input)) <= len(hero.inventory.items):
            clear_screen()
            item_to_sell = hero.inventory.items[num - 1]

            input(f"{colors['cyan']}{hero.name} sold {item_to_sell.name} for {item_to_sell.value} gold.{colors['reset']}")
            hero.gold += item_to_sell.value
            hero.remove_from_inventory(item_to_sell)

        else:
            input(exit)