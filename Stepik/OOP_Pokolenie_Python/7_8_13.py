class Lecture:
    def __init__(self, title, start_time, duration):
        self.title = title
        self.start_time = start_time
        self.duration = duration

class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        self.lectures.append(lecture)

    def total(self):
        total_duration = sum(int(lecture.duration) for lecture in self.lectures)
        hours = total_duration // 60
        minutes = total_duration % 60
        return f"{hours:02d}:{minutes:02d}"

    def longest_lecture(self):
        longest = max(self.lectures, key=lambda lecture: int(lecture.duration))
        return longest.title

    def longest_break(self):
        sorted_lectures = sorted(self.lectures, key=lambda lecture: lecture.start_time)
        longest_break = max(
            (sorted_lectures[i + 1].start_time - sorted_lectures[i].end_time)
            for i in range(len(sorted_lectures) - 1)
        )
        hours = longest_break // 60
        minutes = longest_break % 60
        return f"{hours:02d}:{minutes:02d}"

conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())



conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())  # Ожидаемый результат: 05:20
print(conference.longest_lecture())  # Ожидаемый результат: Жизнь после ChatGPT
print(conference.longest_break())  # Ожидаемый результат: 01:30
