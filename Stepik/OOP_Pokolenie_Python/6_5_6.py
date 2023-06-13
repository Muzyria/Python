class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'До встречи, {self.name}!')
        return True


with Greeter('Кейв'):
    print('...')

with Greeter('Кейв') as greeter:
    print(greeter.name)
