from datetime import date


class WeatherWarning:
    @staticmethod
    def rain():
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow():
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature():
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().rain()

    def snow(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().snow()

    def low_temperature(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().low_temperature()


from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)
