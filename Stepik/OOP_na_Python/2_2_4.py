class Laptop:
    def __init__(self, brand, model, price, laptop_name=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"

'''
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"       
'''

laptop1 = Laptop('hp', '15-bw0xx', 57000)
laptop2 = Laptop('dell', '1', 77000)

print(laptop2.laptop_name)