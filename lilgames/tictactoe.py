# My implentation of a simple commandline tictactoe game in Python 3.8.3 :)
import sys
import time
import keyboard

def main():
    # board is a dictionary to sort of hold where the current marks are and how the game is going
    board = { 
        1 : ' ', 2 : ' ', 3 : ' ',
        4 : ' ', 5 : ' ', 6 : ' ',
        7 : ' ', 8 : ' ', 9 : ' '
    }

    # turncount is how many turns it's been
    # mark is whether the next mark will be X or O. Automatically set as 'X' cause X goes first. 
    turncount = 0
    currentmark = 'X'
    # give instructions to player
    print('''
    This is a 2 player tic tac toe game. The board looks like this: 
     1 | 2 | 3 
    ———|———|——— 
     4 | 5 | 6 
    ———|———|———
     7 | 8 | 9 
    To play, each player takes turn putting what location they want to put their
    X or O mark by inputting the location number. X always goes first. 
    ''') 

    prntBoard(board)
    # the game
    while turncount < 9:
        # find where the user wants to put their mark and update the board with the new mark
        location =  int(input("    What number of the board do you want to put your mark in {} player? - ".format(currentmark)))
        if location < 1 or location > 9:
            print("Please input a number 1-9 for location.")
            continue
        if board[location] == ' ':
            board[location] = currentmark
        else:
            print("There's already a mark in this spot. Choose somewhere else.")
            continue
        prntBoard(board)

        # check if with this new mark, the current mark has won. Pass in what the current board dict contains and also the current mark we're on
        if checkwin(board, currentmark) == True:
            print("{} player wins! Press Y to play again or Q to quit.".format(currentmark))
            while True:
                if keyboard.read_key() == "y":
                    main()
                elif keyboard.read_key() == "q":
                    sys.exit()

        # if noone has won yet we switch marks and continue the game
        currentmark = 'O' if currentmark == 'X' else 'X'
        turncount += 1

    # If nobody wins after the 9th move, it should be a tie 
    print("Game Over. It's a tie! Press Y to play again or Q to quit.")
    while True:
        if keyboard.read_key() == "y":
            main()
        elif keyboard.read_key() == "q":
            sys.exit()
        

# function for printing out the current board and all the marks in it + template
def prntBoard(currentboard):
    print(
    f'''
     1 | 2 | 3          {currentboard[1]} | {currentboard[2]} | {currentboard[3]}           
    ———|———|———        ———|———|———     
     4 | 5 | 6          {currentboard[4]} | {currentboard[5]} | {currentboard[6]}
    ———|———|———        ———|———|———
     7 | 8 | 9          {currentboard[7]} | {currentboard[8]} | {currentboard[9]}
    '''
    )

# function to check if the most recent move made someone win
def checkwin(cboard, mark):
    # horizontal
    if cboard[1] == cboard[2] == cboard[3] == mark:
        return True
    elif cboard[4] == cboard[5] == cboard[6] == mark:
        return True
    elif cboard[7] == cboard[8] == cboard[9] == mark:
        return True
    # vertical
    elif cboard[1] == cboard[4] == cboard[7] == mark:
        return True
    elif cboard[2] == cboard[5] == cboard[8] == mark:
        return True
    elif cboard[3] == cboard[6] == cboard[9] == mark:
        return True
    # diagonals
    elif cboard[1] == cboard[5] == cboard[9] == mark:
        return True
    elif cboard[3] == cboard[5] == cboard[7] == mark:
        return True
    else:
        return False

# calling main at the end to run the program
main()    
