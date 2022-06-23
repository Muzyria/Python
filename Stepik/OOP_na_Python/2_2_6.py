class Zebra:
    def __init__(self, color="white"):
        self.color = color

    def which_stripe(self):
        if self.color == "white":
            print("Полоска белая")
            self.color = "black"
        else:
            print("Полоска черная")
            self.color = "white"


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
z2.which_stripe()
z2.which_stripe()
z2.which_stripe()