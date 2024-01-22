import re


class CaseHelper:

    @staticmethod
    def is_snake(string: str):
        return all(i.islower() for i in string.split('_'))

    @staticmethod
    def is_upper_camel(string):
        return

    @staticmethod
    def to_snake(string):
        return

    @staticmethod
    def to_upper_camel(string):
        return


print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
print()
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
print()
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
print()
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

