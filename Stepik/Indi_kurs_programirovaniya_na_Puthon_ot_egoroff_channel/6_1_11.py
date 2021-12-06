a = int(input())
day={}
for i in range(a):
    name,days, mons  = input().split()
    if mons not in sorted(day):
        day[mons]=str(name)
    else:
        day[mons]=day[mons]+" "+str(name)

a = int(input())
spis=[]
for i in range(a):
    m=input()
    spis.append(m)

for i in spis:

    if i in day:
        if len(day[i]) == 1:
            print(day[i])

        if len(day[i])>1:
            g = []
            for j in sorted(day[i].split()):
                g.append(''.join(j))
            print(*g)
    else:
        print("Нет данных")