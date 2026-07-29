class PosManager:
    def __init__(self):
        self.pos = {}
    def add_obj(self, obj, pos):
       self.pos[obj.uid] = tuple(pos)
    def _replace_obj(self, uid, pos):
        self.pos[uid] = tuple(pos)
    def move_obj_delta(self, uid, delta_pos):
        pos = self.pos[uid]
        new_pos = [ pos[0]+delta_pos[0], pos[1]+delta_pos[1] ]
        self._replace_obj(uid,new_pos)
    def get_pos(self, uid):
        return tuple(self.pos[uid])
    def can_interact(self, uid1, uid2):
        return abs(get_pos(uid1)[0]-get_pos(uid2)[0]) <= 1 and abs(get_pos(uid1)[1]-get_pos(uid2)[1])
    def remove_obj(self, uid):
        del self.pos[uid]
