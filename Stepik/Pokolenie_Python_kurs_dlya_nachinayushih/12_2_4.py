# put your python code here
spisok1=[i for i in input().split('-')]
spisok2=[len(i) for i in spisok1 if i.isdigit()]
print('YES' if spisok2==[1, 3, 3, 4] and spisok1[0]=='7' or spisok2==[3, 3, 4] else 'NO')