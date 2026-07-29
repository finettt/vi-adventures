class GoalManager():
    def __init__(self, enemy_count, chest_count):
        self.enemy_count = enemy_count
        self.chest_count = chest_count
        self.killed_enemies = 0
        self.opened_chests = 0
    def _update_killed(self, delta):
        self.killed_enemies += delta
    def _update_chest(self, delta):
        self.opened_chests += delta
    def register_kill(self):
        self._update_killed(1)
    def register_chest(self):
        self._update_chest(1)
    def is_goal_completed(self):
        return self.killed_enemies >= self.enemy_count and self.opened_chests >= self.chest_count
