def get_min_max(data):
    if data:
        return (min(enumerate(data, 0), key=lambda x: x[1]))[0], (max(enumerate(data, 0), key=lambda x: x[1]))[0]
    return None


data = [2, 3, 8, 1, 7]

print(get_min_max(data))

data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))

data = [9]

print(get_min_max(data))
