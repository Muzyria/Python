class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(cls):
        if cls.role in Access.__access_list:
            return True
        else:
            return False 
            
    @staticmethod
    def get_access(cls):
        if not isinstance(cls, User):
            print("AccessTypeError")
        elif Access.__check_access(cls):
            print(f"User {cls.name}: success")
        else:
            print("AccessDenied")
   

user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError        