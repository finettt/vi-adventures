from interactive import InteractiveField
from obj_types import ObjTypes

class Friend(InteractiveField):
    def __init__(self):
        super().__init__(1, 1, ObjTypes.FRIEND)
        self.load_surface("i.txt")
