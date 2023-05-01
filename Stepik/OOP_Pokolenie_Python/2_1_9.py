
for i in open(0):
    x = __import__('re').findall(r'[\d\.\-]+', i)
    print(-90 <= float(x[0]) <= 90 and -180 <= float(x[1]) <= 180)
