a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c), (a + b + c) - (max(a, b, c) + min(a, b, c)), min(a, b, c), sep='\n')