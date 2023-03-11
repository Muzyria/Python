import re

link = r'\b(https?)\://([a-z.]+)/(?:[a-z0-9-/_]*)(\?[a-z=&0-9]*)?(#[a-z]+)?'

for i in input().split():
    if s := re.match(link, i):
        print('Полная ссылка:', s[0])
        print(f'Протокол: {s[1]} | Домен: {s[2]} | Параметры: {s[3]} | Якорь: {s[4]}')
        print()
