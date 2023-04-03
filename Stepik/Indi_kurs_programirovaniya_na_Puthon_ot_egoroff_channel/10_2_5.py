def gen_squares(n):
    for i in range(1, n + 1):
        yield i ** 2


for i in gen_squares(5):
    print(i)

# Будет напечатано
# 1
# 4
# 9
# 16
# 25
for i in gen_squares(3):
    print(i)

# Будет напечатано
# 1
# 4
# 9
