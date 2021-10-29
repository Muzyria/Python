# put your python code here
'''
s = list((input()).split())
s = ''.join(s)
print('-'.join(s).upper())
'''
a = list(input().upper())
a = '-'.join(a)
a=a.replace('- -',' ')
print(a)