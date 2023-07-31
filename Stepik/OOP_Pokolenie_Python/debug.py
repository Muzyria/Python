import random


def generate_random_path( number_holes, range_time: tuple):
    """Generator random path with range of time"""
    path = [(i, (random.randint(range_time[0], range_time[1])) * 30) for i in range(1, number_holes + 1)]
    print(sum(map(lambda x: x[1], path)))
    random.shuffle(path)
    print(path)


generate_random_path(18, (3, 4))