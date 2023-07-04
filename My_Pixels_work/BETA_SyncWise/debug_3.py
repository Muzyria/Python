import json

point_str = '36.23128696990587 50.0796427739203,36.230924871688856 50.080969826178126'


point_0 = json.dumps([{"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")])

print(point_0, 'generated')

points = []
coordinates = point_str.split(",")
for coordinate in coordinates:
    lng, lat = coordinate.split()
    point = {
        "lat": float(lat),
        "lng": float(lng)
    }
    points.append(point)

points_json = json.dumps(points)
print(points_json)
