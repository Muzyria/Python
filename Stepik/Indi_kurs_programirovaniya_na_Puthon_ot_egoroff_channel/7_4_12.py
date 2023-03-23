def first_repeated_word(val: str) -> str:
    """Находит первый дубль в строке"""
    li = val.split()
    for i in range(len(li)-1):
        if li[i] in li[i+1::]:
            return li[i]


print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc Ab cA aB bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))
