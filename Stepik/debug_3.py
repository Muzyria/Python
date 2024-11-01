

class WeatherWarning:
    def rain(self, date=None):
        if date:
            print(date.strftime('%d.%m.%Y'))
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self, date=None):
        if date:
            print(date.strftime('%d.%m.%Y'))
        print('Ожидается снег и усиление ветра')

    def low_temperature(self, date=None):
        if date:
            print(date.strftime('%d.%m.%Y'))
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    pass


from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)