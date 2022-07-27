
n = int(input())
num_dict = {}
for i in range(1, n+1):
    num_dict[i] = tuple(j for j in range(i, n+1) if i == sum(map(int, list(str(j)))))

print(len(max((value for value in num_dict.values()), key=len)))
