n = int(input())
movement = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}


for _ in range(n):
    direction = input().split()
    if direction[0] in movement:
        movement[direction[0]] += int(direction[1])

x = movement['восток'] - movement['запад']
y = movement['север'] - movement['юг']

print(x, y)