
def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


"""
Здесь point - это проверяемая точка, заданная в виде кортежа координат (x, y), 
    а polygon - список вершин многоугольника,
 каждая вершина задана в виде кортежа координат (x, y).
  Функция point_in_polygon возвращает True, 
 если точка находится внутри многоугольника, и False в противном случае.
"""
