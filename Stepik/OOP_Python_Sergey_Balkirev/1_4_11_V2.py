class Translator:
    dict_data = {}

    def add(self, eng, rus):
        self.dict_data.setdefault(eng, [])
        if rus not in self.dict_data[eng]:
            self.dict_data[eng].append(rus)

    def translate(self, eng):
        return self.dict_data[eng]

    def remove(self, eng):
        del self.dict_data[eng]


tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove("car")
print(*tr.translate("go"))

tr2 = Translator()
print(tr.__dict__)
print(tr.dict_data)

tr2.add("go", "идти")
tr2.add("go", "ехать")
tr2.add("go", "ходить")

print(tr2.__dict__)
print(tr2.dict_data)
