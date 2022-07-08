
s = "abababa"
t = "abw"

# s, t = input(), input()
count = 0
i = s.find(t)
while i != -1:
    count += 1
    i = s.find(t, i+1)

print(count)