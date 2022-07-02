from dataclasses import dataclass


@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5


stonehenge = Location('Stonehenge', 51, 1.5)   


print(stonehenge)