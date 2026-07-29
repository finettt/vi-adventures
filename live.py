from field import Field
class LiveField(Field):
    def __init__(self, size_x, size_y, obj_type, hp=1, damage=1):
        super().__init__(1, 1, obj_type)
        self.hp = hp
        self.damage = damage
        self.attack_range = 1
