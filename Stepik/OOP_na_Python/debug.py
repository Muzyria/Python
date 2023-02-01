s = ''.join([bin(int(i))[2:].zfill(8) for i in input().split('.')])

print(all(i in range(256) for i in (n1, n2, n3, n4)) and f'{n1}.{n2}.{n3}.{n4}' not in ('0.0.0.0', '255.255.255.255'))

print("1" not in s[s.index("0"):])