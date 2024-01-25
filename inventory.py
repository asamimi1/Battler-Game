from character import *
from config import *


class Inventory():
    def __init__ (self, max_capacity=MAX_CAPACITY):
        self.max_capacity = max_capacity
        self.items = []

    def add_item(self, item):
            self.items.append(item)
            input(f"{colors['cyan']}{item.name} added to inventory!{colors['reset']}\n[Press Enter to Continue]\n")
                    
        
    def remove_from_inventory(self, item):
        if item in self.items:
            self.items.remove(item)
            input(f"{colors['cyan']}{item.name} removed from inventory!{colors['reset']}\n[Press Enter to Continue]\n")
            return True
        else:
            return False
        
    def display_inventory(self, hero):
        exit = f"{colors['cyan']}Exiting Inventory.{colors['reset']}\n[Press Enter to Continue]\n"
        while True:
            clear_screen()
            if not self.items:
                input("No items in Inventory.\n[Press Enter to Continue]\n")
                input(exit)
                break
            else:
                print(f"{colors['yellow']}Inventory:{colors['reset']}")
                for num, item in enumerate(self.items, start=1):

                    if item.name == hero.weapon.name:
                        equipped = f"{colors['yellow']}[EQUIPPED]{colors['reset']}"
                    else:
                        equipped = ""

                    lined_item=(f" {num}. {item.name} (Damage: {item.damage}, Type: {item.weapon_type}, Crit Chance: {item.crit_chance*10}%) {equipped}")
                    print(lined_item)

                user_input = input("Select weapon for settings? '0' to exit.\n")

                match user_input:
                    case "0":
                        input(exit)
                        break
                    case str(num)  if user_input.isdigit() and (num := int(user_input)) in range(1, len(self.items) + 1):
                        clear_screen()
                        item_listed = self.items[num - 1]
                        lined_item = f"{colors['yellow']}Item:\n {colors['reset']}{item_listed.name} (Damage: {item_listed.damage}, Type: {item_listed.weapon_type}, Crit Chance: {item_listed.crit_chance*10}%) {equipped}"
                        weapon_input = input(f"{lined_item}\n[Press '1' to equip weapon, '2' to drop weapon, press '0' to exit.]\n")
                        match weapon_input:
                            case "1":
                                hero.equip(self.items[num - 1])
                            case "2":
                                hero.remove_from_inventory(self.items[num - 1])
                    case _:
                        input(exit)
                        break

    def reset_inventory(self):
        self.items = []