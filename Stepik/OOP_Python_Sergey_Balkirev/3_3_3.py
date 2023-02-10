import sys

# здесь пишите программу

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка из входного потока (эту строчку не менять)


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


book = Book(*lst_in)
print(book)
