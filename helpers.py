import math
import random
import re
from dataclasses import dataclass
from item_types import ItemTypes
import os
import platform

@dataclass
class Size:
    lines: int
    columns: int

def get_size(obj):
    return Size(obj.size_y, obj.size_x)

def clear_screen():
    is_windows = platform.system() == "Windows"
    is_linux = platform.system() == "Linux"

    if is_windows:
        os.system("cls")
    elif is_linux:
        os.system("clear")

def relative_to_full(pos, delta):
    return (pos[0]+delta[0], pos[1]+delta[1])

def generate_room_surface(w,h):
    if w<4 or h<4:
        return
    surface = []
    surface.append("█"*w)
    for _ in range(h-2):
        string="█"+" "*(w-2)+"█"
        surface.append(string)
    surface.append("█"*w)

    return surface 

def calculate_distance(pos1, pos2):
    delta_x = pos1[0]-pos2[0]
    delta_y = pos1[1]-pos2[1]
    distance = math.sqrt(delta_x**2+delta_y**2)
    return distance

def calculate_center_pos(x, y, w, h):
    cx = x + w//2
    cy = y + h//2
    return (cx,cy)

def parse_string(s):
    # Pattern explanation:
    # (\d+)?      -> Group 1: Optional one or more digits at the start.
    # ([a-zA-Z]+) -> Group 2: One or more letters following the number (or just letters).
    
    match = re.match(r'(\d+)?([a-zA-Z]+)', s)
    
    if not match:
        # Instead of raising an error, return defaults as requested
        final_num = 1
        letter_str = ""
    else:
        num_str = match.group(1)
        letter_str = match.group(2)
        final_num = int(num_str) if num_str else 1

    return final_num, letter_str

def get_random_item():
    items = [ItemTypes.SWORD, ItemTypes.BOOTS, ItemTypes.ROSE, ItemTypes.LONG_SWORD]
    random_item = random.choice(items)
    return random_item

def item_to_text(item_type):
    match item_type:
        case ItemTypes.SWORD:
            return "sword"
        case ItemTypes.BOOTS:
            return "boots"
        case ItemTypes.ROSE:
            return "rose"
        case ItemTypes.LONG_SWORD:
            return "longsword"
reset_color = "\033[0m"
