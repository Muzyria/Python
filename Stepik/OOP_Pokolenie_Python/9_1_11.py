class Currency:
    RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def change_to(self, target_currency):
        if self.currency == target_currency:
            return

        rate = self.RATE.get(self.currency, {}).get(target_currency)
        if rate is None:
            raise ValueError(f"Cannot convert from {self.currency} to {target_currency}")

        self.value *= rate
        self.currency = target_currency

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value + other.value, self.currency)
            else:
                rate = self.RATE.get(self.currency, {}).get(other.currency)
                if rate is None:
                    raise ValueError(f"Cannot convert from {self.currency} to {other.currency}")
                converted_value = self.value + (other.value / rate)
                return Currency(converted_value, self.currency)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value - other.value, self.currency)
            else:
                rate = self.RATE.get(self.currency, {}).get(other.currency)
                if rate is None:
                    raise ValueError(f"Cannot convert from {self.currency} to {other.currency}")
                converted_value = self.value - (other.value / rate)
                return Currency(converted_value, self.currency)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.value * other.value, self.currency)
            else:
                rate = self.RATE.get(self.currency, {}).get(other.currency)
                if rate is None:
                    raise ValueError(f"Cannot convert from {self.currency} to {other.currency}")
                converted_value = self.value * (other.value / rate)
                return Currency(converted_value, self.currency)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.value / other.value
            else:
                rate = self.RATE.get(self.currency, {}).get(other.currency)
                if rate is None:
                    raise ValueError(f"Cannot convert from {self.currency} to {other.currency}")
                converted_value = self.value / (other.value / rate)
                return converted_value

        else:
            raise TypeError("Unsupported operand type for /")

print(Currency(5, 'EUR') + Currency(5, 'EUR'))
print(Currency(11, 'USD') - Currency(5, 'EUR'))
print(Currency(5, 'RUB') * Currency(11, 'USD'))
print(Currency(5, 'USD') / Currency(5, 'EUR'))
