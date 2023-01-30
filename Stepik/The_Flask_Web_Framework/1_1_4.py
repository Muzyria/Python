def detect_lucky(x):
    s = list(str(x))
    return sum(int(i) for i in s[:3]) == sum(int(i) for i in s[3:])
