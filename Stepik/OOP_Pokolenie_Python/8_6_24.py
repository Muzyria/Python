from dataclasses import dataclass

@dataclass()
class City:
    name: str
    population: int
    founded: int

# from dataclasses import make_dataclass
#
# City = make_dataclass('City', ('name', 'population', 'founded'))

city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)
