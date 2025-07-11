import sys
import pygame
import pygame.display
import pygame.event
import pygame.time

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class containing all game assets"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self._screen_mode()
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(ai_game=self)

    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()
            self.ship.move()
            self._update_screen()
            # Next line aligns that the loop runs 60 times per second
            # 60 frames are rendered in a single second (60FPS)
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Process the keydowns"""
        if event.key == pygame.K_RIGHT:
            self.ship.r_direction.start_moving()
        elif event.key == pygame.K_LEFT:
            self.ship.l_direction.start_moving()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Process key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.r_direction.stop_moving()
        elif event.key == pygame.K_LEFT:
            self.ship.l_direction.stop_moving()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Recolor the bg during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _screen_mode(self):
        """Run in window or fullscreen mode depending on Settings"""
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.scree_width, self.settings.scree_height))
            


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()