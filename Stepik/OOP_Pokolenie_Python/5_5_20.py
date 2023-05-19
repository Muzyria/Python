class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @property
    def _convert_time(self):
        return (self.hours + self.minutes // 60) % 24, self.minutes % 60

    def __str__(self):
        converted_time = self._convert_time
        return f"{converted_time[0]:02d}:{converted_time[1]:02d}"

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            return self
        return NotImplemented


t = Time(22, 0)
t += Time(3, 0)
print(t)

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

t = Time(40, 80)
print(t.__add__([]))
print(t.__iadd__('bee'))
