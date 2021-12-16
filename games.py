#Para declarar uma função, devemos usar a palavra chave def do mundo Python,
# seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:

import hangman
import guessing

print("*********************************")
print("Choose your game!")
print("*********************************")

print("(1) hangman (2) guessing")

play = int(input("What´s game?: "))

if play == 1:
    hangman.play()
elif play == 2:
    guessing.play()