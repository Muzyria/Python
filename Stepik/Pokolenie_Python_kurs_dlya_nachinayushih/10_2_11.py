# put your python code here
s = input()
f = s.find('h')
l = s.rfind('h')
s2 = s[l-1:f:-1]
s = s[:f+1] + s2 + s[l:]
print(s)


'''
s = input()
pos1, pos2 = s.find('h'), s.rfind('h')
print(s[:pos1] + s[pos2:pos1:-1] + s[pos2:])

'''