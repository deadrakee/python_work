from enum import Enum

class ShipState(str, Enum):
    """Enumeration for all possible ship states"""
    IDLE = "idle"
    IDLE_FIRE = "idle_fire"
    MOVE_LEFT = "move_left"
    MOVE_RIGHT = "move_right"
    MOVE_LEFT_FIRE = "move_left_fire"
    MOVE_RIGHT_FIRE = "move_right_fire"