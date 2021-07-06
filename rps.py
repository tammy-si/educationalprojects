# My implementation of a simple commandline rock paper scissors game in Python 3.8.3 :)
import random
import keyboard
import sys

def game():
    print("\n This is rock paper scissors. To play you just input rock, paper, or scissors fully.")
    choice = 0
    # validating input
    while True:
        choice = input("Pick rock, paper, or scissors: ").lower()
        if choice == "rock" or choice =="paper" or choice == "scissors":
            break

    # getting what the computer picked
    arr = ["rock", "paper", "scissors"]
    computerchoice = arr[random.randint(0, 2)]
    print("You picked " + choice + "." + " The computer picked " + computerchoice + ".")

    # dictionary connecting key to the values that make the key lose. 
    dict = {"rock" : "paper",
            "paper" : "scissors",
            "scissors": "rock"}
    # comparing user input and computer's choice to see who won
    # if the user and computer picked the same thing
    if choice == computerchoice:
        print("It's a tie. If you want to play again press y. If you want to quit press q.")
        while True:
            if keyboard.is_pressed("y"):
                game()
            elif keyboard.is_pressed("q"):
                sys.exit()
    # if the computer picked something beats what the user picked, then the computer whens
    elif computerchoice == dict[choice]:
        print("The computer wins. If you want to play again press y, but if you want to quit press q.")
        while True:
            if keyboard.is_pressed("y"):
                game()
            elif keyboard.is_pressed("q"):
                sys.exit()
    # if the computer didn't win, and it isn't a tie, then it means that the user must've won
    else:
        print("Congrats! You won! If you want to play again press y, but if you want to quit press q.")
        while True:
            if keyboard.is_pressed("y"):
                game()
            elif keyboard.is_pressed("q"):
                sys.exit()

game()


