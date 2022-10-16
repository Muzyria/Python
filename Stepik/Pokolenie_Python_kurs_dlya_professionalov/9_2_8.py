def hash_as_key(objects):
    my_dict = {}
    for i, j in zip([hash(i) for i in objects], objects):
        print(i, j)
        if i not in my_dict:
            my_dict[i] = j
        else:
            my_dict[i] = [j]
            my_dict[i].append(j)
    return my_dict


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))
# {1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
# {-2: [-1, -2], -3: -3, -4: -4, -5: -5}
