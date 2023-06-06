def point_in_polygon(point, polygon):
    """
    Проверяет, находится ли точка внутри многоугольника.
    point: Координаты точки (lat, lng) в виде строки.
    polygon: Список координат многоугольника.
    Возвращает True, если точка находится внутри многоугольника, и False в противном случае.
    """
    lat, lng = [float(coord) for coord in point.split(',')]

    num_vertices = len(polygon)
    j = num_vertices - 1
    in_polygon = False

    for i in range(num_vertices):
        if ((float(polygon[i]['lat']) < lat and float(polygon[j]['lat']) >= lat)
                or (float(polygon[j]['lat']) < lat and float(polygon[i]['lat']) >= lat)):
            if (float(polygon[i]['lng']) + (lat - float(polygon[i]['lat'])) / (float(polygon[j]['lat']) - float(polygon[i]['lat']))
                    * (float(polygon[j]['lng']) - float(polygon[i]['lng']))) < lng:
                in_polygon = not in_polygon
        j = i

    return in_polygon

# Пример использования

# Заданные координаты многоугольника
polygon = [
    {'lat': '50.0844272', 'lng': '36.2357837'},
    {'lat': '50.0835598', 'lng': '36.2353009'},
    {'lat': '50.0832775', 'lng': '36.2373823'}
]

# Точка для проверки
point = '50.0839934,36.2358002'

# Проверка, находится ли точка внутри многоугольника
is_inside = point_in_polygon(point, polygon)

if is_inside:
    print("Точка находится внутри зоны.")
else:
    print("Точка не находится внутри зоны.")


