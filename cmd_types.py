from enum import Enum

class CmdTypes(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    INTERACT = 5
    QUIT = 6
    ATTACK = 7
    LIST_INVENTORY = 8
