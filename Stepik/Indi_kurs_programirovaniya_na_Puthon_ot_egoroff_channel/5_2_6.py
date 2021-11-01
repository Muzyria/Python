# put your python code here
a, b = int(input()), int(input())
for i in range(a, b +1):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)