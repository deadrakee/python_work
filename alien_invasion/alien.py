import pygame
import pygame.image
import pygame.sprite

from alien_state import AlienState
from my_timer import Timer

class Alien(pygame.sprite.Sprite):
    """Contains characteristics of a single alien"""
    INITAL_FRAME : int = 0

    def __init__(self, ai_game):
        """Create new sprite almost in the top left corner"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Make list of alien sprites and set its rect attribute by a single sprite image
        self.meas_image = pygame.image.load('images/alien.bmp')
        self.rect = self.meas_image.get_rect()
        self._load_spritesheet()

        # Start each new alien near the top left of the screen(one alien spacing)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store its row and column postion
        self.row = 0
        self.col = 0

        # Animation
        self._init_animation()


    def blitme(self):
        """Draw alien with curent animation and frame"""
        self.screen.blit(self.image_list[self.state.value][self.frame], self.rect)


    def update(self):
        """Move the alien left and right and switch animations"""
        # Move across the screen
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

        # Go to next frame
        self._advance_frame()


    def _advance_frame(self):
        """Advance animation to next frame and delete when dying animation is over"""
        # Play next frame when delay elapsed
        if self.anim_timer.is_elapsed():
            # Increment +1 or start from 0 when last frame is reached
            self.frame = (self.frame + 1) % len(self.image_list[self.state.value])
            self.anim_timer.start_timer(duration=self.anim_speed)

            # When last animation of Dying is reached, kill obj
            if self.state == AlienState.DYING and self.frame == Alien.INITAL_FRAME:
                self.kill()


    def mark_dying(self):
        """Raise flag to delete alien after death animation finishes"""
        if not self.dying:
            self.dying = True
            self.state = AlienState.DYING
            self.frame = Alien.INITAL_FRAME
            self.anim_timer.start_timer(duration=self.anim_speed)


    def check_edges(self):
        """Return True if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.left <= 0) or (self.rect.right >= screen_rect.right)
    

    def _init_animation(self):
        """Set inital state, frame, flags and animation timer"""
        # Current alien state
        self.state = AlienState.MOVING
        # Current frame of active state
        self.frame = Alien.INITAL_FRAME
        # Flag indicating kill transition
        self.dying = False
        # Timer for next animation frame
        self.anim_speed = self.settings.alien_anim_speed
        self.anim_timer = Timer(self.anim_speed)
        self.anim_timer.start_timer()


    def _load_spritesheet(self):
        """Create list of actions, containing all sprite images"""
        self.sheet_image = pygame.image.load('images/alien_sheet.png')
        
        # List containing lists of individual sprites
        self.image_list = []

        # Each action has a predefined sprite count
        # Idle, Dying
        self.state_sprites = [1, 5]

        # Coordinates in sprite sheet
        curr_x = 0

        for index in self.state_sprites:
            temp_state_list = []

            for _ in range(index):
                temp_state_list.append(self._extract_sprite(curr_x))

                # Advance to the coordinates of next image
                curr_x += self.rect.width

            # List of sprites for current state is ready
            self.image_list.append(temp_state_list)


    def _extract_sprite(self, x):
        """Return a single sprite surface from sprite sheet"""
        new_image = pygame.Surface(
            (self.rect.width, self.rect.height))
        
        new_image.blit(self.sheet_image,                # source
                       (0,0),                           # destination is top left corner of empty surface
                       (x,                              # area from sprite sheet; current x
                        0,                              # sprite sheet is a line, so y is always 0
                        self.rect.width,                # are from sprite sheet is with the size of alien image
                        self.rect.height))
        
        # Make surface bg transparent
        new_image.set_colorkey(self.settings.WHITE)
        
        return new_image