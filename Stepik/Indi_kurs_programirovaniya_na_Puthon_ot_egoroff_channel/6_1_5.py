# put your python code here
def fun(names, match_name):
    j = 1
    while True:
        new_name = match_name + str(j)
        if new_name in names:
            j += 1
        else:
            names[new_name] = new_name
            break
 
 
number = int(input())
d = {}
for i in range(number):
    a = input()
    if a in d:
        fun(d, a)
    else:
        d[a] = 'OK'
for i in d:
    print(d.get(i))
