class PrintManager():
    def __init__(self):
        self.surface = []
    def update_surface(self, new_surface):
        self.surface = new_surface
    def print_all(self):
        for line in self.surface:
            print("".join(line))
