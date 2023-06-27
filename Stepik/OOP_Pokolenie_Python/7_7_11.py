class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02d}-{self.day:02d}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d}'

class ItalianDate(USADate):
    def format(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year}'


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())