class RoundedInt(int):
    def __new__(cls, value, even=True, *args, **kwargs):
        value += (value % 2 == 1) if even else (value % 2 == 0)
        instance = super().__new__(cls, value)
        return instance
