
from random import randint, choice

class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return "".join([choice(self.psw_chars) for _ in range(randint(self.min_length, self.max_length))])

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)

lst_pass = [rnd(), rnd(), rnd()]
