cord = [50.09299891996568, 36.24363899230958, 50.09313658004037, 36.25930309295655,50.0806629720677, 36.258916854858406, 50.08022234377751, 36.24402523040772]






# Новые координаты (центр)
new_center = (50.0806375, 36.2288086)

# Точка на старой карте
old_point = (28.4037203, -81.5869747)

# Рассчитываем разницу в координатах
lat_diff = new_center[0] - old_point[0]
lng_diff = new_center[1] - old_point[1]

# Старые координаты, которые вы хотите пересчитать
old_coordinates = [
    (28.4037238, -81.5870471),
    (28.4037002, -81.5870994),
    # Добавьте остальные координаты сюда
]

# Функция для пересчета координат
def convert_coordinates(center, coordinates, lat_diff, lng_diff):
    converted_coordinates = []
    for coord in coordinates:
        new_lat = center[0] + (coord[0] - old_point[0])
        new_lng = center[1] + (coord[1] - old_point[1])
        converted_coordinates.append((new_lat, new_lng))
    return converted_coordinates

# Вызываем функцию и получаем новые координаты
new_coordinates = convert_coordinates(new_center, old_coordinates, lat_diff, lng_diff)
print(new_coordinates)
