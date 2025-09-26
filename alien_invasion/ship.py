import pygame
import pygame.image

from pygame.sprite import Sprite
from direction import MoveRight, MoveLeft
from ship_state import ShipState
from my_timer import Timer

class Ship(Sprite):
    """Create and manipulate a ship, representing a player"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Create a list of actions with list of all sprites
        self._load_spritesheet()
        self.rect = self.image_list[0][0].get_rect()
        # Place ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement by key pressing
        self.r_direction = MoveRight(self.rect, self.screen_rect)
        self.l_direction = MoveLeft(self.rect, self.screen_rect)

        # Animation
        # Current ship state
        self.state = ShipState.IDLE
        # Current frame of active state
        self.frame = 0
        # Active when firing bullet
        self.firing = False
        # Timer for next animation frame
        self.anim_speed = self.settings.ship_anim_speed[self.state.value]
        self.anim_timer = Timer(self.anim_speed)
        self.anim_timer.start_timer()


    def blitme(self):
        """Draw ship at curent animation and frame"""
        self.screen.blit(self.image_list[self.state.value][self.frame], self.rect)


    def update(self):
        """Move left and right and update animation"""
        self.x = self.r_direction.move(self.settings.ship_speed, self.x)
        self.x = self.l_direction.move(self.settings.ship_speed, self.x)

        #Advance animation to next frame
        self._next_frame()


    def _next_frame(self):
        """Advance animation to next frame"""

        # Play next frame when delay elapsed
        if self.anim_timer.is_elapsed():
            self.frame = (self.frame + 1) % len(self.image_list[self.state.value])
            self.anim_timer.start_timer(duration=self.anim_speed)

            # Disable firing, when animation is finished
            if self.firing and self.frame == 0:
                self.firing = False
                self.set_state()
        

    def _load_spritesheet(self):
        """Create list of actions, containing all sprite images"""
        self.sheet_image = pygame.image.load('images/ship_sheet.png')
        
        # List containing lists of individual sprites
        self.image_list = []

        # Each action has a predefined sprite count
        # Idle, Idle+f, MoveL, MoveR, MoveL+f, MoveR+f
        self.state_sprites = [3, 2, 1, 1, 2, 2]

        # Coordinates in sprite sheet
        curr_x = 0

        for index in self.state_sprites:
            temp_state_list = []

            for _ in range(index):
                temp_state_list.append(self._extract_sprite(curr_x))

                # Advance to the coordinates of next image
                curr_x += self.settings.ship_width

            # List of sprites for current state is ready
            self.image_list.append(temp_state_list)


    def _extract_sprite(self, x):
        """Return a single sprite surface from sprite sheet"""
        new_image = pygame.Surface(
            (self.settings.ship_width, self.settings.ship_height))
        
        new_image.blit(self.sheet_image,                # source
                       (0,0),                           # destination is top left corner of empty surface
                       (x,                              # area from sprite sheet; current x
                        0,                              # sprite sheet is a line, so y is always 0
                        self.settings.ship_width,       # are from sprite sheet is with the size of ship image
                        self.settings.ship_height))
        
        return new_image
    

    def reset_ship(self):
        """Center, put to IDLE and reset animation timer, flags and frame"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.state = ShipState.IDLE
        self.frame = 0
        self.anim_speed = self.settings.ship_anim_speed[self.state.value]
        self.anim_timer.start_timer(duration=self.anim_speed)
        self.firing = False


    def set_state(self):
        """Change ship to start new animation"""
        # This is used when:
        # Left/right key press/release;
        # Space is pressed in order on fire;
        # On active fire when animation finished (Fire animation is fast and completes almost instantly)
        new_state = self._assess_state()

        if new_state != self.state:
            # New state is set. Reset frame, animation speed and timer
            self.state = new_state
            self.frame = 0
            self.anim_speed = self.settings.ship_anim_speed[self.state.value]
            self.anim_timer.start_timer(duration=self.anim_speed)


    def _assess_state(self):
        """Combine move and fire flags to determine new state"""
        if self.firing:
            if self.l_direction.is_moving:
                new_state = ShipState.MOVE_LEFT_FIRE

            elif self.r_direction.is_moving:
                new_state = ShipState.MOVE_RIGHT_FIRE

            else:
                new_state = ShipState.IDLE_FIRE
        else:
            if self.l_direction.is_moving:
                new_state = ShipState.MOVE_LEFT

            elif self.r_direction.is_moving:
                new_state = ShipState.MOVE_RIGHT

            else:
                new_state = ShipState.IDLE

        return new_state
