### 13-4. Steady Rain:

import sys
import pygame
import random
from pygame.sprite import Sprite
from pygame.sprite import Group

class Settings:
    """Container for parameters of the game"""

    def __init__(self):
        """Construct the object"""
        self.fullscreen = True
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (95, 108, 130)
        self.randomize = True
        self.drop_speed = 1



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
        self.grid_x = 0
        self.grid_y = 0


    def blitme(self):
        """Draw the image on the screen"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Move the drop vertically"""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
        self.rect.x = self.x



class RainGame:
    """Class for game attributes"""

    def __init__(self):
        """Build the game"""
        self.run = True
        self.settings = Settings()

        # screen
        pygame.init()
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        
        self.screen_rect = self.screen.get_rect()
        self.screen.fill(self.settings.bg_color)

        # raindrops
        self.raindrops = Group()
        self._create_rain()

    def run_game(self):
        """Run main loop infinitely"""
        while self.run:
            self._check_events()
            self._update_raindrops()
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

    def _update_raindrops(self):
        """Check for expiring raindrops and update position"""
        self._check_drop_edges()
        self.raindrops.update()

    def _check_drop_edges(self):
        """If a rain drop exits the screen, create a new one on first row"""
        for drop in self.raindrops.sprites():
            if drop.rect.top >= self.settings.screen_height:
                # Return the drop just above the top of the screen
                drop.y = 0-drop.rect.height    
                # Set a new random X postition to avoid repetitive patterns
                # Use original grid X to avoid overlapping
                rand_x = 0
                if self.settings.randomize:
                    rand_x = random.randint(-20, 20)
                drop.x = drop.grid_x + rand_x

    # Variant with drop deletion. Drops spawn strangely on top
    # def _check_drop_edges(self):
    #     """If a rain drop exits the screen, create a new one on first row"""
    #     for drop in self.raindrops.copy():
    #         if drop.rect.top >= self.settings.screen_height:
    #             temp_x = drop.grid_x
    #             temp_y = 0-drop.rect.height
    #             self.raindrops.remove(drop)
    #             self._create_drop(temp_x, temp_y)

    def _create_rain(self):
        """Create all raindrops and place them on the screen"""
        single_drop = Raindrop(self)
        drop_rect = single_drop.rect

        current_x = drop_rect.width
        current_y = 0
        while current_y <= (self.screen_rect.height - (2*drop_rect.height)):
            while current_x <= (self.screen_rect.width - (2*drop_rect.width)):
                self._create_drop(current_x, current_y)
                current_x += drop_rect.width*3 
            current_y += drop_rect.height*3 
            current_x = drop_rect.width            


    def _create_drop(self, x, y):
        """Create a raindrop object at a position and add it to the group"""
        drop = Raindrop(self)
        drop.grid_x = x
        drop.grid_y = y
        # Create a random offset of the raindrops if enabled
        if self.settings.randomize:
            x += random.randint(-20, 20)
            y += random.randint(-20, 20)
        drop.x = x
        drop.y = y
        drop.rect.x = x
        drop.rect.y = y
        self.raindrops.add(drop) 

    

if __name__ == "__main__":
    while True:
        rain_game = RainGame()
        rain_game.run_game()