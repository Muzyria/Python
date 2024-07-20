# Напишите определение класса PermissionMixin
class PermissionMixin:
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions

class User(PermissionMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

# Ниже код для проверки миксина PermissionMixin

user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

assert user1.email == 'alice@example.com'
assert user1.name == 'Alice'
assert user1.permissions == set()

assert user2.email == 'bob@example.com'
assert user2.name == 'Bob'
assert user2.permissions == set()

user1.grant_permission('read')
user1.grant_permission('write')
user2.grant_permission('read')
assert user1.permissions == {'read', 'write'}
assert user2.permissions == {'read'}

assert user1.has_permission('read') is True
assert user1.has_permission('write') is True
assert user1.has_permission('execute') is False

assert user2.has_permission('read') is True
assert user2.has_permission('write') is False
assert user2.has_permission('execute') is False

user1.revoke_permission('write')
user1.revoke_permission('execute')

assert user1.has_permission('read') is True
assert user1.has_permission('write') is False
assert user1.has_permission('execute') is False

print('Good')