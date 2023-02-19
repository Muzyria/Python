# Напишите определение класса Library
class Library:
    def __init__(self, list_books):
        self.__books = list_books

    def __check_availability(self, name_book):
        return name_book in self.__books

    def search_book(self, name_book):
        return self.__check_availability(name_book)

    def return_book(self, name_book):
        self.__books.append(name_book)

    def _checkout_book(self, name_book):
        if self.search_book(name_book):
            self.__books.remove(name_book)
            return True
        return False



# Напишите определение класса Library


# Ниже код для проверки методов класса Library
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')
