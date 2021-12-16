import random

def print_msg():
    print("*********************************")
    print("Welcome to game hangman game!")
    print("*********************************")


def carrying_word():
    archive = open("words.txt", "r")
    words = []
    for line in archive:
        line = line.strip()
        words.append(line)
    archive.close()
    num = random.randrange(0, len(words))
    word_secret = words[num].lower()
    return word_secret


def play():
    print_msg()

    word_secret = carrying_word()

    list_letter = ["_" for letter in word_secret]

    hanged = False
    right = False
    error = 0
    # while (True)
    while not hanged and not right:
        guess = input("Guess the word secret: \n").lower()
        guess = guess.strip()
        #marca o chute correto no espaçamento certo
        if guess in word_secret:
            index = 0
            for letter in word_secret:
                if guess == letter:
                    list_letter[index] = letter
                index += 1
        else:
            error += 1
            drawing(error)

        hanged = error == 8
        #substitui _ pela letra certa
        right = "_" not in list_letter
        print(list_letter)
    #mensagem se acertou/errou
    if right:
        print("\nYou won, congratulations 🥳")
    else:
        print("\nYou died ⚰️")
        print(word_secret)


def drawing(error):
    print("  _______     ")
    print(" |/      |    ")

    if error == 1:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 2:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 3:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if error == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if error == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if error == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if error == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if error == 8:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    play()
