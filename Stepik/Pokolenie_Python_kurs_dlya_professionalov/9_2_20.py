
item = eval(input())

if isinstance(item, list):
    print(item[-1])
elif isinstance(item, tuple):
    print(item[0])
else:
    print(len(item))
