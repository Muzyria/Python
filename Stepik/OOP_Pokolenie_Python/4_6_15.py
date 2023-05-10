class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def x1(self):
        discriminant = self._b**2 - 4*self._a*self._c
        if discriminant < 0:
            return None
        else:
            return (-self._b - discriminant**0.5) / (2*self._a)

    @property
    def x2(self):
        discriminant = self._b**2 - 4*self._a*self._c
        if discriminant < 0:
            return None
        else:
            return (-self._b + discriminant**0.5) / (2*self._a)

    @property
    def view(self):
        sign_b = '+' if self._b >= 0 else '-'
        sign_c = '+' if self._c >= 0 else '-'
        return f"{self._a}x^2 {sign_b} {abs(self._b)}x {sign_c} {abs(self._c)}"

    @property
    def coefficients(self):
        return self._a, self._b, self._c

    @coefficients.setter
    def coefficients(self, new_coefficients):
        self._a, self._b, self._c = new_coefficients
