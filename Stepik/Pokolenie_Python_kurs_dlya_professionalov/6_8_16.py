import sys

s = [tuple(student.strip().split()) for student in sys.stdin]

print(sorted(s, key=lambda x: int(x[1]))[1][0])
