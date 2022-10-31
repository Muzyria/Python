# def txt_to_dict():
with open('planets.txt', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(' = ') for line in file_lines)
        # line_dicts = (dict() for data in line_values)
    for _ in range(4):
        for i in line_values:
            d = dict(i[0] = i[1])


# planets = txt_to_dict()
# print(next(planets))
