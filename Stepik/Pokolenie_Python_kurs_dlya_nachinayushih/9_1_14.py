# put your python code here
s = input().lower()
gl, sogl = 0, 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёе':
        gl += 1
for i in range(len(s)):
    if s[i] in 'бвгджзйклмнпрстфхцчшщ':
        sogl += 1
print('Количество гласных букв равно', gl)
print('Количество согласных букв равно', sogl) 