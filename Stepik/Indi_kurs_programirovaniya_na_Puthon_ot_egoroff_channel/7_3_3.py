def find_duplicate(x):
    s = []
    for i in x:
        if i not in s and x.count(i) > 1:
            s.append(i)
    return s