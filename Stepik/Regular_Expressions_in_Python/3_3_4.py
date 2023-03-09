import re


for _ in range(5):
    result = re.search(r'(?<=Activation key: )([A-Z\d]{5}-?){5}\b', input())
    if result:
        print(result.group())
