import sys

data = [line.strip() for line in sys.stdin]
result = 0
miss = 0
for i in data:
    try:
        result += float(i)
    except (TypeError, ValueError):
        miss += 1

print(str(result)[:-2] if str(result)[-2::] == '.0' else result)
print(miss)
