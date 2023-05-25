from collections import defaultdict
from string import printable

hashes = defaultdict(int)

for char in printable:
    hashes[hash(char) % 20] += 1

for hash_value, hash_count in sorted(hashes.items()):
    print(hash_value, '■' * hash_count)