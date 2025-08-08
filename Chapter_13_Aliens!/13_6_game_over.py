### 13-6. Game Over:

import sys
import pygame
import pygame.image
import pygame.sprite
import pygame.font
import random

from time import sleep

class Settings:
    """Global options of the game"""

    def __init__(self):
        """Construct initial parameters"""
        # screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.fullscreen = True
        self.bg_color = (230, 230, 230)

        # status bar
        self.status_bar_width = self.screen_width
        self.status_bar_height = 50
        self.status_bar_color = (0, 0, 0)
        self.status_bar_li_spacing = 10
        self.status_bar_ji_color = (255, 255, 255)

        # active field
        self.field_height = self.screen_height-self.status_bar_height

        # ship
        self.ship_speed = 10
        self.ship_lifes = 3

        # bullet
        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_speed = 9
        self.bullet_color = (0, 0, 0)
        self.autoshoot_cd = 30

        # jokers
        self.joker_spawn_cd = 50
        self.joker_speed = 5



class GameStats:
    """Contain the live stats of the game"""

    def __init__(self, bs_game):
        """Construct unique game statistics"""
        self.settings = bs_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Options which can be resetted at runtime"""
        self.remaining_ships = 3
        self.jokers_shot = 0


class LifeIndicator(pygame.sprite.Sprite):
    """Sprite for batlogo life indicator on status bar"""

    def __init__(self):
        """Construct a sprite object"""
        super().__init__()
        self.image = pygame.image.load("batlogo_small.png")
        self.rect = self.image.get_rect()


class StatusBar():
    """Field at the bottom of the screen to show HUD elements"""

    def __init__(self, bs_game):
        """Create a solid color bar on the bottom of the screen"""
        # screen parameters
        self.settings = bs_game.settings
        self.game_stats = bs_game.game_stats
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen_rect

        # status bar parameters
        self.surface = pygame.Surface(
            (self.settings.status_bar_width, self.settings.status_bar_height))
        self.surface.fill(self.settings.status_bar_color)
        self.rect = self.surface.get_rect()
        self.rect.bottom = self.screen_rect.bottom

        # life indicators
        self.life_indicators = pygame.sprite.Group()
        self._create_life_indicators()

        # jokers shot
        self._place_joker_indicator()
        self._place_joker_indicator_counter()


    def _create_life_indicators(self):
        """Place initial life indicators on status bar"""
        # This object is just to get image width and height
        meas_li = LifeIndicator()

        # Coordinates of sprite are based on status bar size not on screen size
        current_x = self.settings.status_bar_li_spacing
        # Center on the status bar
        current_y = (self.rect.height - meas_li.rect.height) / 2

        # Place initial life counters next to each other with a little spacing
        for _ in range(self.settings.ship_lifes):
            new_li = LifeIndicator()
            new_li.rect.x = current_x
            new_li.rect.y = current_y
            self.life_indicators.add(new_li)
            current_x += meas_li.rect.width + self.settings.status_bar_li_spacing


    def _place_joker_indicator(self):
        """Place the static jokers shot indicator on the status bar"""
        self.joker_ind_image = pygame.image.load("small_joker_craft.png")
        self.joker_ind_rect = self.joker_ind_image.get_rect()

        # Place on the right side of the status bar
        self.joker_ind_rect.x = self.rect.width / 2
        # Center on the status bar
        self.joker_ind_rect.y = (self.rect.height - self.joker_ind_rect.height) / 2


    def _place_joker_indicator_counter(self):
        """Place number of shot jokers next to the static indicator"""
        self.font = pygame.font.SysFont(None, 50)
        self.ji_count = self.font.render(f" - {self.game_stats.jokers_shot}", True, self.settings.status_bar_ji_color)
        self.ji_count_rect = self.ji_count.get_rect()

        # Offset the shots count right next to the indicator
        self.ji_count_rect.x = self.joker_ind_rect.x + self.joker_ind_rect.width
        self.ji_count_rect.y = self.joker_ind_rect.y


    def draw(self):
        """Draw everything on status bar then blit it on screen """
        # Fill the status bar with solid color
        self.surface.fill(self.settings.status_bar_color)

        # Draw remaining life indicators
        self.life_indicators.draw(self.surface)
        
        # Draw joker indicator
        self.surface.blit(self.joker_ind_image, self.joker_ind_rect)

        # Render new number and draw jokers shot count next to the indicator
        self.ji_count = self.font.render(f" - {self.game_stats.jokers_shot}", True, self.settings.status_bar_ji_color)
        self.surface.blit(self.ji_count, self.ji_count_rect)
        
        # Draw the composed status bar on the screeen
        self.screen.blit(self.surface, self.rect)     
        


class Ship:
    """Class for main character"""

    def __init__(self, bs_game):
        """Construct the ship"""
        # screen and settings
        self.settings = bs_game.settings
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen_rect

        # create and place
        self.image = pygame.image.load("logo_sideways_bat_rocket.png")
        self.rect = self.image.get_rect()
        self.reset_ship()

    
    def blitme(self):
        """Draw ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move ship up and down"""
        if self.move_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom <= self.settings.field_height:
            self.y += self.settings.ship_speed

        self.rect.y = self.y


    def reset_ship(self):
        """Place in original position and stop ongoing movement"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False


