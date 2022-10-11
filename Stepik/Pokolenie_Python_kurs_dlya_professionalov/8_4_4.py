def recursive_sum(nested_list):
    total = 0
    for i in nested_list:
        if type(i) == int:
            total += i
        else:
            total += recursive_sum(i)
    return total


my_list = [1, [4, 4], 2, [1, [2, 10]]]


print(recursive_sum(my_list))
