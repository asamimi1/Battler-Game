from config import *

class Shop():
    def __init__ (self, max_capacity=MAX_CAPACITY):
        self.max_capacity = max_capacity
        self.items = []