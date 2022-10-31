# def txt_to_dict():
with open('planets.txt', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(' = ') for line in file_lines)
    line_dicts = ({data[0]: data[1]} for data in line_values)



# planets = txt_to_dict()
# print(next(planets))
