my_dict = {'Дили': set(), 'Вили': set(), 'Били': set()}
while (n := input()) != 'конец':
    my_dict[n.split(': ')[0]].add((n.split(': ')[1]))

for k, v in sorted(my_dict.items(), key=lambda x: -len(x[1])):
    print(f"Количество уникальных комментаторов у {k} - {len(v)}")
