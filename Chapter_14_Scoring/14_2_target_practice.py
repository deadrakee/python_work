### 14-2. Target Practice:

from re import S
from shutil import move
import sys
from matplotlib.pyplot import flag
import py
import pygame
import pygame.display
import pygame.event
import pygame.image
import pygame.sprite
from tables import Group

class Settings:
    """Game parameters"""

    def __init__(self):
        """Construct settings"""

        # screen
        self.screen_width = 1920
        self.screen_height = 1080

        # xwing
        self.xwing_speed = 5

        # bullet
        self.bullet_color = (255,0,0)
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_speed = 4

        # target
        self.target_color = (130,130,130)
        self.target_width = 20
        self.target_height = 250
        self.target_speed = 4
        


class GameStats:
    """Contain the live stats of the game"""

    def __init__(self, tp_game):
        """Construct unique game statistics"""
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Options which can be resetted at runtime"""
        self.target_miss = 0



class Target:
    """Enemy on the right"""

    def __init__(self, tp_game):
        """Construct"""
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect((0,0), (self.settings.target_width,self.settings.target_height))
        self.rect.midright = self.screen_rect.midright
        self.x = float(self.rect.x)


    def draw(self):
        """Draw rectangle on screen"""
        self.screen.fill(self.settings.target_color, self.rect)



class Bullet(pygame.sprite.Sprite):
    """Sprite class for bullets"""

    def __init__(self, tp_game):
        super().__init__()
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.xwing_rect = tp_game.xwing.rect

        self.rect = pygame.Rect((0,0), (self.settings.bullet_width,self.settings.bullet_height))
        self.x = float(self.rect.x)


    def update(self):
        """Move bullet accross the screen"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x


    def draw(self):
        """Draw rectangle on screen"""
        self.screen.fill(self.settings.bullet_color, self.rect)


class Xwing:
    """Ship class"""

    def __init__(self, tp_game):
        """Construct ship"""
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load and place image
        self.image = pygame.image.load("x_wing.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False


    def update(self):
        """Move the xwing"""
        if self.move_up and self.y >= 0:
            self.y -= self.settings.xwing_speed

        if self.move_down and self.y <= self.settings.screen_height-self.rect.height:
            self.y += self.settings.xwing_speed

        self.rect.y = self.y

    
    def blitme(self):
        """Draw Xwing on screen"""
        self.screen.blit(self.image, self.rect)



class TargetPractice:
    """Game class"""

    def __init__(self):
        """Construct initial parameters"""
        self.settings = Settings()
        self.game_stats = GameStats(self)
        pygame.init()

        # screen
        pygame.display.set_caption("Target Practice")
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        
        # xwing
        self.xwing = Xwing(self)

        # bullets
        self.bullets = pygame.sprite.Group()

        # target
        self.target = Target(self)


    def run_game(self):
        """Main loop"""
        while True:
            self._check_events()
            self._update_bullets()
            self.xwing.update()
            self._update_screen()
            print(len(self.bullets.sprites()))


    def _check_events(self):
        """Respond to keypres and mouse click"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)


    def _handle_keydown(self, event):
        """Handle keypress"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self.xwing.move_up = True
        elif event.key == pygame.K_s:
            self.xwing.move_down = True
        elif event.key == pygame.K_k:
            self._fire_bullet() 


    def _handle_keyup(self, event):
        """Handle key release"""
        if event.key == pygame.K_w:
            self.xwing.move_up = False
        elif event.key == pygame.K_s:
            self.xwing.move_down = False


    def _update_screen(self):
        """Draw everything on the screen"""
        self.screen.fill((0,0,0))


        for bullet in self.bullets.sprites():
            bullet.draw()

        self.xwing.blitme()

        self.target.draw()

        pygame.display.flip()


    def _fire_bullet(self):
        """Create new bullet"""
        new_bullet = Bullet(self)
        new_bullet.rect.midright = self.xwing.rect.midright
        new_bullet.x = new_bullet.rect.x
        self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Move all bullets accros the screen and delete the expired"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
                # Count missing the target
                self.game_stats.target_miss += 1

        self._check_bullet_target_collision()


    def _check_bullet_target_collision(self):
        """Detects hits"""
        while pygame.sprite.spritecollideany(self.target, self.bullets):
            self.bullets.remove(pygame.sprite.spritecollideany(self.target, self.bullets))


# TODO
# Make target move
# add game active flag
# detect when target_miss > 3
# stop and restart game

if __name__ == "__main__":
    game = TargetPractice()
    game.run_game()