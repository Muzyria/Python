n = int(input())
a = input()
count = 0

a = ''.join(a)

b = list(a)


while '0' in b and '1' in b:
    b.remove('0')
    b.remove('1')
    count = count + 1


print(len(b))