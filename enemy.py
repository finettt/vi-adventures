from live import LiveField
from obj_types import ObjTypes

class Enemy(LiveField):
    def __init__(self):
        super().__init__(1, 1, ObjTypes.ENEMY, 1, 0.5)
        self.load_surface("enemy.txt")
