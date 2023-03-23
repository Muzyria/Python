def first_repeated_word(val: str) -> str:
    """Находит первый дубль в строке"""
    my_li = []
    for word in val.split():
        if word in my_li:
            return word
        else:
            my_li.append(word)


print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc Ab cA aB bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))
