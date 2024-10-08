class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data.append(data)

    def show_table(self):
        if self.is_show:
            print(" ".join(map(str, self.data)))
        else:
            print("Отображение данных закрыто")    

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
        else:
            print("Отображение данных закрыто")

    def  show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show



data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()

"""
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data.append(data)

    def show_table(self):
        if self.is_show:
            print(" ".join(map(str, self.data)))
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f'Графическое отображение данных: {" ".join(map(str, self.data))}')
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {" ".join(map(str, self.data))}')
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show



# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)

gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()


"""
