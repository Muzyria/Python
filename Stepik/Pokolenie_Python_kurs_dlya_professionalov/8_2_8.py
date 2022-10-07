import sys


data = [line.strip() for line in sys.stdin][::-1]


def my_rec(num=0):
    if num < len(data):
        print(data[num])
        my_rec(num + 1)


my_rec()


# def my_f():
#     i = int(input())
#     if i != 0:
#         my_f()
#     print(i)
#
#
# my_f()
