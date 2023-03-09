# import re; match = re.match(input(), input())
import re; match = re.match("123", "456789")

print(match.group(0) if match else "")
