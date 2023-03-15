# s = 'Величайший урок жизни в том, что и дураки бывают правы.( Уинстон Черчилль )'

s = input()
print(len(__import__('re').findall(fr'(?i){input()}', s)) or len(s))
