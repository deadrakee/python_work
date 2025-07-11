"""Module containing classes for ship movement"""

class Direction:
    """Base class abstracting direction"""
    
    def __init__(self, img_rect):
        """Init a static right movement"""
        self.is_moving = False
        self.img_rect = img_rect

    def start_moving(self):
        """Raise flag indicating a right movement"""
        self.is_moving = True

    def stop_moving(self):
        """Lower flag indicating a right movement"""
        self.is_moving = False


class MoveRight(Direction):
    """Holds the state of the right movement"""

    def __init__(self, img_rect):
        super().__init__(img_rect)
    
    def move(self, speed, current_x):
        """Move ship to the right based on its old x"""
        # Update the x location passed in the argument to avoid
        # data loss when the speed is a float value, then assign
        # the integer part to rect object
        if self.is_moving:
            current_x += speed
            self.img_rect.x = current_x
        return current_x


class MoveLeft(Direction):
    """Holds the state of the left movement"""
    
    def __init__(self, img_rect):
        super().__init__(img_rect)

    def move(self, speed, current_x):
        """Move ship to the left based on its old x"""
        # Update the x location passed in the argument to avoid
        # data loss when the speed is a float value, then assign
        # the integer part to rect object
        if self.is_moving:
            current_x -= speed
            self.img_rect.x = current_x
        return current_x
