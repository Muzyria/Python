def get_max_index(numbers):
    max_index = 0
    max_value = 0

    for index, value in enumerate(numbers, 0):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index


print(get_max_index([2,3,4,5,6,7,1,2]))
