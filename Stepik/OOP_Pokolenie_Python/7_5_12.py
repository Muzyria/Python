from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, new_horizontal, new_vertical):
        pass


class King(ChessPiece):
    def can_move(self, new_horizontal, new_vertical):
        # Король может переместиться только на одну клетку в любом направлении
        return (new_horizontal != self.horizontal or new_vertical != self.vertical) and \
               abs(ord(new_horizontal) - ord(self.horizontal)) <= 1 and abs(new_vertical - self.vertical) <= 1


class Knight(ChessPiece):
    def can_move(self, new_horizontal, new_vertical):
        dx = abs(ord(new_horizontal) - ord(self.horizontal))
        dy = abs(new_vertical - self.vertical)
        return dx * dy == 2


king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))




