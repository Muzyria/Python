class Circle:
    def __new__(cls, radius):
        cls.PI = 3.14
        instance = super().__new__(cls)
        instance._radius = radius
        instance._diameter = 2 * radius
        cls.get_radius = lambda self: self._radius
        cls.get_diameter = lambda self: self._diameter
        cls.get_area = lambda self: self.PI * self._radius ** 2
        cls.get_perimeter = lambda self: 2 * self.PI * self._radius
        return instance


