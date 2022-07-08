import re
import requests
s1, s2, flag = input(), input(), 'No'
pattern = r'https.+\.html'
res = requests.get(s1)
lst = re.findall(pattern, res.text)
for el in lst:
    res = requests.get(el)
    temp = re.findall(pattern, res.text)
    if s2 in temp:
        flag = 'Yes'
print(flag)

