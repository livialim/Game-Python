#Usando nesse joguinho #print() #int(input(()) #if #else #while #for in range #random
#Vars inputs and loops

import random

def play():
    print("*********************************")
    print("Welcome to play guessing game!")
    print("*********************************")

    num_secret = round(random.randrange(10))
    attempts = 0
    points = 1000

    print("What level of difficulty?")
    print("(1)easy (2)medium (3)hard")
    level = int(input("Answer: "))
    if level == 1:
        attempts = 5
    if level == 2:
        attempts = 4
    else:
        attempts = 3

    guessing = int(input("Enter a number between 1 and 10: "))
    print("You digit", guessing)

    while guessing != num_secret:

        if guessing < 1 or guessing > 10:
            guessing = int(input("[ERROR!] Enter a number between 1 and 10: "))

        if guessing < num_secret:
            print("You missed! Play higher")
            guessing = int(input("Enter a number: "))

        elif guessing > num_secret:
            print("You missed! Play lower")
            guessing = int(input("Enter a number: "))

        if guessing == num_secret:
            print("You right!, total points {}".format(points))

        points_lost = abs(guessing - num_secret)
        points = points - points_lost

if (__name__ == "__main__"):
    play()

# for x in range (x, y, w): w is optional = (start, stop, [step])
# print(x)
