import os
from weapons import *

PAUSE_DURATION = 0.5
MAX_CAPACITY = 5
DEFAULT_PLAYER_HEALTH = 100
DEFAULT_PLAYER_STRENGTH = 5
DEFAULT_PLAYER_WEAPON = bronze_sword
DEFAULT_GOLD = 0
MAX_COUNTER = 3

colors = {
    'reset': '\033[0m',
    'black': '\033[30m',
    'red': '\033[91m',
    'green': '\033[32m',
    'green2': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')