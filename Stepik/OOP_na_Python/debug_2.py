class MaxLengthAttribute:
    def __get__(self, instance, owner):
        try:
            return sorted(instance.__dict__, key=len, reverse=True)[0]
        except IndexError:
            return



class MyClass:
    max_length_attribute = MaxLengthAttribute()

obj = MyClass()
print(obj.max_length_attribute)