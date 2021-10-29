# put your python code here
s =[]
for i in range(3):
    s.append(input())
print(*s[::-1], sep='\n')