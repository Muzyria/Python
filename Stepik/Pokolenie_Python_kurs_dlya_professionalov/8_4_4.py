def recursive_sum(nested_lists):
    res = 0
    if type(nested_lists) == int:
        print(nested_lists, end=' ')
        res += nested_lists

    if type(nested_lists) == list:
        for i in nested_lists:
            recursive_sum(i)


my_list = [1, [4, 4], 2, [1, [2, 10]]]


print(recursive_sum(my_list))
