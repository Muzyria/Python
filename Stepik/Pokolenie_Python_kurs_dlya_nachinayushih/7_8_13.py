for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)

'''
data = {}

def pow5(x):
    try:
        return data[x]
    except KeyError:
        data[x] = x ** 5
        return data[x]

for a in range(1, 150):
    for b in range(a + 1, 150):
        for c in range(b + 1, 150):
            for d in range(c + 1, 150):
                z = pow5(a) + pow5(b) + pow5(c) + pow5(d)
                e = int(z ** (1 / 5))
                if z == pow5(e):
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
'''