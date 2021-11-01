# put your python code here
n = int(input())
for i in range(n):
    s = input().lower()
    if 'рок' in s:
        v = s.find('рок')
        print(i + 1, v +1)