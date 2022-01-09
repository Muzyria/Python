file = open(r'C:\Users\Sasha\Downloads\prices.txt', 'r', encoding="utf-8")
li = list(map(lambda line: int(line.strip().split('\t')[1]) * int(line.strip().split('\t')[2]), file.readlines() ))


print(sum(li))

file.close()