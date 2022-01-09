def read_csv():
    result = []
    with open('data.csv') as file:
        keys = file.readline().strip('\n').split(',')
        for line in file:
            values = line.strip('\n').split(',')
            result.append(dict(zip(keys, values)))       
    return result