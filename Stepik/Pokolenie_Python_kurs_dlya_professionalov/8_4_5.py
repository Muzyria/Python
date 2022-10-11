def linear(nested_list):
    total = []
    for i in nested_list:
        if type(i) == int:
            total.append(i)
        else:
            total.extend(linear(i))
    return total


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
