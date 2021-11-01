# put your python code here
n = int(input())
for i in range(n):
    s = input()
    if 'соль' in s:
        continue
    else:
        if i < n-1:
            s += ',' 
            print(s, end=' ')
        else: print(s, end=' ')     
