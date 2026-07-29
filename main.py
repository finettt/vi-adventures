import time
import random
from screen_manager import ScreenManager
from story import Story
from print_manager import PrintManager
from obj_types import ObjTypes
from game import GameManager
from portal import Portal
from room import Room
from rogue import Rogue
from helpers import *

def main():
    surface = game.render_game()
    pm.update_surface(surface)
    pm.print_all()
    state = game.game_step()
    return state

if __name__ == "__main__":
    skip_lore = os.getenv("VIADV_SKIP_LORE", False)
    level_num = int(os.getenv("VIADV_FORCE_LEVEL", 0))
    state = int(os.getenv("VIADV_FORCE_STATE", 0))
    game = GameManager()
    game.lm.level_num = level_num
    game.generate_level()
    pm = PrintManager()
    if not skip_lore:
        for i in range(1,6):
            screen_uid = game.sm.create_screen()
            screen = game.sm.get_screen_by_uid(screen_uid)
            story = Story(screen, f"chapter{i}.txt")
            pm.update_surface(story.surface)
            pm.print_all()
            n = input()
            if n=="q":
                exit(0)
            clear_screen()
            pm.print_all()
            game.sm.delete_screen(screen_uid)
    while state!=2:
        state = main()
        if state == 1:
            break
        time.sleep(1/24)
        clear_screen()

    if state==1:
        screen_uid = game.sm.create_screen()
        screen = game.sm.get_screen_by_uid(screen_uid)
        story = Story(screen, "chapter6.txt")
        pm.update_surface(story.surface)
        pm.print_all()
    elif state == 2:
        size = os.get_terminal_size()
        base_line = "V  i"
        _current_base_line = base_line
        surface = [_current_base_line]
        for i in range(60):
            screen_uid = game.sm.create_screen()
            screen = game.sm.get_screen_by_uid(screen_uid) 
            screen._draw_centered(surface)
            pm.update_surface(screen.surface)
            pm.print_all()
            for idx in range(len(surface)):
                surface[idx] = surface[idx].swapcase()
            if i>8 and i%4 == 0 and len(surface)+2<size.lines:
                surface.append("")
                surface.append(_current_base_line) 
            if i>8 and i%4 == 0 and len(_current_base_line)+1+len(base_line)<size.columns:
                _current_base_line+=f"  {base_line}"
                for idx in range(len(surface)):
                    if surface[idx]!="":
                        surface[idx]=_current_base_line
            time.sleep(1/2)
            clear_screen()
        surface = ["Author: finett"]
        screen_uid = game.sm.create_screen()
        screen = game.sm.get_screen_by_uid(screen_uid) 
        screen._draw_centered(surface)
        pm.update_surface(screen.surface)
        pm.print_all()
        input()
