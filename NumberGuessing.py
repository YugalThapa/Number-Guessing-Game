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

 #for score
def score( chance_Remaining):
    key = str(chance_Remaining)
    score_list = {
        "0" : 0,
        "1" : 10,
        "2" : 20,
        "3" : 30,
        "4" : 60,
        "5" : 80,
        "6" : 100,
    }
    if key in score_list:
            print("Your score is ", score_list[key])


#actual game function
def The_Game():
    number = Generate_num()
    print("You Have To Guess The Number Between 1 to 100 in seven chances. ")
    guess = False
    chance = 7

    while guess == False and chance !=0 :
        guessNum = int(input("Take a guess: "))

        if guessNum != number:
            chance -= 1
            if number > guessNum and chance >= 1:
                
                print(f"Guess higher number! {chance} chance remaining")
            elif number < guessNum and chance >= 1:
                
                print(f"Guess lower number! {chance} chance remaining")
            
        elif guessNum == number:
            print("Congaratulation!! Your guess is right.")
            guess = True

    if chance == 0:
        print("Game Over!! You guess it wrong")
        chance -= 1
    score( chance )

    #for play again
    playAgain = input("Do You Want To Play Again? (Yes/No) : ")
    playAgain.lower()
    clear_console()
    
    if playAgain == "yes":
        return The_Game()
    else:
        return


The_Game()

