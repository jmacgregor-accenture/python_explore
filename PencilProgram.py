from pencilkatapython.paper import Paper
from pencilkatapython.pencil import Pencil
from os import system

paper = Paper()
pencil = Pencil(15, 5)

exit = "n"
selection = ""

while exit != "y":
    system('clear')
    print(F"Your Paper Shows: {paper.content}")
    print(F"Your Pencil Point is {pencil.durability} and Length of {pencil.length}")
    selection = input("Do you want to <write>, <sharpen>, or <erase>? Type in your answer: ")
    print()
    print()

    if selection == "write":
        writing = input("Type in what you want to write: ")
        paper.write(writing, pencil)
        print(F"Your Paper Shows: {paper.content}")
        print()
    elif selection == "sharpen":
        pencil.sharpen()
        print(F"Your Pencil Point is {pencil.durability} and Length of {pencil.length}")
        print()
    elif selection == "erase":
        erasure = input("What do you want to erase? ")
        paper.erase(erasure)
        print(F"Your Paper Shows: {paper.content}")
        print()

    exit = input("Do you want to exit, y or n? ")

print()
input("Goodbye! Press any key to exit...")

