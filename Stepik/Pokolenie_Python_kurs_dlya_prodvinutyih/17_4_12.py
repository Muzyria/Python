
with open("goats.txt", "r", encoding='utf-8') as file_r, \
        open("answer.txt", "w", encoding='utf-8') as file_w:
    file_r.readline()
    colours = {}
    lst_goats = []

    line = file_r.readline().rstrip()
    while line != "GOATS":
        colours.setdefault(line, 0)
        line = file_r.readline().rstrip()
    for item in file_r.readlines():
        lst_goats.append(item.rstrip())

    for color in colours:
        colours[color] = lst_goats.count(color)

    for k, v in colours.items():
        if v > 7:
            file_w.write(f'{k}\n')
