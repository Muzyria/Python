from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code):
        pairs = [('winter', 'зима'), ('spring', 'весна'), ('summer', 'лето'), ('fall', 'осень')]
        return pairs[self.value -1][0] if code == 'en' else pairs[self.value -1][1]


print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))
