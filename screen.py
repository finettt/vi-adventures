from field import Field
from pos_manager import PosManager
from obj_manager import ObjManager
from obj_types import ObjTypes
from helpers import *
import os

def insert_at_line(line, text, text_len, text_pos):
        line_start = line[:text_pos]
        line_end = line[text_pos+text_len:]
        return "".join(line_start)+text+"".join(line_end)


class Screen(Field):
    def __init__(self):
        size = os.get_terminal_size()
        self.pos_manager = PosManager()
        self.obj_manager = ObjManager()
        super().__init__(size.columns, size.lines-1, ObjTypes.SCREEN)
    
    def _draw_at_pos_line(self, text, pos, color):
        colored_text = f"{color}{text}{reset_color}"
        self.surface[pos[0]] = insert_at_line(self.surface[pos[0]], text, len(text), pos[1])

    def _draw_at_pos(self, text, pos, color):
        for i, line in enumerate(text):
            line_pos = (
                pos[1]+i,
                pos[0]
            )
            self._draw_at_pos_line(line, line_pos, color)

    #deprecated
    def _draw_centered_line(self, text):
        text_size = len(text)
        text_pos = (
            size.lines // 2,
            (size.columns - text_size) // 2
        )
        self._draw_at_pos(self.surface, text, text_pos)
         
    def _draw_centered(self, text):
        size = get_size(self)
        text_lines = len(text)
        for i, line in enumerate(text):
            text_line_len= len(line)
            line_pos = (
                (size.lines - text_lines) // 2 + i,
                (size.columns - text_line_len) // 2 
            )    
            self._draw_at_pos_line(line, line_pos, "")
    def place(self, obj, pos):
        self.pos_manager.add_obj(obj, pos)
        self.obj_manager.add_obj(obj)

    def clear_screen(self):
        self.surface = []
        for i in range(self.size_y):
            self.surface.append(" "*self.size_x)


    def render(self):
        self.clear_screen()
        for obj in self.obj_manager.get_all_objects():
            surface = obj.surface
            uid = obj.uid
            pos = self.pos_manager.get_pos(uid)
            if hasattr(obj, "color"):
                color = obj.color
            else:
                color = ""
            self._draw_at_pos(surface, pos, color)

    def is_empty(self, pos):
        return self.surface[pos[1]][pos[0]] == " "

    def move_obj(self, obj, delta_pos): 
        full_pos = relative_to_full(self.pos_manager.get_pos(obj.uid), delta_pos)
        if self.is_empty(full_pos):
            self.pos_manager.move_obj_delta(obj.uid, delta_pos)
        else:
            pass

    def interact_obj(self, player, interacteble):
        if self.manager.can_interact(player.uid, interacteble.uid):
            return interacteble.interact()
    
    def _find_nearest_pos(self, pos, exclude=[ObjTypes.PLAYER], include=[]):
        dists = {}
        for obj in self.obj_manager.get_all_objects():
            obj_type = self.get_type_by_uid(obj.uid)
            if obj_type in exclude:
                continue
            
            if include!=[] and obj_type not in include:
                continue

            dist = calculate_distance(pos, self.pos_manager.get_pos(obj.uid))
            dists[dist] = obj.uid

        uid = None
        if dists.keys():
            nearest = min(dists.keys(), key=float)
            uid = dists[nearest]
        return uid

    #Retranslation for upper levels
    def get_type_by_uid(self, uid):
        return self.obj_manager.get_type_by_uid(uid)

    def get_pos(self, uid):
        return self.pos_manager.get_pos(uid)

    def remove_obj(self, uid):
        self.obj_manager.remove_obj(uid)
        self.pos_manager.remove_obj(uid)
