import re


def normalize_jpeg(filename):
    return re.sub(f'(\w+)$', 'jpg', filename)


print(normalize_jpeg('stepik.jPeG'))
