from enum import Enum


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


print(Direction.WEST.name)
print(Direction.SOUTH.value)
