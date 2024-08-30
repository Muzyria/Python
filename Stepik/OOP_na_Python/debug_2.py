# def is_member(value: str, lst: list) -> bool:
#     return value in lst
def is_member(value: str, lst: list) -> bool:
    if len(lst) == 0:
        return False
    if value == lst[-1]:
        return True
    return is_member(value, lst[:-1])

print(is_member("e", ['a', 'e', 'i', 'o', 'u']))