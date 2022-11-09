import re


def abbreviate(phrase):
    pat = r'(\b\w|[A-Z])'
    return (''.join(re.findall(pat, phrase))).upper()


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))
