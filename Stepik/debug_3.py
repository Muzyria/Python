
import sys

class UpperPrint:
    def __enter__(self):
        self.write = sys.stdout.write
        sys.stdout.write = lambda x: self.write(x.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.write


print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
