from bisect import insort
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Lecture:
    _PATTERN = '%H:%M'

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, self._PATTERN)
        self.duration = datetime.strptime(duration, self._PATTERN)
        self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        for cur_lecture in self.lectures:
            if any((
                    cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
                    lecture.start_time <= cur_lecture.start_time < lecture.end_time,
            )):
                raise ValueError('Провести выступление в это время невозможно')
        insort(self.lectures, lecture, key=lambda item: item.start_time)

    def total(self):
        total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
        return f'{total.hours:0>2}:{total.minutes:0>2}'

    def longest_lecture(self):
        longest = max(lecture.duration for lecture in self.lectures)
        return f'{longest.hour:0>2}:{longest.minute:0>2}'

    def longest_break(self):
        longest = max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1))
        hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
        return f'{hours:0>2}:{minutes:0>2}'
