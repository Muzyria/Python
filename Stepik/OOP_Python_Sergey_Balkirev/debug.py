class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        res = (Clock.get_time(self.clock1) - Clock.get_time(self.clock2))
        if res <= 0:
            return '00: 00: 00'
        hours = res // 3600
        minutes = res % 3600 // 60
        seconds = res % 3600 % 60
        return f'{hours:02}: {minutes:02}: {seconds:02}'

    def __len__(self):
        return Clock.get_time(self.clock1) - Clock.get_time(self.clock2)


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)