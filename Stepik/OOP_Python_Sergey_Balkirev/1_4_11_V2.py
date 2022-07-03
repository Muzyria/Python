
class Translator:
    def __init__(self):
        self.di = {}
  
    def add(self, eng, rus):
        self.di.setdefault(eng, []).append(rus)  

    def  remove(self, eng):
        del self.di[eng]

    def translate(self, eng):
        return self.di[eng]   



tr = Translator()
tr2 = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))

print(tr.__dict__)

tr2.add("go", "идти")
tr2.add("go", "ехать")
tr2.add("go", "ходить")

print(tr2.__dict__)

