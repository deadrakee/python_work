from enum import Enum, unique

@unique
class ShipState(Enum):
    """Enumeration for all possible ship states"""
    IDLE = 0
    IDLE_FIRE = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    MOVE_LEFT_FIRE = 4
    MOVE_RIGHT_FIRE = 5