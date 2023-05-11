from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress: str):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _list_tuple__init__(self, ipaddress):
        self.ipaddress = ".".join(map(str, ipaddress))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipaddress}')"

    def __str__(self):
        return self.ipaddress


ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))
