import pygame
import pygame.font


class Scoreboard:
    """Displays stats on screen"""

    def __init__(self, ai_game):
        """Construct scorebard"""
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Font settings for score on screen
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prepare_score()
        
    
    def prepare_score(self):
        """Creates an image for score points"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Display score at the topright
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    
    def draw_score(self):
        """Draw the score image on screen"""
        self.screen.blit(self.score_image, self.score_rect)