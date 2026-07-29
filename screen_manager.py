from screen import Screen
class ScreenManager():
    def __init__(self):
        self.screens = {}
    def get_screen_by_uid(self, uid):
        return self.screens[uid]
    def add_screen(self,screen):
        self.screens[screen.uid] = screen
    def create_screen(self):
        screen = Screen()
        self.add_screen(screen)
        return screen.uid
    def delete_screen(self, uid):
        del self.screens[uid]
