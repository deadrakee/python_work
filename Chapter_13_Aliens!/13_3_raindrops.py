### 13-3. Raindrops:

import sys
import pygame
import random
from pygame.sprite import Sprite
from pygame.sprite import Group

class Raindrop(Sprite):
    """Class representig a single raindrop"""

    def __init__(self, rain_game):
        """Create a drop sprite"""
        super().__init__()
        self.settings = rain_game.settings
        self.screen = rain_game.screen
        self.image = pygame.image.load("tiny_drop.png")
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        """Draw the image on the screen"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Move the drop vertically"""
        self.y += self.settings.drop_speed
        self.rect.y = self.y



class Settings:
    """Container for parameters of the game"""

    def __init__(self):
        """Construct the object"""
        self.bg_color = (95, 108, 130)
        self.randomize = True
        self.drop_speed = 1



class RainGame:
    """Class for game attributes"""

    def __init__(self):
        """Build the game"""
        self.run = True
        self.settings = Settings()

        # screen
        pygame.init()
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen_rect = self.screen.get_rect()
        self.screen.fill(self.settings.bg_color)

        # raindrops
        self.raindrops = Group()
        self._create_rain()

    def run_game(self):
        """Run main loop infinitely"""
        while self.run:
            self._check_events()
            self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.run = False

    def _update_screen(self):
        """Draw everything on the screen"""
        self.screen.fill(self.settings.bg_color)
        # Draw all raindrops
        self.raindrops.draw(self.screen)

        pygame.display.flip()

    def _create_rain(self):
        """Create all raindrops and place them on the screen"""
        single_drop = Raindrop(self)
        drop_rect = single_drop.rect

        current_x = drop_rect.width
        current_y = drop_rect.height
        while current_y <= (self.screen_rect.height - (2*drop_rect.height)):
            while current_x <= (self.screen_rect.width - (2*drop_rect.width)):
                self._create_drop(current_x, current_y)
                current_x += drop_rect.width*3 
            current_y += drop_rect.height*3 
            current_x = drop_rect.width             


    def _create_drop(self, x, y):
        """Create a raindrop object at a position and add it to the group"""
        # Create a random offset of the raindrops if enabled
        if self.settings.randomize:
            x += random.randint(-20, 20)
            y += random.randint(-20, 20)

        drop = Raindrop(self)
        drop.x = x
        drop.y = y
        drop.rect.x = x
        drop.rect.y = y
        self.raindrops.add(drop) 

    

if __name__ == "__main__":
    while True:
        rain_game = RainGame()
        rain_game.run_game()