import math


def calculate_circle_points(center, diameter, num_points=10):
    latitude, longitude = center
    radius = diameter / 2  # радиус в метрах
    earth_radius = 6371000  # радиус Земли в метрах

    points = []
    for angle in range(0, 360, int(360 / num_points)):
        angle_rad = math.radians(angle)

        # Смещение в градусах
        delta_lat = (radius / earth_radius) * (180 / math.pi)
        delta_lon = (radius / earth_radius) * (180 / math.pi) / math.cos(math.radians(latitude))

        # Вычисление координат новой точки
        new_lat = latitude + delta_lat * math.sin(angle_rad)
        new_lon = longitude + delta_lon * math.cos(angle_rad)

        points.append((new_lat, new_lon))
        points.append(points[0])

    return points


# Пример использования
center = (36.2451303225386, 50.08329004978064)
diameter = 50  # в метрах
points = calculate_circle_points(center, diameter)

for i, point in enumerate(points):
    print(f"Point {i + 1}: {point}")
