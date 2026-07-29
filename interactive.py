from field import Field

class InteractiveField(Field):
    def __init__(self, w, h, obj_types):
        super().__init__(w, h, obj_types)
        self.deactivated_color = ""
        self.activated_color = ""

    def interact(self):
        pass
