from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = ".".join((version.split(".") + ["0", "0"])[:3])

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.version)})"

    def __str__(self):
        return self.version

    def __eq__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split("."))) == list(map(int, other.version.split(".")))
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split("."))) > list(map(int, other.version.split(".")))
        return NotImplemented


versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))

