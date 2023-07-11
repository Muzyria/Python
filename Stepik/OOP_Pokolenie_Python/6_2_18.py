class MutableString:
    def __init__(self, string=''):
        self._string = string

    def _set_or_del(self, key, value=None):
        tmp = list(self._string)
        if value:
            tmp[key] = value
        else:
            del tmp[key]
        return tmp

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __str__(self):
        return self._string

    def __repr__(self):
        return f"MutableString('{self._string}')"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        return iter(self._string)

    def __delitem__(self, key):
        tmp = self._set_or_del(key)
        self._string = ''.join(tmp)

    def __setitem__(self, key, value):
        tmp = self._set_or_del(key, value)
        self._string = ''.join(tmp)

    def __getitem__(self, key):
        return MutableString(self._string[key])

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self._string + other._string)
        return NotImplemented
