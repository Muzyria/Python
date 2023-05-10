import re


class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return re.sub(r'(?i)[aeiouy]', '', string)

    @staticmethod
    def leave_alpha(string):
        return re.sub(r'(?i)[^a-z]', '', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(rf'[{chars}]', char, string)


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('StEpik'))

s = StrExtension()

print(s.remove_vowels('QWERTYqwerty'))

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))

