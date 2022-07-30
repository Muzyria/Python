# file = open(r'C:\Users\Sasha\Downloads\nums.txt', 'r', encoding="utf-8")
# line = list(map(lambda line: int(line.strip()), file.read().split() ))
# print(sum(line))
#
# file.close()


with open("nums.txt", "r", encoding='utf-8') as file:
    line = list(map(int, file.read().split()))
    print(sum(line))
