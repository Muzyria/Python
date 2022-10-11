def my_rec(n):
    if n > 0:
        print(n)
        my_rec(n - 5)
    print(n)


my_rec(int(input()))
