def my_pow(number):
    return sum([int(i[1]) ** int(i[0]) for i in enumerate(str(number), 1)])

# def my_pow(number):
    # return sum(int(c)**i for i, c in enumerate(str(number),1))


print(my_pow(139))
