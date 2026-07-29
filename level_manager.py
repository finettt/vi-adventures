from level import Level
class LevelManager():
    def __init__(self, screen_manager):
        self.levels = {}
        self.sm = screen_manager
        self.level_num = 0
    def generate_level(self, screen_uid=None):
        if screen_uid:
            screen = self.sm.get_screen_by_uid(screen_uid)
            level = Level(screen, self.level_num)
            self.levels[screen_uid] = level
        else:
            screen_uid = self.sm_create_screen()
            screen = self.sm.get_screen_by_uid(screen_uid)
            level = Level(screen, self.level_num)
            self.levels[screen_uid] = level
        self.level_num+=1
        return screen_uid


    def get_level_by_uid(self, uid):
        return self.levels[uid]
