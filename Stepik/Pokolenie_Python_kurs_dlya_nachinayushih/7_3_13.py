n = int(input())
mmin = 0
mmax = 0
for i in range(1, n + 1):
    m = int(input())
    if m > mmax:
        mmin = mmax
        mmax = m
    elif m > mmin:
        mmin = m
print(mmax, mmin, sep='\n')