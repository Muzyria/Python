class UserNotFoundError(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)


users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    if username not in users:
        raise UserNotFoundError
    else:
        return users[username]["name"]

try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)
