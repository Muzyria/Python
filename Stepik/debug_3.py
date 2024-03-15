


def txt_to_dict():
    with open(r'C:\Users\FILA\Downloads\planets.txt', 'r', encoding='utf-8') as file:
        result_dict = {}
        lines = (line.strip().split('=') for line in file if line.strip())
        for line in lines:
            result_dict.update({line[0]: line[1]})
            if len(result_dict) == 4:
                yield result_dict
                result_dict = {}





txt_to_dict()