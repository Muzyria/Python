def hash_as_key(objects):
    objects_2 = [hash(i) for i in objects]
    my_dict = {}
    for i, j in zip(objects_2, objects):
        if objects_2.count(i) > 1:
            my_dict.setdefault(i, []).append(j)
        else:
            my_dict.setdefault(i, j)
    return my_dict


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))
# {1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
# {-2: [-1, -2], -3: -3, -4: -4, -5: -5}
