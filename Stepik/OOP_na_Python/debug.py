n1, n2, n3, n4 = [int(i) for i in input().split('.')]
m1, m2, m3, m4 = [int(i) for i in input().split('.')]


def check_ip(*args):
    return all(i in range(256) for i in args) and '.'.join(list(map(str, args))) not in ('0.0.0.0', '255.255.255.255')

def check_mask(*args):
    if all(i in range(256) for i in args):
        s = ''.join([bin(int(i))[2:].zfill(8) for i in args])
        return "1" not in s[s.index("0"):] if "0" in s else True
    else:
        return False

def to_bin():
    l1 = [bin(i) for i in  (n1, n2, n3, n4)]
    l2 = [bin(i) for i in  (m1, m2, m3, m4)]
    for k, v in zip(l1, l2):
        print(k, v)



print(check_ip(n1, n2, n3, n4))
print(check_ip(m1, m2, m3, m4))
print(to_bin())

