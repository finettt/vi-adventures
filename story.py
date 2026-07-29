class Story():
    def __init__(self, screen, path):
        self.screen = screen
        self.text = []
        with open(path, "r") as f:
            line = f.readline().rstrip()
            while line!="":
                self.text.append(line)
                line = f.readline().rstrip()

        screen._draw_centered(self.text) 
        self.surface = screen.surface
