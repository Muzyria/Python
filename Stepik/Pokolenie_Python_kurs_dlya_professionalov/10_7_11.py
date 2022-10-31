def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as fi:
        # генератор объектов вида:
        # ['Name = Mercury', 'Diameter = 4879.4', 'Mass = 3.302×10^23', 'OrbitalPeriod = 0.241']
        planets = (planet.split('\n') for planet in fi.read().split('\n\n'))

        # генератор объектов вида:
        # [['Name', 'Mercury'], ['Diameter', '4879.4'], ['Mass', '3.302×10^23'], ['OrbitalPeriod', '0.241']]
        planets_info = ((p.split(' = ') for p in planet) for planet in planets)

    # преобразование объектов генератора в словари согласно условию
    for planet in planets_info:
        yield dict(planet)

# def txt_to_dict():
#     with open('planets.txt', 'r', encoding='utf-8') as file:
#         items = (i.split('\n') for i in file.read().split('\n\n'))
#         return (dict(i.split(' = ') for i in planet) for planet in items)

planets = txt_to_dict()
print(next(planets))

planets = txt_to_dict()
print(*planets)
