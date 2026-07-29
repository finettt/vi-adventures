from interactive import InteractiveField
from obj_types import ObjTypes

class Portal(InteractiveField):
    def __init__(self):
        super().__init__(1,1, ObjTypes.PORTAL) 
        self.load_surface("portal.txt")
        self.activated = False
    def activate_portal(self):
        self.activated = True
        self.surface = "@"
