from datetime import date


class DateFormatter:
    C_CODES = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"
    }

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        return date.strftime(d, self.C_CODES[self.country_code])


ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))
