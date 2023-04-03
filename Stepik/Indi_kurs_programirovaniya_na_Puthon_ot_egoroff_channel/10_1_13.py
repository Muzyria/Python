a = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for i in (days := ((i, a[(i % 7) - 1]) for i in range(1, 78))):
    print(i)
