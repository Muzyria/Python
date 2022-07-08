import requests
import re

res = requests.get(input()).text
pattern = r'''<a.*href=[\"|\'](?:[a-zA-Z0-9]*\:\/\/)?(\w[\w\.-]*)(?:/|\:|\'|\")'''
for i in sorted(set(re.findall(pattern, res))):
    print(i)
