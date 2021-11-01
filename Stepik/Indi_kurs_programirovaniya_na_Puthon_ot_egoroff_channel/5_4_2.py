# put your python code here
n = input()
for i in range(0, 10):
    if str(i) in n:
        print(i, n.count(str(i)))