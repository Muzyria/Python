# my_str = input()
my_str = 'Sorting1234'

a = sorted([i for i in my_str if i.islower()])
b = sorted([i for i in my_str if i.isupper()])
c = sorted([i for i in my_str if i.isdigit() and int(i) % 2 == 0])
d = sorted([i for i in my_str if i.isdigit() and int(i) % 2 == 1])
print(''.join(a) + ''.join(b) + ''.join(d) + ''.join(c))

#
# s = input()
# res = "".join(sorted(s, key=lambda x: (not x.isalpha(), not x.islower(), x.isdigit() and not int(x) % 2, x)))
# print(res)