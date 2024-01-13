import os

PAUSE_DURATION = 0.5
MAX_CAPACITY = 5

gold = 0

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