from itertools import permutations

[print(''.join(i), sep='\n') for i in sorted(set(permutations(input())))]
