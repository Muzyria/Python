# put your python code here
n = int(input()[1:])
li = []
for i in range(n):
    li.append(input().rstrip())
for j in range(len(li)):
    if '#' in li[j]:
        li[j] = li[j][:li[j].index('#')]
        li[j] = li[j].rstrip()
              
print(*li, sep='\n')

'''
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())
'''