class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


setattr(Book, "name", "Скотный двор")
setattr(Book, "pages", 115)

# [setattr(Book, attr, value) for attr, value in [('name', 'Скотный двор'), ('pages', 115)]]
# [setattr(Book, *p) for p in (['name', 'Скотный двор'], ['pages', 115])]