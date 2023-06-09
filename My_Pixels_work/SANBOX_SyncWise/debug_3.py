import json

point_str = "36.23908154605 50.089809146357,36.234252228719 50.086182711312,36.23445205329 50.086132802355,36.236780210715 50.08819408508,36.239128484708 50.089814739176"

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
