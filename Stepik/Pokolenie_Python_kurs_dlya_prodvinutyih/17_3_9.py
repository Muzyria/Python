with open(r'C:\Users\Sasha\Downloads\lines.txt', 'r', encoding='utf-8') as file:
    li = list(map(lambda x: x.strip(), file.readlines()))
    
    li2 = list(filter(lambda x: len(x) == len(max(li, key=len)), li) )
    print(*li2, sep='\n')
    