import pygame
import pygame.font
from pygame.sprite import Group

import settings
from ship import Ship

class Scoreboard:
    """Displays stats on screen"""

    def __init__(self, ai_game):
        """Construct scorebard"""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Font settings for score on screen
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self._prep_images()

    
    def _prep_images(self):
        """Render all scores"""
        # Prepare the initial score and high score and level
        self.prepare_score()
        self.prep_high_score()
        self.prep_level()

        # Construct initial live indicators
        self.prep_lives()
        
    
    def prepare_score(self):
        """Creates an image for score points"""
        # Display score as multiple of 10 but store internally the actual value
        rounded_score = round(self.stats.score,-1)
        # Display with coma separator for readability
        score_str = f"{rounded_score:,}"

        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Display score at the topright
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Update image for highscore"""
        # Round the highscore to a multiple of 10, and seperate with a comma for readability
        high_score_str = f"{round(self.stats.high_score, -1):,}"
        
        # Update the image with latest number
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        
        # Place it on the top of the screen in the middle
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_rect.top


    def prep_level(self):
        """Update image representing current level"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color)
        
        # Place level below score points
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right 
        self.level_rect.top = self.score_rect.bottom + 10 
    

    def prep_lives(self):
        """Create ships indicating remaining lives"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_remaining):
            new_ship = Ship(self.ai_game)
            # Place each live indicator 10px away from the previous
            new_ship.rect.x = 10 + new_ship.rect.width*ship_number
            new_ship.rect.y = 10
            self.ships.add(new_ship)

    
    def check_new_highscore(self):
        """Updates highscore when curren is bigger"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def draw_score(self):
        """Draw tall statuses on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        