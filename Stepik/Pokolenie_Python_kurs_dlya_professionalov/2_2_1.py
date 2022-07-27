
d1, d2, d3 = [int(input()) for i in range(3)]

print(min(d1 + d2 + d3, 2*(d1 + d2), 2*(d2 + d3), 2*(d1 + d3)))
