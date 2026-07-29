from interactive import InteractiveField
from obj_types import ObjTypes

class Chest(InteractiveField):
    def __init__(self):
        super().__init__(1,1, ObjTypes.CHEST)
        self.load_surface("chest.txt")
        self.activated = False
    def activate_chest(self):
        self.activated = True
        self.surface = "_"
