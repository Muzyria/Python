def sort_priority(values, group):
    group = [i for i in group if i in numbers]
    values = set(values) - set(group)
    numbers.clear()
    numbers.extend(sorted(list(group)))
    numbers.extend(sorted(list(values)))

# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])
print(numbers)
# [200, 300, 50, 150, 1000, 20000]