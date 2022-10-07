def is_good_password(string: str):
    if not len(string) >= 9:
        return False
    if not any(i.isdigit() for i in string):
        return False
    if not any(i.islower() for i in string):
        return False
    if not any(i.isupper() for i in string):
        return False
    return True


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))


