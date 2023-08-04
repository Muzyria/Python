d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(d,a=[]):
    for item in d:
        if type(item) != list:
            a.append(item)
        else:
            get_line_list(item)
    return a


print(get_line_list(d))
