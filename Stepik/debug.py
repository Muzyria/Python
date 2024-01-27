from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = version

    @property
    def version(self) -> list:
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        numbers_list = list(map(int, version.split('.')))
        numbers_list.extend([0] * (3 - len(numbers_list)))
        self._version = numbers_list

    def __repr__(self):
        return f"{self.__class__.__name__}('{'.'.join(map(str, self.version))}')"

    def __str__(self):
        return ".".join(map(str, self.version))

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self.version > other.version
        return NotImplemented


a = Version('3')
print(a)
print(repr(a))


print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))
print()
print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))
print()
versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))
