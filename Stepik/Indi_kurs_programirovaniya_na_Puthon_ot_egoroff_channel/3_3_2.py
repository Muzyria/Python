# put your python code here
n = int(input())
if n % 5 == 0 and n % 3 == 0:
    print('FizzBuzz')
elif n % 5 == 0:
    print('Buzz')
elif n % 3 == 0:
    print('Fizz')
else:
    print(n)