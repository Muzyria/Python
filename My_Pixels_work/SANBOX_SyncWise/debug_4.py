def get_intermediate_coordinates(path, steps):
    if steps <= 1 or len(path) <= 1:
        return path

    intermediate_coordinates = []
    num_segments = len(path) - 1
    segment_length = steps / num_segments

    for i in range(num_segments):
        start_coord = path[i]
        end_coord = path[i + 1]

        for j in range(steps):
            ratio = j / steps
            lat = start_coord['lat'] + (end_coord['lat'] - start_coord['lat']) * ratio
            lng = start_coord['lng'] + (end_coord['lng'] - start_coord['lng']) * ratio
            intermediate_coordinates.append({'lat': lat, 'lng': lng})

    intermediate_coordinates.append(path[-1])  # Добавляем последнюю координату

    return intermediate_coordinates


path = [
    {'lat': 50.079678437647, 'lng': 36.231405436993},
    {'lat': 50.082184485494, 'lng': 36.231842637062}
]
steps = 2

result = get_intermediate_coordinates(path, steps)
print(result)
