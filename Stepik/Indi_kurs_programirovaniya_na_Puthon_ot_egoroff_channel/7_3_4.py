def first_unique_char(x):
    for i in x:
        if x.count(i) == 1:
            return x.find(i)
        
    return -1