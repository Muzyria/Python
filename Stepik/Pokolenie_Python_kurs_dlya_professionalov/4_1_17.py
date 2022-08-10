from datetime import datetime
import sys


data = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
if data == sorted(data) and len(data) == len(set(data)):
    print('ASC')
elif data == sorted(data, reverse=True) and len(data) == len(set(data)):
    print('DESC')
else:
    print('MIX')
