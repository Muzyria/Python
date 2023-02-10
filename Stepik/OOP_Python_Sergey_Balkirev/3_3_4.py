class Model:
    def __init__(self):
        self.__base = {}

    def query(self, **kwargs):
        self.__base = kwargs

    def __str__(self):
        if self.__base:
            return "Model: " + ", ".join([f"{k} = {v}" for k, v in self.__base.items()])
        return "Model"

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
