from enum import Flag, auto

class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()

class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre):
        return genre in self.genres

    def __str__(self):
        return self.name
