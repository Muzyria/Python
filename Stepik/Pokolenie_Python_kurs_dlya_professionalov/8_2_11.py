def bee(n=1):
    if n < 4:
        print(n)
        bee(n + 1)
    print(n)


bee()
