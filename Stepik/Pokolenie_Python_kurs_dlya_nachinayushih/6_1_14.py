# put your python code here
a = int(input())
a1 = int(a // 100)
a2 = int((a // 10) % 10)
a3 = int(a % 10)
if ((a1 + a2 + a3) - (max(a1, a2, a3) + min(a1, a2, a3))) + min(a1, a2, a3) == max(a1, a2, a3):
    print('Число интересное')
else:
    print('Число неинтересное')
