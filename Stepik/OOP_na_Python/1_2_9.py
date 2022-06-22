class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


setattr(Book, "rating", 8.7)
Book.genre = "dystopian"