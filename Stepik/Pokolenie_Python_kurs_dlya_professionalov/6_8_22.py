from collections import Counter

total = 0
list_books = Counter(input().split())
# print(list_books)

for _ in range(int(input())):
    book, price = input().split()
    if list_books[book] > 0:
        total += int(price)
        list_books[book] -= 1

print(total)
