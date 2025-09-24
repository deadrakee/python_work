import pygame
import pygame.image

from pygame.sprite import Sprite
from direction import MoveRight, MoveLeft
from ship_state import ShipState

class Ship(Sprite):
    """Create and manipulate a ship, representing a player"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship's image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp') 
        self._load_spritesheet()
        self.rect = self.image_list[0][0].get_rect()


        # Place ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement by key pressing
        self.r_direction = MoveRight(self.rect, self.screen_rect)
        self.l_direction = MoveLeft(self.rect, self.screen_rect)

        # Current ship state
        self.state = ShipState.IDLE
        # Is currently firing
        self.firing = False

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image_list[1][1], self.rect)

    def update(self):
        """Move in all active directions"""
        self.x = self.r_direction.move(self.settings.ship_speed, self.x)
        self.x = self.l_direction.move(self.settings.ship_speed, self.x)

        # TODO
        # Advance Animation
        

    def _load_spritesheet(self):
        """asdas"""
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
    

    def center_ship(self):
        """Place the ship in the original position"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

#TODO
# set state on left/right key press/release
# set on fire, set when fire finishes and release firing flag
# what happens when we move while firing? Fire flag is stuck ?

    def set_state(self):
        """asda"""
        new_state = self._assess_state()

        if new_state != self.state:
            # TODO
            # Reset animation
            pass


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
