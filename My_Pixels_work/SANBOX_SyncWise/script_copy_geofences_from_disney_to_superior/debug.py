cord = [50.09299891996568, 36.24363899230958, 50.09313658004037, 36.25930309295655, 50.0806629720677,
        36.258916854858406, 50.08022234377751, 36.24402523040772]

# Новые координаты (центр) в формате словаря
new_center = {"lat": 50.0856375, "lng": 36.2198086}

# Точка на старой карте в формате словаря
old_point = {"lat": 28.4037203, "lng": -81.5869747}

# Рассчитываем разницу в координатах
lat_diff = new_center["lat"] - old_point["lat"]
lng_diff = new_center["lng"] - old_point["lng"]

# Старые координаты, которые вы хотите пересчитать, в формате списка словарей
old_coordinates = [{'lat': 28.4121427, 'lng': -81.5903417}, {'lat': 28.4097329, 'lng': -81.5902528},
                   {'lat': 28.409344, 'lng': -81.5898944}, {'lat': 28.4090065, 'lng': -81.5894698},
                   {'lat': 28.4087964, 'lng': -81.5892348}, {'lat': 28.4084781, 'lng': -81.5891266},
                   {'lat': 28.4077706, 'lng': -81.5890515}, {'lat': 28.40778, 'lng': -81.5890301},
                   {'lat': 28.4054475, 'lng': -81.5873129}, {'lat': 28.403114, 'lng': -81.5858314},
                   {'lat': 28.4028757, 'lng': -81.585744}, {'lat': 28.3997296, 'lng': -81.5845351},
                   {'lat': 28.3976066, 'lng': -81.5824649}, {'lat': 28.3956818, 'lng': -81.5802447},
                   {'lat': 28.3945561, 'lng': -81.5813145}, {'lat': 28.3943863, 'lng': -81.5846932},
                   {'lat': 28.3935256, 'lng': -81.5859064}, {'lat': 28.39228, 'lng': -81.586507},
                   {'lat': 28.389487, 'lng': -81.5880194}, {'lat': 28.3877656, 'lng': -81.5906952},
                   {'lat': 28.3881336, 'lng': -81.5951465}, {'lat': 28.3985466, 'lng': -81.5952391},
                   {'lat': 28.397471, 'lng': -81.6015031}, {'lat': 28.3983816, 'lng': -81.6046068},
                   {'lat': 28.4003441, 'lng': -81.6074269}, {'lat': 28.401022, 'lng': -81.6081901},
                   {'lat': 28.4019063, 'lng': -81.6080731}, {'lat': 28.4037928, 'lng': -81.6063746},
                   {'lat': 28.4072985, 'lng': -81.606308}, {'lat': 28.4082891, 'lng': -81.6005481},
                   {'lat': 28.4092986, 'lng': -81.5984458}, {'lat': 28.4090671, 'lng': -81.5966747},
                   {'lat': 28.4110483, 'lng': -81.5943149}, {'lat': 28.4119446, 'lng': -81.5931351},
                   {'lat': 28.4123031, 'lng': -81.592644}, {'lat': 28.4122748, 'lng': -81.5920947},
                   {'lat': 28.4121427, 'lng': -81.5903417}]


# Функция для пересчета координат
def convert_coordinates(center, coordinates, lat_diff, lng_diff):
    converted_coordinates = []
    for coord in coordinates:
        new_lat = center["lat"] + (coord["lat"] - old_point["lat"])
        new_lng = center["lng"] + (coord["lng"] - old_point["lng"])
        converted_coordinates.append({"lat": new_lat, "lng": new_lng})
    return converted_coordinates


# Вызываем функцию и получаем новые координаты
new_coordinates = convert_coordinates(new_center, old_coordinates, lat_diff, lng_diff)
print(new_coordinates)


# def convert_coordinates_to_float(coordinates):
#     """Функция для преобразования строковых координат в тип float"""
#     converted_coordinates = []
#     for coord in coordinates:
#         lat = float(coord["lat"])
#         lng = float(coord["lng"])
#         converted_coordinates.append({"lat": lat, "lng": lng})
#     return converted_coordinates

# # Вызываем функцию и получаем координаты в формате float
# coordinates_float = convert_coordinates_to_float(old_coordinates)
# print(coordinates_float)
