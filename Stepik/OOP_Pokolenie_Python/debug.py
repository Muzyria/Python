from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


READ_WRITE = Permission.READ | Permission.WRITE

print(~READ_WRITE)