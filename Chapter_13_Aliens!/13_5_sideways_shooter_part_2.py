### 13-5. Sideways Shooter Part 2:

import sys
import pygame
import pygame.image
import pygame.sprite
import random

class Settings:
    """Global options of the game"""

    def __init__(self):
        """Construct initial parameters"""
        # screen
        self.screen_width = 1920
        self.screen_height = 1080
        self.fullscreen = False
        self.bg_color = (230, 230, 230)

        # ship
        self.ship_speed = 10

        # bullet
        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_speed = 9
        self.bullet_color = (0, 0, 0)
        self.autoshoot_cd = 30

        # jokers
        self.joker_spawn_cd = 50
        self.joker_speed = 3



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
        self.rect.midleft = self.screen_rect.midleft

        # location
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False

    
    def blitme(self):
        """Draw ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move ship up and down"""
        if self.move_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y



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
        self.settings = Settings()
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

        # ship
        self.ship = Ship(self)

        # bullets
        self.bullets = pygame.sprite.Group()
        self.autoshoot = False
        self.autoshoot_cd = 0

        # jokers
        self.jokers = pygame.sprite.Group()
        self.joker_spawn_cd = 0


    def run_game(self):
        """Main loop of the game"""

        while True:
            self._check_events()
            self.ship.update()
            self._spawn_joker()
            self.jokers.update()
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
        elif key == pygame.K_e:
            print("all bullets")
            for joker in self.jokers.sprites():
                print(joker.rect)



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
        pygame.sprite.groupcollide(
            self.bullets, self.jokers, True, True)


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
            y = random.randint(0, self.screen_rect.height-temp_joker.rect.height)
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


    # def _crash_ship(self):
    #     """Detect if a joker collides with the ship"""
    #     for joker in self.jokers:
    #         if pygame.sprite.collide_rect()

if __name__ == "__main__":
    bs_game = BatmanShooter()
    bs_game.run_game()