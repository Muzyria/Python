def move_geofence_to_square(geofence, target_square_center):
    # Вычислить смещение (разницу) между центрами
    lat_offset = target_square_center["lat"] - (geofence[0]["lat"] + geofence[1]["lat"] + geofence[2]["lat"]) / 3
    lng_offset = target_square_center["lng"] - (geofence[0]["lng"] + geofence[1]["lng"] + geofence[2]["lng"]) / 3

    # Применить смещение ко всем точкам геофенса
    moved_geofence = [
        {"lat": point["lat"] + lat_offset, "lng": point["lng"] + lng_offset}
        for point in geofence
    ]

    return moved_geofence


# Текущие координаты геофенса
geofence = [
    {"lat": 32.95181966580096, "lng": -82.85081863403322},
    {"lat": 32.951837671538215, "lng": -82.85045385360719},
    {"lat": 32.9515135677063, "lng": -82.85062551498415}
]

# Желаемый центр квадрата
target_square_center = {"lat": 32.955294705133, "lng": -82.832450866699}
# -82.84663438797 32.956014903445,-82.847149372101 32.943590660032,-82.833116054535 32.943122465997,-82.832450866699 32.955294705133
# Переместить геофенс в желаемый квадрат
moved_geofence = move_geofence_to_square(geofence, target_square_center)

print(moved_geofence)


def generate_random_target_square(min_lat, max_lat, min_lng, max_lng):
    random_lat = random.uniform(min_lat, max_lat)
    random_lng = random.uniform(min_lng, max_lng)
    return {"lat": random_lat, "lng": random_lng}

min_square_lat = 32.95
max_square_lat = 32.96
min_square_lng = -82.86
max_square_lng = -82.84

# Генерировать случайный центр в заданных границах квадрата
random_target_square = generate_random_target_square(min_square_lat, max_square_lat, min_square_lng, max_square_lng)

# Переместить геофенс в случайный квадрат
moved_geofence = move_geofence_to_square(geofence, random_target_square)