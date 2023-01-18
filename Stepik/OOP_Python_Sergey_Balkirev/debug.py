from random import randint, choice
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + "_.@"
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + "_"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return "".join([choice(cls.EMAIL_RANDOM_CHARS) for _ in range(randint(4, 20))]) + "@gmail.com"

    @classmethod
    def check_email(cls, email):
        if all(char in cls.EMAIL_CHARS for char in email):
            if len(email) <= 100:
                if ".." not in email:
                    if len(email.split("@")[1]) <= 50:
                        if "." in email.split("@")[1]:
                            if email.split("@")[1].count(".") == 1:
                                if cls.__is_email_str(email):
                                    return True
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)
