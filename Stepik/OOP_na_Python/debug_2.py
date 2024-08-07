def make_strings_big(*args, reverse=False):
    for i in args:
        if reverse:
            print(i.lower())
        else:
            print(i.upper())



make_strings_big('У лукоморья дуб зелёный',
                 'Златая цепь на дубе том:',
                 'И днём и ночью кот учёный')