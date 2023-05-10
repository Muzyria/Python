# import re
#
#
# class CaseHelper:
#     @staticmethod
#     def is_snake(string):
#         return bool(re.fullmatch(r'^[a-z][a-z0-9_]*$', string))
#
#     @staticmethod
#     def is_upper_camel(string):
#         return bool(re.fullmatch(r'^[A-Z][a-zA-Z0-9]*$', string))
#
#     @staticmethod
#     def to_snake(string):
#         return (re.sub('([a-z0-9])([A-Z])', r'\1_\2',  string[0].lower() + string[1::])).lower()
#
#     @staticmethod
#     def to_upper_camel(string):
#         words = re.split('_', string)
#         return ''.join([i.title() for i in words])

import re


class CaseHelper:
    CAMEL_CASE = re.compile(r'^([A-Z][a-z]+)+$')
    SNAKE_CASE = re.compile(r'^([a-z]+_?)+$')

    @staticmethod
    def is_snake(string):
        return bool(CaseHelper.SNAKE_CASE.search(string))

    @staticmethod
    def is_upper_camel(string):
        return bool(CaseHelper.CAMEL_CASE.search(string))

    @staticmethod
    def to_snake(string):
        string = re.sub(r'\B([A-Z])\B', r'_\1', string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())


print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
# beegeek
# bee_geek
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
# Beegeek
# BeeGeek
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))
