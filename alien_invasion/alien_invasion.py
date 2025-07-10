import sys
import pygame
import pygame.display
import pygame.event
import pygame.time
import random

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class containing all game assets"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.scree_width, self.settings.scree_height))
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(ai_game=self)

    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()
            self._update_screen()
            # Next line aligns that the loop runs 60 times per second
            # 60 frames are rendered in a single second (60FPS)
            self.clock.tick(60)


    def change_bg_color_randomly(self):
        """Changes the background with a random color"""
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.settings.bg_color = (r, g, b)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Recolor the bg during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()