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
        days_ahead = (self.weekday.value - self.today.weekday()) % 7
        if self.after_today and days_ahead == 0:
            days_ahead = 7
        next_date = self.today + timedelta(days=days_ahead)
        return next_date

    def days_until(self):
        days_ahead = (self.weekday.value - self.today.weekday()) % 7
        if self.after_today and days_ahead == 0:
            days_ahead = 7
        return days_ahead
