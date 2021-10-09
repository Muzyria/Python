# put your python code here
s = input()
q = len(s) // 2 + len(s) % 2

print(s[q:] + s[:q])