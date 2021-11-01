# put your python code here
a = input().lower().replace('ь','')
b = input().lower().replace('ь','')
if a[-1] == b[0]:
    print('Good')
else:
    print('Bad')