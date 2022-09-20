dict_symbols = input()
s = input().lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
tbl = str.maketrans(alphabet, dict_symbols)

print(s.translate(tbl))
