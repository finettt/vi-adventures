import uuid

class Field():
    def __init__(self, size_x, size_y, obj_type):
        self.size_x = size_x
        self.size_y = size_y
        self.type = obj_type
        self.surface = []
        self.uid = str(uuid.uuid4()) 
        for i in range(self.size_y):
            self.surface.append(" " * self.size_x)
    def load_surface(self, surface_path):
        with open(surface_path, "r") as f:
            self.surface = []
            line = f.readline().rstrip()
            idx = 0
            while line!="" and idx < self.size_y:
                self.surface.append(line[:self.size_x])
                line = f.readline().strip()
                idx+=1
                


