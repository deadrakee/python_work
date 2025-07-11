"""Module containing classes for ship movement"""

class Direction:
    """Base class abstracting direction"""
    
    def __init__(self, ship_rect, screen_rect):
        """Init a static right movement"""
        self.is_moving = False
        self.ship_rect = ship_rect
        self.screen_rect = screen_rect

    def start_moving(self):
        """Raise flag indicating a right movement"""
        self.is_moving = True

    def stop_moving(self):
        """Lower flag indicating a right movement"""
        self.is_moving = False


class MoveRight(Direction):
    """Holds the state of the right movement"""

    def __init__(self, ship_rect, screen_rect):
        super().__init__(ship_rect, screen_rect)
    
    def move(self, speed, current_x):
        """Move ship to the right based on its old x"""
        # Update the x location passed in the argument to avoid
        # data loss when the speed is a float value, then assign
        # the integer part to rect object
        if self.is_moving and self.ship_rect.right < self.screen_rect.right:
            current_x += speed
            self.ship_rect.x = current_x
        return current_x


class MoveLeft(Direction):
    """Holds the state of the left movement"""
    
    def __init__(self, ship_rect, screen_rect):
        super().__init__(ship_rect, screen_rect)

    def move(self, speed, current_x):
        """Move ship to the left based on its old x"""
        # Update the x location passed in the argument to avoid
        # data loss when the speed is a float value, then assign
        # the integer part to rect object
        if self.is_moving and self.ship_rect.left > 0:
            current_x -= speed
            self.ship_rect.x = current_x
        return current_x
