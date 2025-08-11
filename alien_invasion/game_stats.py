class GameStats:
    """Contains all game statistics"""

    def __init__(self, ai_game):
        """Construct the only instance of the class"""
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Parameters which can be returned to initial values at runtime"""
        self.ships_remaining = self.settings.ship_limit
        self.score = 0