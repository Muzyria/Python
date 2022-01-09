with open('data.txt', 'r', encoding='utf-8') as file:
    li = list(map(lambda line: line.strip(), file.readlines()))
    print(*li[::-1], sep='\n')