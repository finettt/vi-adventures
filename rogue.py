from live import LiveField
from inventory import Inventory
from obj_types import ObjTypes
class Rogue(LiveField):
    def __init__(self):
        super().__init__(1, 1, ObjTypes.PLAYER, 5, 1)
        self.load_surface("rogue.txt")
        self.color = "\033[92m"
        self.inventory = Inventory()
        self.attack_range = 2
        self.max_step = 5
        self.max_enemies = 1
    def add_to_inventory(self, item):
        self.inventory._add_to_inventory(item)
    def get_items(self):
        return self.inventory._get_items()
    def get_items_counted(self):
        return self.inventory._get_items_counted()

