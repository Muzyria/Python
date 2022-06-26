class Date:
    def __init__(self, d, m, y):
        self.__date = f"{d:02}/{m:02}/{y:04}"
        self.__usa_date = f"{m:02}-{d:02}-{y:04}"
    
    @property
    def date(self):
        return self.__date

    @property
    def usa_date(self):
        return self.__usa_date


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999


    
