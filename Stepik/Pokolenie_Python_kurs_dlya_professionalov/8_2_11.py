def bee(n=1):
    if n < 4:
        s = (str(n) * (16 - (4 * (n - 1))))
        x = int((16 - len(s))/2)
        print(f'{" " * x}{s}')
        bee(n + 1)
    s = (str(n) * (16 - (4 * (n - 1))))
    x = int((16 - len(s)) / 2)
    print(f'{" " * x}{s}')


bee()
