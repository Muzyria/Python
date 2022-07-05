class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.li = []

    def add(self, *a):
        # добавить следующую часть последовательности
        for i in a:
            self.li.append(i)
            if len(self.li) >= 5:
                print(sum([self.li.pop(0) for i in range(5)]))

    def get_current_part(self):
        #print(self.li)
        return self.li
