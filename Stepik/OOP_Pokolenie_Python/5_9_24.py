def hash_function(obj):
    obj_str = str(obj)
    length = len(obj_str)
    middle = length // 2

    temp1 = sum([ord(obj_str[i]) * ord(obj_str[length - i - 1]) for i in range(middle)])
    if length % 2 == 1:
        temp1 += ord(obj_str[middle])

    temp2 = sum([(lambda x: x * i if i % 2 else x * -i)(ord(obj_str[i - 1])) for i in range(1, length + 1)])

    return (temp1 * temp2) % 123456791


print(hash_function('python'))
