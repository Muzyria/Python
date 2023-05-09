class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not isinstance(hours, int) or not (0 < hours <= 12):
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(get_hours, set_hours)




try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
