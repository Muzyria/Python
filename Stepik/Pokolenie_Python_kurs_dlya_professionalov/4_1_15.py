import sys


for line in sys.stdin:
    if not line.strip().startswith('#'):
        sys.stdout.write(line)
