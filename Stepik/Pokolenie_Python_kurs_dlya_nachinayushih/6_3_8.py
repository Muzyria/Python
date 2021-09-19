# put your python code here
a, b, c = input(), input(), input()
a1, b1, c1 = int(len(a)), int(len(b)), int(len(c))
if b1 < a1 < c1: print(b, c, sep='\n')
elif a1 < b1 < c1: print(a, c, sep='\n')
elif a1 < c1 < b1: print(a, b, sep='\n')
elif c1 < a1 < b1: print(c, b, sep='\n')
elif b1 < c1 < a1: print(b, a, sep='\n')
elif c1 < b1 < a1: print(c, a, sep='\n') 