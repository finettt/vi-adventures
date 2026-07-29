from rogue import Rogue
from enemy import Enemy
import random
from goal import GoalManager
from room import Room
from portal import Portal
from friend import Friend
from chest import Chest
from helpers import *
import os
class Level():
    def __init__(self, screen, level_num):
        self.screen = screen
        self.player = Rogue()
        self.portal = Portal()
        self.friend = Friend()
        self.level_num = level_num
        is_zen = os.getenv("VIADV_ZEN_MODE", False)
        if not is_zen:
            self.is_lucky = level_num > 5 and random.randint(0,3)==3
        else:
            self.is_lucky = False
        self.room, room_pos = self.generate_room()
        room_size = (self.room.size_x, self.room.size_y)
        self.enemies = self.generate_enemies(room_size)
        self.chests = self.generate_chests(room_size)
        self.gm = GoalManager(len(self.enemies), len(self.chests))
        self.place_room(room_pos)
        if self.is_lucky:
            self.place_friend(room_pos, room_size)
        else:
         self.place_portal(room_pos, room_size)
        self.place_obj_in_room(self.player, room_pos, room_size)
        for enemy in self.enemies:
            self.place_obj_in_room(enemy, room_pos, room_size)

        for chest in self.chests:
            self.place_obj_in_room(chest, room_pos, room_size)

    def export_player_inventory(self):
        return self.player.inventory._get_items()

    def import_player_inventory(self, inventory):
        self.player.inventory._set_items(inventory)


    def get_chest_count(self, room_size):
        base_chest_count = 1/3000
        room_sqare = room_size[0]*room_size[1]
        chest_count = int(base_chest_count*room_sqare)
        return chest_count

    def generate_chests(self, room_size):
        chests_count = self.get_chest_count(room_size)
        chests = [Chest() for _ in range(chests_count)]
        return chests
        
    def get_enemy_count(self, room_size):
        base_enemy_count = 1/1000
        room_sqare = room_size[0]*room_size[1]
        level_bias = 1 + 0.05*self.level_num
        enemy_count = int(base_enemy_count*room_sqare*level_bias)
        random_delta = random.randint(0,2)
        return enemy_count + random_delta

    def generate_enemies(self, room_size):
        enemies_count = self.get_enemy_count(room_size)
        enemies = [Enemy() for _ in range(enemies_count)]
        return enemies
    def get_pos(self, uid):
        return self.screen.get_pos(uid)

    def generate_room(self):
        size = os.get_terminal_size()
        w = random.randint(int(0.75*size.columns), size.columns-1)
        h = random.randint(int(0.75*size.lines), size.lines-2)
        max_w, max_h = size.columns, size.lines
        cx, cy = (max_w-w)//2, (max_h-h)//2
        room = Room(w, h)
        return room, (cx, cy)
    def place_room(self, room_pos):
        self.screen.place(self.room, room_pos)
        

    def place_portal(self, room_pos, room_size):
        portal_pos = calculate_center_pos(room_pos[0], room_pos[1], room_size[0], room_size[1])
        self.screen.place(self.portal, portal_pos)
        self.screen.render()

    def place_friend(self, room_pos, room_size):
        friend_pos = calculate_center_pos(room_pos[0], room_pos[1], room_size[0], room_size[1])
        self.screen.place(self.friend, friend_pos)
        self.screen.render()

    def place_obj_in_room(self, obj, room_pos, room_size):
        obj_x = random.randint(room_pos[0]+1, room_pos[0]+room_size[0]-2)
        obj_y = random.randint(room_pos[1]+1, room_pos[1]+room_size[1]-2)
        while not self.screen.is_empty((obj_x, obj_y)):
            obj_x = random.randint(room_pos[0]+1, room_pos[0]+room_size[0]-2)
            obj_y = random.randint(room_pos[1]+1, room_pos[1]+room_size[1]-2)
        
        obj_pos = (obj_x, obj_y)
        
        self.screen.place(obj, obj_pos)
        self.screen.render()


    def render_level(self):
        self.screen.render()
        return self.screen.surface

    def get_player(self):
        return self.player

    def move_player(self, delta_pos):
        self.move_obj(self.player, delta_pos)

    def move_by_uid(self, uid, delta_pos):
        obj = self.screen.obj_manager.obj[uid]["obj"]
        self.move_obj(obj, delta_pos)

    def move_obj(self, obj, delta):
        self.screen.move_obj(obj, delta)

    def find_nearest(self, obj, exclude=[], include=[]):
        pos = self.screen.pos_manager.get_pos(obj.uid)
        return self.screen._find_nearest_pos(pos, exclude=exclude, include=include)

    def get_type_by_uid(self, uid):
        return self.screen.get_type_by_uid(uid)

    def open_chest(self, uid):
        self.screen.obj_manager.obj[uid]["obj"].activate_chest() 
        random_item = get_random_item()
        self.gm.register_chest() 
        self.player.add_to_inventory(random_item)
        return random_item
    def get_enemies_delta(self):
        deltas = {}
        for enemy in self.enemies:
            deltas[enemy.uid] = self.get_enemy_delta(enemy)
        return deltas

    def get_enemy_delta(self, enemy):
        enemy_pos = self.screen.pos_manager.get_pos(enemy.uid)
        player_pos = self.screen.pos_manager.get_pos(self.player.uid)
        unw_delta_x = player_pos[0]-enemy_pos[0]
        unw_delta_y = player_pos[1]-enemy_pos[1]
        def clamp(val):
            return max(-1, min(1, val))
        w_delta_x = clamp(unw_delta_x)
        w_delta_y = clamp(unw_delta_y)
        w_delta = (w_delta_x, w_delta_y)

        return w_delta

    def get_enemies(self):
        return self.enemies

    def damage_player(self, damage):
        self.player.hp -= damage

    def is_completed(self):
        return self.gm.is_goal_completed()
    
    def activate_portal(self):
        self.portal.activate_portal()
    def damage_enemy(self, enemy_uid, damage):
        obj = self.screen.obj_manager.obj[enemy_uid]["obj"]
        obj.hp-=damage
        if obj.hp<=0:
            self.screen.remove_obj(obj.uid)
            self.enemies.remove(obj)
            self.gm.register_kill()
