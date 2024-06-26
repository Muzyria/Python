class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"


book = Book('Изучаем Python', 'Марк Лутц', 2021)

print(book)
print(repr(book))


