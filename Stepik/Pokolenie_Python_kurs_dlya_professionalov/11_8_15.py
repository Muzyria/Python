from re import sub, S
import sys

s = sys.stdin.read()
result = sub(r'\n?[ ]*#.+','',s)
result = sub(r'[\n ]*""".+?"""','',result, flags=S)
print(result)
