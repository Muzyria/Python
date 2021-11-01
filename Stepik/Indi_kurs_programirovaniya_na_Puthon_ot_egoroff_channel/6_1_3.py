from string import ascii_lowercase
#print(ascii_lowercase)

alphabet = {}
count = 1
for i in ascii_lowercase:
    alphabet.setdefault(i, count)
    count += 1
for para in alphabet.items():
    print(*para)