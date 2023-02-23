class Order:
    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        return Order(self.cart.append(other), self.customer)

    def __radd__(self, other):
        pass



# Напишите определение класса Order


# Ниже код для проверки методов класса Order

order = Order(['banana', 'apple'], 'Гена Букин')
print(order.cart)
order_2 = order + 'orange'
print(order.cart)
print(order_2.cart)
# assert order.cart == ['banana', 'apple']
# assert order.customer == 'Гена Букин'
# assert order_2.cart == ['banana', 'apple', 'orange']

# order = 'mango' + order
# assert order.cart == ['mango', 'banana', 'apple']
# order = 'ice cream' + order
# assert order.cart == ['ice cream', 'mango', 'banana', 'apple']
#
# order = order - 'banana'
# assert order.cart == ['ice cream', 'mango', 'apple']
#
# order = order - 'mango'
# assert order.cart == ['ice cream', 'apple']
# order = 'lime' - order
# assert order.cart == ['ice cream', 'apple']
# print('Good')
