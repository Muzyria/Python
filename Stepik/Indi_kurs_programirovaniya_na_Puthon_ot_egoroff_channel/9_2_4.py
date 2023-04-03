with open('lorem.txt', 'r', encoding='utf-8') as file:
    my_set = set()
    for line in file:
        [my_set.add(i) for i in line.strip().upper().split()]
    print(len(my_set))
