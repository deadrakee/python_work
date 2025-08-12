from pathlib import Path
class GameStats:
    """Contains all game statistics"""

    def __init__(self, ai_game):
        """Construct the only instance of the class"""
        self.settings = ai_game.settings
        self._load_highscore()
        self.reset_stats()


    def reset_stats(self):
        """Parameters which can be returned to initial values at runtime"""
        self.ships_remaining = self.settings.ship_limit
        self.score = 0
        self.level = 0


    def _load_highscore(self):
        """Read high score from file and store it in program memory"""
        try:
            hs_path = Path("highscore.txt")
            self.high_score = int(hs_path.read_text())
        except FileNotFoundError:
            self.high_score = 0