class Bullet(pygame.sprite.Sprite):
    """Sprite class for bullets"""

    def __init__(self, bs_game):
        """Call superclass constructor and init params"""
        super().__init__()
        self.settings = bs_game.settings
        self.screen = bs_game.screen
        self.ship_rect = bs_game.ship.rect
        self.color = bs_game.settings.bullet_color

        # create a bullet rect at (0, 0) and them move to ship position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = self.ship_rect.midright

        # always store current x as float for precise current position
        self.x = float(self.rect.x)

    def draw_bullet(self):
        """Fill a rectangle with color and place it on screen surface"""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def update(self):
        """Move current bullet across the screen"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x



class Joker(pygame.sprite.Sprite):
    """The enemy class, part of a group"""

    def __init__(self, bs_game):
        """Construct a single joker sprite and place it on screen"""
        super().__init__()
        self.settings = bs_game.settings
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen_rect

        self.image = pygame.image.load("joker_craft.png")
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """Move the jokers to batman"""
        self.x -= self.settings.joker_speed
        self.rect.x = self.x


class BatmanShooter:
    """The game class"""

    def __init__(self):
        """Init basic game elements"""
        # settings and game stats
        self.settings = Settings()
        self.game_stats = GameStats(self)

        pygame.init()
        self.clock = pygame.time.Clock()

        # screen
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.screen_rect = self.screen.get_rect()
            self.settings.screen_height = self.screen_rect.height
            self.settings.screen_width = self.screen_rect.width
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            self.screen_rect = self.screen.get_rect()

        # status bar
        self.settings.status_bar_width = self.screen_rect.width
        self.status_bar = StatusBar(self)

        # active field
        self.settings.field_height = self.settings.screen_height-self.settings.status_bar_height

        # ship
        self.ship = Ship(self)

        # bullets
        self.bullets = pygame.sprite.Group()
        self.autoshoot = False
        self.autoshoot_cd = 0

        # jokers
        self.jokers = pygame.sprite.Group()
        self.joker_spawn_cd = 0

        self.game_active = True


    def run_game(self):
        """Main loop of the game"""

        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._spawn_joker()
                self._update_jokers()
                self._autoshoot_bullets()
                self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Detects keydown and keyup events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._respond_keydown_event(event.key)
            elif event.type == pygame.KEYUP:
                self._respond_keyup_event(event.key)


    def _respond_keydown_event(self, key):
        """Takes action when keydown event happened"""
        if key == pygame.K_q:
            sys.exit()
        elif key == pygame.K_w:
            self.ship.move_up = True
        elif key == pygame.K_s:
            self.ship.move_down = True
        elif key == pygame.K_SPACE:
            self._create_bullet()
            self.autoshoot = True
            self.autoshoot_cd = self.settings.autoshoot_cd


    def _respond_keyup_event(self, key):
        """Takes action when key is released"""
        if key == pygame.K_w:
            self.ship.move_up = False
        elif key == pygame.K_s:
            self.ship.move_down = False
        elif key == pygame.K_SPACE:
            self.autoshoot = False


    def _update_screen(self):
        """Draw everything on the screen"""
        # Recolor the bg during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draw the status bar
        self.status_bar.draw()
        
        # Draw the ship
        self.ship.blitme()

        # Draw all Joker ships
        self.jokers.draw(self.screen)

        # Draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _create_bullet(self):
        """Add a new bullet to the group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Move all bullets accros the screen and delete the expired"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_bullet_joker_collision()


    def _check_bullet_joker_collision(self):
        """Delete joker and bullet when they collide"""
        if pygame.sprite.groupcollide(
            self.bullets, self.jokers, True, True):
            self.game_stats.jokers_shot += 1


    def _autoshoot_bullets(self):
        """Fire at stady rate when SPACE is pressed"""
        # Create new bullet after cooldown has expired
        if self.autoshoot and self.autoshoot_cd == 0:
            self._create_bullet()
            self.autoshoot_cd = self.settings.autoshoot_cd
        
        if self.autoshoot_cd > 0:
            self.autoshoot_cd -= 1


    def _make_rand_coordinates(self):
        """Generate unique random coordinates for joker spawning"""
        is_overlapping = True
        temp_joker = Joker(self)
        attempts = 0

        # Generate coordinates until a free space is found
        while is_overlapping and attempts<10:
            # Make sure they are in the right side of the screen
            x = random.randint(
                self.screen_rect.centerx, self.screen_rect.width-temp_joker.rect.width)
            y = random.randint(0, self.settings.field_height-temp_joker.rect.height)
            temp_joker.rect.x = x
            temp_joker.rect.y = y

            # Check if another joker is already in that space
            collison_detected = False
            for joker in self.jokers:
                if pygame.sprite.collide_rect(temp_joker, joker):
                    collison_detected = True
            if not collison_detected:
                return (x, y)
            else:
                attempts += 1
    

    def _spawn_joker(self):
        """Create joker on a random place"""

        if self.joker_spawn_cd == 0:
            new_joker = Joker(self)
            try:
                x, y = self._make_rand_coordinates()
            except TypeError:
                pass
            else:
                new_joker.x = x
                new_joker.y = y
                new_joker.rect.x = x
                new_joker.rect.y = y
                self.jokers.add(new_joker)

            # Start cooldown timer
            self.joker_spawn_cd = self.settings.joker_spawn_cd

        if self.joker_spawn_cd > 0:
            self.joker_spawn_cd -= 1


    def _update_jokers(self):
        """Move all jokers, detect ship collisions and detect escapes"""
        self.jokers.update()

        if pygame.sprite.spritecollideany(self.ship, self.jokers):
            self._ship_hit()

        # Treat any joker out of the screen as a ship collision
        for joker in self.jokers.sprites():
            if joker.rect.right <= 0:
                self._ship_hit()
                break


    def _ship_hit(self):
        """Respond to collisions between a joker and the batship"""
        if self.game_stats.remaining_ships > 1:

            # clear screen and pause game
            self.jokers.empty()
            self.bullets.empty()
            sleep(0.5)

            # clear events and reset movement
            pygame.event.clear()
            self.ship.reset_ship()
        else:
            self.game_active = False

        # reduce ships left and remove them from status bar
        self.game_stats.remaining_ships -= 1
        for li in self.status_bar.life_indicators.sprites():
            # Iterate until the last life indicator (the one on the most right)
            temp_li = li
        self.status_bar.life_indicators.remove(temp_li)



if __name__ == "__main__":
    bs_game = BatmanShooter()
    bs_game.run_game()