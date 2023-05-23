class Ord:
    def __getattr__(self, item):
        return ord(item)


obj = Ord()

print(obj.a)
print(obj.b)
