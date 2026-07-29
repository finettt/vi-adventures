from field import Field
from helpers import *
from obj_types import ObjTypes
class Room(Field):
    def __init__(self, width, height):
        super().__init__(width,height, ObjTypes.ROOM)
        self.surface = generate_room_surface(width,height)
