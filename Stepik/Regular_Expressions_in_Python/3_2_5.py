import re

# match = re.match(input(), input())
match = re.match("I", "I love regex!")
# Код писать сюда \(❤‿❤)/
print(match.group())
print(match.start())
print(match.end())
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)

[print(eval(f'match.{arg}')) for arg in ('group()', 'start()', 'end()', 'pos', 'endpos', 're', 'string')]
