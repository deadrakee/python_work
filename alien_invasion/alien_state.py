from enum import Enum, unique


@unique
class AlienState(Enum):
    """Enumeration for all possible alien states"""
    MOVING = 0
    DYING = 1