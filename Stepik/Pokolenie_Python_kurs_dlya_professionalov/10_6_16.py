# from sympy import isprime
#
#
# def is_prime(number):
#     return isprime(number)

def is_prime(n):
    return n != 1 and all(n % i != 0 for i in range(2, n))


print(is_prime(7))
