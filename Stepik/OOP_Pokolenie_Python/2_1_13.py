def is_decimal(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
