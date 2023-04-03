with open('words.txt', 'r', encoding='utf-8') as file:
    my_set = set()
    for line in file:
        [my_set.add(i) for i in line.strip().upper().split() if i.endswith('ЕЯ')]
    print(*sorted(my_set, key=lambda x: (len(x), x)), sep='\n')
