'''
total = 0
for i in range(1729, 40000):            # верхнюю границу увеличивал, чтобы выдало минимум 5 чисел
    x = int(i ** (1 / 3))               # верхняя граница (т.к. число не больше корня 3й ст. из i)
    for j in range(1, x + 1):
        for k in range(1, x + 1):
            if j ** 3 + k ** 3 == i:    
                total += 1
    if total >= 3:                      # чтобы напечатать числа в которых есть разные j и k 
        print(i)
    total = 0
'''
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a**3 + b**3 == c**3 + d**3 and a!=d and b!= c and b != d and a>b and c>d:
                    print(a**3 + b**3)