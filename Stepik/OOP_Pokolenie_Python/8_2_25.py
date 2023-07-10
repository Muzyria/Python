from datetime import timedelta
from enum import Enum
class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.after_today and self.weekday.value <= self.today.weekday():
            days_ahead = (7 - self.today.weekday() + self.weekday.value)
        else:
            days_ahead = (self.weekday.value - self.today.weekday())
        next_date = self.today + timedelta(days=days_ahead)
        return next_date

    def days_until(self):
        if self.after_today and self.weekday.value <= self.today.weekday():
            days_ahead = (7 - self.today.weekday() + self.weekday.value)
        else:
            days_ahead = (self.weekday.value - self.today.weekday())
        return days_ahead
