'''
def closest_mod_5(x):
    y = x
    while True:
        if x % 5 == 0 and x >= y:
            return x
        x += 1
'''
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return closest_mod_5(x+1)