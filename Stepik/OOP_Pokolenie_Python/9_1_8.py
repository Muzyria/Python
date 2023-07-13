class Testpaper:
    def __init__(self, topic, questions, pass_percentage):
        self.topic = topic
        self.questions = questions
        self.pass_percentage = pass_percentage


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, answers):
        if isinstance(self.tests_taken, dict):
            self.tests_taken[testpaper.topic] = self._get_result(testpaper, answers)
        else:
            self.tests_taken = {testpaper.topic: self._get_result(testpaper, answers)}

    def _get_result(self, testpaper, answers):
        total_questions = len(testpaper.questions)
        correct_answers = sum([1 for ans in answers if ans in testpaper.questions])
        percentage = correct_answers / total_questions * 100

        if percentage >= int(testpaper.pass_percentage[:-1]):
            result = 'Passed!'
        else:
            result = 'Failed!'

        return f'{result} ({round(percentage)}%)'



# TEST
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student = Student()

print(student.tests_taken)