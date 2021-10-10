# put your python code here
n = input().split()
count = 0
for i in n:
    if i.lower() == 'a' or i.lower() == 'an' or i.lower() == 'the':
        count += 1
print('Общее количество артиклей:', count)
