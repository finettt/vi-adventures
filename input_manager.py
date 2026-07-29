from cmd_types import CmdTypes
from helpers import *
class InputManager():
    def __init__(self, hp = 5):
        self.hp = hp
        self.info = ""
        self.prompt = f"{self.info}{' ' *bool(self.info)}HP:{self.hp} | :"
    
    def update_hp(self, new_hp):
        self.hp = new_hp 
        self.prompt = f"{self.info}{' '*bool(self.info)}HP:{self.hp} | :"
    def update_info(self, new_info):
        self.info = new_info
        self.prompt = f"{self.info}{' '*bool(self.info)}HP:{self.hp} | :"
    def get_cmd(self):
        cmd = self._get_cmd()
        return self._parse_cmd(cmd)
    def _get_cmd(self):
        return input(self.prompt)
    def _parse_cmd(self, cmd):
        iters, cmd = parse_string(cmd)
        parsed_cmd = ""
        match cmd:
            case "h":
                parsed_cmd = CmdTypes.MOVE_LEFT
            case "l":
                parsed_cmd = CmdTypes.MOVE_RIGHT
            case "j":
                parsed_cmd = CmdTypes.MOVE_DOWN
            case "k":
                parsed_cmd = CmdTypes.MOVE_UP
            case "q":
                parsed_cmd = CmdTypes.QUIT
            case "e":
                parsed_cmd = CmdTypes.INTERACT
            case "a":
                parsed_cmd = CmdTypes.ATTACK
            case "i":
                parsed_cmd = CmdTypes.LIST_INVENTORY
            case _:
                parsed_cmd = cmd
        return iters, parsed_cmd
