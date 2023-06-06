import random

def point_in_polygon(point, polygon):
    """
    Проверяет, находится ли заданная точка внутри многоугольника.
    point: Координаты точки в формате 'lat, lng'.
    polygon: Список координат многоугольника.
    Возвращает True, если точка находится внутри многоугольника, и False в противном случае.
    """
    lat, lng = map(float, point.split(','))

    is_inside = False
    n = len(polygon)
    p1x, p1y = map(float, polygon[0].values())
    for i in range(n+1):
        p2x, p2y = map(float, polygon[i % n].values())
        if (lng > min(p1y, p2y)):
            if (lng <= max(p1y, p2y)):
                if (lat <= max(p1x, p2x)):
                    if (p1y != p2y):
                        xinters = (lng - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if (p1x == p2x or lat <= xinters):
                        is_inside = not is_inside
        p1x, p1y = p2x, p2y

    return is_inside


def generate_random_point_in_polygon(polygon):
    """
    Генерирует случайную точку внутри заданного многоугольника.
    polygon: Список координат многоугольника.
    Возвращает координаты случайной точки в виде строки 'lat, lng'.
    """
    x_coords = [float(coord['lat']) for coord in polygon]
    y_coords = [float(coord['lng']) for coord in polygon]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    while True:
        random_x = random.uniform(min_x, max_x)
        random_y = random.uniform(min_y, max_y)

        if point_in_polygon(f'{random_x},{random_y}', polygon):
            return f'{random_x},{random_y}'


# Пример использования

polygon = [
    {'lat': '50.0844272', 'lng': '36.2357837'},
    {'lat': '50.0835598', 'lng': '36.2353009'},
    {'lat': '50.0832775', 'lng': '36.2373823'}
]

random_point = generate_random_point_in_polygon(polygon)
print("Случайная точка внутри многоугольника:", random_point)


def generate_random_point(min_lat, max_lat, min_lng, max_lng, polygon):
    """
    Генерирует случайную точку внутри заданной области, но вне многоугольника.
    min_lat: Минимальное значение широты.
    max_lat: Максимальное значение широты.
    min_lng: Минимальное значение долготы.
    max_lng: Максимальное значение долготы.
    polygon: Список координат многоугольника.
    Возвращает координаты случайной точки в виде строки 'lat, lng'.
    """
    while True:
        random_lat = random.uniform(min_lat, max_lat)
        random_lng = random.uniform(min_lng, max_lng)
        random_point = f'{random_lat},{random_lng}'

        if not point_in_polygon(random_point, polygon):
            return random_point


# Пример использования

polygon = [
    {'lat': '50.0844272', 'lng': '36.2357837'},
    {'lat': '50.0835598', 'lng': '36.2353009'},
    {'lat': '50.0832775', 'lng': '36.2373823'}
]

min_lat = 50.08
max_lat = 50.09
min_lng = 36.23
max_lng = 36.24

random_point = generate_random_point(min_lat, max_lat, min_lng, max_lng, polygon)
print("Случайная точка внутри заданной области, но вне многоугольника:", random_point)
