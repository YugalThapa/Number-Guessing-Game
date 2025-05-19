# Guess the number game!!

import os
import random

#clear console after playing
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#generate random number
def Generate_num():
    number = random.randint(1,100)
    return number

#actual game function
def The_Game():
    number = Generate_num()
    print("You Have To Guess The Number Between 1 to 100 ")
    guess = False

    while guess == False:
        guessNum = int(input("Take a guess: "))

        if guessNum != number:
            if number > guessNum:
                print("Guess higher number!")
            elif number < guessNum:
                print("Guess lower number!")

        elif guessNum == number:
            print("Congaratulation!! Your guess is right.")
            guess = True

    #for play again
    playAgain = input("Do You Want To Play Again? (Yes/No) : ")
    playAgain.lower()
    clear_console()
    
    if playAgain == "yes":
        return The_Game()
    else:
        return


The_Game()

