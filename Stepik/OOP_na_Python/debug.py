import re
class UserMail:
    def __init__(self, login, email):
        self.__email = None
        self.login = login
        self.set_email(email)

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) and re.findall(r'^\w+@\w+\.\w+$', email):
            self.__email = email
        else:
            print(f"ErrorMail:{email}")

    email = property(fget=get_email, fset=set_email)