from itertools import combinations, permutations, combinations_with_replacement
wallet = [100, 50, 20, 10, 5]

count = 0
for i in range(1, 21):
    for j in set(combinations_with_replacement(wallet, i)):
        if sum(j) == 100:
            count += 1
print(count)
