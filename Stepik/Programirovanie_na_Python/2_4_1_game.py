from random import randint
times = 1
level = float(input('Какой уровень 1 2 3? '))
if level == 1 or level == 2 or level == 3:
    score = level
    print('ПЕРЕХОДИМ НА 1 УРОВЕНЬ')
    while 2 > level > 0.9:
        z = randint(1, 2)
        n1 = randint(1, 5)
        n2 = randint(1, 5)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        else:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('ПЕРЕХОДИМ НА 2 УРОВЕНЬ')
    while 3 > level > 1.9:
        z = randint(1, 2)
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        else:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('ПЕРЕХОДИМ НА 3 УРОВЕНЬ')
    while 4 > level > 2.9:
        z = randint(1, 4)
        n1 = randint(1, 50)
        n2 = randint(1, 50)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        if z == 1:
            r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1+n2
        elif z == 2:
            r = float(input(str(times) + ')' + str(n1+n2) + '-' + str(n1) + '=')) == n1+n2-n1
        elif z == 3:
            r = float(input(str(times) + ')' + str(n3) + '*' + str(n4) + '=')) == n3*n4
        else:
            r = float(input(str(times) + ')' + str(n3*n4) + ':' + str(n4) + '=')) == n3*n4/n4
        if r == 1:
            print('Правильно')
            level += 0.1
            times += 1
        else:
            print('Не правильно')
            times += 1
    print('Вашь счёт = ' + str(int((level-score)*10)) + ' из ' + str(times-1))
else:
    print('Такого уровня нету!')