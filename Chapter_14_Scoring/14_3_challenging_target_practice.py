### 14-3. Challenging Target Practice:

import sys
import pygame
import pygame.display
import pygame.event
import pygame.font
import pygame.image
import pygame.mouse
import pygame.sprite

class Settings:
    """Game parameters"""

    def __init__(self):
        """Construct settings"""

        # screen
        self.screen_width = 1920
        self.screen_height = 1080

        # game
        self.miss_threshold = 30
        self.hit_threshold = 3
        self.speedup_scale = 1.1

        # xwing
        self.xwing_speed = 6

        # bullet
        self.bullet_color = (255,0,0)
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_speed = 5

        # target
        self.target_color = (130,130,130)
        self.target_width = 20
        self.target_height = 250

        # text
        self.text_color = (255,255,255)

        # dynamic settings
        self.init_dynamic_settings()

    
    def init_dynamic_settings(self):
        """Set default values for some parameters"""
        self.target_speed = 0.5


    def increase_speed(self):
        """Make target faster"""
        self.target_speed *= self.speedup_scale



class GameStats:
    """Contain the live stats of the game"""

    def __init__(self, tp_game):
        """Construct unique game statistics"""
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Options which can be resetted at runtime"""
        self.target_miss = 0
        self.hit_count = 0



class Button:
    """Custom button class"""

    def __init__(self, tp_game, msg):
        """Create a button with custom text on the screen"""
        # screen and settings
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        # button params
        self.button_width, self.button_height = 200, 50
        self.button_color = (255,0,0)
        self.font = pygame.font.SysFont(None, 50)

        # button image
        self.rect = pygame.Rect((0,0), (self.button_width,self.button_height))
        self.rect.center = self.screen_rect.center

        # text image
        self.text_image = self.font.render(msg, True, self.settings.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.screen_rect.center

    
    def draw(self):
        """Draw the button on screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)



class Target:
    """Enemy on the right"""

    def __init__(self, tp_game):
        """Construct"""
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect((0,0), (self.settings.target_width,self.settings.target_height))
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        # Move down = 1; move up = -1
        self.direction = 1


    def draw(self):
        """Draw rectangle on screen"""
        self.screen.fill(self.settings.target_color, self.rect)

    
    def update(self):
        """Move target up and down until screen border"""
        # Screen edge is reached. Change direction
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            self.direction *= -1
        self.y += (self.settings.target_speed * self.direction)
        self.rect.y = self.y


    def center(self):
        """Place target at the initial place and direction to down"""
        self.rect.midright = self.screen_rect.midright
        self.y = self.rect.y
        # Move down
        self.direction = 1


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


    def center(self):
        """Place xwing in initial place"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y



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

        # misses counter
        self.font = pygame.font.SysFont(None, 50)
        self.misses = self.font.render(f"{self.game_stats.target_miss} {self.game_stats.hit_count}", True, self.settings.text_color)
        self.misses_rect = self.misses.get_rect()
        self.misses_rect.bottomleft = self.screen_rect.bottomleft

        # game
        self.game_active = False
        self.game_paused = False
        self.button_play = Button(self, "PLAY")
        self.button_pause = Button(self, "PAUSED")


    def run_game(self):
        """Main loop"""
        while True:
            self._check_events()
            if self.game_active and not self.game_paused:
                self._update_bullets()
                self.xwing.update()
                self.target.update()
            self._update_screen()
            print(self.settings.target_speed)


    def _check_events(self):
        """Respond to keypres and mouse click"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()
                self._check_pause_button()


    def _handle_keydown(self, event):
        """Handle keypress"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self.xwing.move_up = True
        elif event.key == pygame.K_s:
            self.xwing.move_down = True
        elif event.key == pygame.K_k:
            if not self.game_paused:
                self._fire_bullet() 
        elif event.key == pygame.K_r:
            self._start_game()
        elif event.key == pygame.K_p:
            if self.game_active:
                self.game_paused = not self.game_paused


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

        if not self.game_active:
            self.button_play.draw()

        if self.game_paused:
            self.button_pause.draw()

        self.misses = self.font.render(f"{self.game_stats.target_miss} {self.game_stats.hit_count}", True, self.settings.text_color)
        self.screen.blit(self.misses, self.misses_rect)

        # self.screen
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

                # Detect endgame condition
                if self.game_stats.target_miss >= self.settings.miss_threshold:
                    self.game_active = False

        self._check_bullet_target_collision()


    def _check_bullet_target_collision(self):
        """Detects hits and levelup"""
        while pygame.sprite.spritecollideany(self.target, self.bullets):
            self.bullets.remove(pygame.sprite.spritecollideany(self.target, self.bullets))
            self.game_stats.hit_count += 1
            self.settings.increase_speed()


    def _start_game(self):
        """Set all parameters to initial and change game flag"""
        self.settings.init_dynamic_settings()
        self.game_active = True
        self.game_paused = False
        self.game_stats.reset_stats()
        self.xwing.center()
        self.target.center()
        self.bullets.empty()


    def _check_play_button(self):
        """Checks if mouse clicks are on the play button"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = self.button_play.rect.collidepoint(mouse_pos)
        if mouse_clicked and not self.game_active:
            self._start_game()


    def _check_pause_button(self):
        """Resume paused game by button"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = self.button_pause.rect.collidepoint(mouse_pos)
        if mouse_clicked and self.game_paused :
            self.game_paused = not self.game_paused


if __name__ == "__main__":
    game = TargetPractice()
    game.run_game()