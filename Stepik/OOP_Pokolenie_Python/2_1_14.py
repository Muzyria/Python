def is_fraction(string):
    parts = string.split('/')
    if len(parts) != 2:
        return False
    numerator, denominator = parts

    if numerator.startswith('-'):
        numerator = numerator[1:]  # Убираем знак "-"

    if not numerator.isdigit() or not denominator.isdigit():
        return False

    if int(denominator) == 0:
        return False

    return True


print(is_fraction('-54/9'))
print(is_fraction('1 / 82'))