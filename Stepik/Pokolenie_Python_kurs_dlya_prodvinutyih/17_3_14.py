with open(r'C:\Users\Sasha\Downloads\population.txt') as file:
    for line in file.readlines():
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)