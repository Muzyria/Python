koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

from itertools import count
import random

random.shuffle(koloda)

print("Do you play in game ?")
count = 0

while True:
    choice = input("Do you need a card? y/n\n")
    if choice == "y":
        current = koloda.pop()
        print("You heve a card %d" %current)
        count += current
        if count > 21:
            print("You loss, your count = %d" %count)
            break
        elif count == 21:
            print("You WIN")
            break
        else: 
            print("You have a %d" %count)
    elif choice == "n":
        print("Yuo have %d balls and you finish this game" %count)
        break
print("Good bye")            
            




