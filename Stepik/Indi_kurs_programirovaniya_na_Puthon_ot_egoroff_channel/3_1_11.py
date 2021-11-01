# put your python code here
n = int(input())
'''
num1 = sum(list(range(2, n +1, 2)))  # список содержит четные числа 
num2 = sum(list(range(1, n +1, 2)))  # список содержит нечетные числа
print((num2 * -1) + num1)
'''
if n % 2 == 0:
    print(n - n // 2)
else:
    print((n -n // 2) * -1)