# put your python code here
s = input()
total = s.count('f')
ind = 0
if total == 0:
    print(-2)
elif total == 1:
    print(-1)
else:
    ind = s.find('f')
    s = s[:ind] + 'X' + s[ind +1:]
    print(s.find('f'))


    '''
    # put your python code here
s = input()
total = s.count('f')
ind = 0
if total == 0:
    print(-2)
elif total == 1:
    print(-1)
else:
    ind = s.find('f')
    s = s[:ind] + 'X' + s[ind +1:]
    print(s.find('f'))
    
    '''