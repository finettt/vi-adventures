from screen_manager import ScreenManager
from level_manager import LevelManager
from input_manager import InputManager
from cmd_types import CmdTypes
from obj_types import ObjTypes
from level import Level
from helpers import *
class GameManager():
    def __init__(self):
        self.sm = ScreenManager()
        self.lm = LevelManager(self.sm)
        self.im = InputManager()
        self.inventory = []

    def generate_level(self):
        screen_uid = self.sm.create_screen()
        screen = self.sm.get_screen_by_uid(screen_uid)
        self.lm.generate_level(screen_uid)
        level = self.lm.get_level_by_uid(screen_uid) 
        self.player = level.get_player()
        level.import_player_inventory(self.inventory)
        for item in self.inventory:
            match item:
                case ItemTypes.SWORD:
                    self.player.damage+=0.5
                case ItemTypes.ROSE:
                    self.player.hp+=1
                case ItemTypes.BOOTS:
                    self.player.max_step+=1
                case ItemTypes.LONG_SWORD:
                    self.player.max_enemies+=1
                    self.player.attack_range+=1
        self.im.update_hp(self.player.hp)
        self.current_level = level

    def render_game(self):
        return self.current_level.render_level() 

    def game_step(self):
        # Ask user command, check what is this command, move player/interact/quit, thats all
        iters, cmd = self.im.get_cmd()
        self.im.update_info("")
        delta_pos = (0,0)
        match cmd:
            case CmdTypes.MOVE_UP:
                delta_pos = (0, -1)
            case CmdTypes.MOVE_DOWN:
                delta_pos = (0, 1)
            case CmdTypes.MOVE_LEFT:
                delta_pos = (-1, 0)
            case CmdTypes.MOVE_RIGHT:
                delta_pos = (1, 0)
            case CmdTypes.QUIT:
                exit(0)
            case CmdTypes.INTERACT:
                nearest_uid = self.current_level.find_nearest(self.player, exclude=[ObjTypes.PLAYER])
                nearest_type = self.current_level.get_type_by_uid(nearest_uid)
                nearest_pos = self.current_level.get_pos(nearest_uid)
                player_pos = self.current_level.get_pos(self.player.uid)
                nearest_dist = calculate_distance(player_pos, nearest_pos)
                match nearest_type:
                    case ObjTypes.PORTAL:
                        if nearest_dist <= 1 and self.current_level.is_completed():
                            self.inventory = self.current_level.export_player_inventory()
                            self.generate_level()
                    case ObjTypes.CHEST:
                        if nearest_dist <= 1:
                            item = self.current_level.open_chest(nearest_uid)
                            self.im.update_info(f"You find {item_to_text(item)}")
                    case ObjTypes.FRIEND:
                        if nearest_dist <= 1:
                            return 2
            case CmdTypes.ATTACK:
                for i in range(self.player.max_enemies):
                    nearest_uid = self.current_level.find_nearest(self.player, [ObjTypes.PLAYER], [ObjTypes.ENEMY])
                    if nearest_uid:
                        nearest_pos = self.current_level.get_pos(nearest_uid)
                        player_pos = self.current_level.get_pos(self.player.uid)
                        nearest_dist = calculate_distance(player_pos, nearest_pos)
                        if nearest_dist <= self.player.attack_range:
                            self.current_level.damage_enemy(nearest_uid, self.player.damage)
            case CmdTypes.LIST_INVENTORY:
                item_counted = self.player.inventory._get_items_counted()
                inventory_string = []
                for item_type, item_count in item_counted.items():
                    item_name = item_to_text(item_type)
                    inventory_string.append(item_name)
                    inventory_string.append(f"x{item_count}")
                self.im.update_info(f"{' '.join(inventory_string)}")

            case _:
                self.im.update_info(f"Unknown command: {cmd}")
        # Moving player
        for i in range(min(iters, self.player.max_step)):
            self.current_level.move_player(delta_pos)
        # Moving delta
        
        player_pos = self.current_level.get_pos(self.player.uid)

        enemies_deltas = self.current_level.get_enemies_delta()
        for enemy, delta in enemies_deltas.items():
            enemy_pos = self.current_level.get_pos(enemy)
            dist = calculate_distance(player_pos, enemy_pos)
            if dist>1 and dist<5:
                self.current_level.move_by_uid(enemy, delta)
            
        #Calculating enemies damage
        for enemy in self.current_level.get_enemies():
            enemy_pos = self.current_level.get_pos(enemy.uid)
            
            dist = calculate_distance(player_pos, enemy_pos)
            if dist <= enemy.attack_range:
                self.current_level.damage_player(enemy.damage)

        if self.player.hp <= 0:
            return 1

        self.im.update_hp(self.player.hp)

        if self.current_level.is_completed():
           self.current_level.activate_portal()

        return 0
