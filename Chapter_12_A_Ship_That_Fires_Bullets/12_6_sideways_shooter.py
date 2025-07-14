### 12-6. Sideways Shooter:

import sys
import pygame
import pygame.display
import pygame.draw
import pygame.event
import pygame.image
import pygame.sprite

# bullets container
bullets = pygame.sprite.Group()
# global rocket surface
rocket_surface = pygame.image.load('sideways_bat_rocket.png')
rocket_rect = rocket_surface.get_rect()

class Keys:
    """Container for all keypresses"""

    def __init__(self):
        """Build all keys unpressed initially"""
        self.up_pressed = False
        self.down_pressed = False


class Bullet(pygame.sprite.Sprite):
    """Contains rect and sprite for bullet"""

    def __init__(self, rocket_rect):
        """Build bullet on rocket coordinates and init Sprite"""
        super().__init__()
        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.midright = rocket_rect.midright

    def update(self, speed):
        """Move bullet horizontally"""
        self.rect.x += speed


def check_events(keys):
    """Monitors for all events"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown_event(event, keys)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event, keys)

def handle_keydown_event(event, keys):
    """Handles keypress"""
    if event.key == pygame.K_UP:
        keys.up_pressed = True
    elif event.key == pygame.K_DOWN:
        keys.down_pressed = True
    elif event.key == pygame.K_SPACE:
        fire_bullet()
    elif event.key == pygame.K_q:
        sys.exit()
    print(f"KeyDown - {event.key}")

def handle_keyup_event(event, keys):
    """Handles release of a key"""
    if event.key == pygame.K_UP:
        keys.up_pressed = False
    elif event.key == pygame.K_DOWN:
        keys.down_pressed = False
    print(f"KeyUp - {event.key}")

def move_rocket(keys, rocket_rect, screen_rect, speed):
    """move rocket depending on pressed key"""
    if keys.up_pressed and rocket_rect.top > 0:
        rocket_rect.y -= speed
    if keys.down_pressed and rocket_rect.bottom < screen_rect.bottom:
        rocket_rect.y += speed

def fire_bullet():
    """create bullet object where the ship is"""
    new_bullet = Bullet(rocket_rect)
    bullets.add(new_bullet)

def update_bullets():
    """Move bullets and delete the expired ones"""
    bullets.update(bullet_speed)

    for bullet in bullets.copy():
        if bullet.rect.midleft >= screen_rect.midright:
            bullets.remove(bullet)


pygame.init()
# setup screen
screen = pygame.display.set_mode((1920, 1080))
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()

# setup keypresses
keys = Keys()
# setup rocket
rocket_rect.midleft = screen.get_rect().midleft
# setup bullet
bullet_speed = 1


while True:
    check_events(keys)
    move_rocket(keys, rocket_rect, screen_rect, 2)
    update_bullets()
    screen.fill((0, 0, 0))
    screen.blit(rocket_surface, rocket_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, (0,255,0), bullet.rect)
    print(len(bullets))
    pygame.display.flip()