from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: [x for x in data.items() if x[1] == max(data.values())]
data.min_values = lambda: [x for x in data.items() if x[1] == min(data.values())]


print(data.max_values())
print(data.min_values())
