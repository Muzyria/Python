import re


def abbreviate(phrase):
    pat = r'[A-Z]|\b(\w)'
    return re.findall(pat, phrase)


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))
