# commandline hangman game in Python 3.8.3 :)
import sys
import random
import re
print(sys.version)

# array for hangman pics
hangpics = [
    '''
    +---+
        |
        |
        |
    -----
    ''' 
    ,
    '''
     +---+
     O   |
         |
         |
     -----
    '''
    ,
    '''
     +---+
     O   |
     |   |
         |
     -----
    '''
    ,
    '''
     +---+
     O   |
    /|   |
         |
     -----
    '''
    ,
    '''
     +---+
     O   |
    /|\  |
         |
     -----
    '''
    ,
    '''
     +---+
     O   |
    /|\  |
    /    |
     -----
    '''
    ,
    '''
     +---+
     O   |
    /|\  |
    / \  |
     -----
    '''
]
# list of themes, these themes can be used as keys for the dictionary
themelist = ['animal', 'colors', 'fruits']

# dictionary of words. keys of the dict are the themes, the values is the corresponding tuple that contain the words that match the theme
worddict = {'animals' : ("ant", "bird", "cat", "chicken", "cow", "dog", "elephant", "fish", "fox", "horse", "kangaroo", "lion",
        "monkey", "penguin", "pig", "rabbit", "sheep", "tiger", "whale", "wolf"),
        'colors' : ("aqua", "azure", "beige", "blue", "brown", 	"coral", "crimson",
        "cyan", "gold", "gray", "green", "grey", "hotpink", "indigo", "ivory", "lime",
        "linen", "maroon", "navy", "olive", "orange", "orchid", "peru", "pink", "plum",
        "purple", "red", "salmon", "sienna", "silver", "skyblue", "teal", "thistle", "violet"), 
        'fruits' : ("apple", "apricot", "avocado", "banana", "blueberry", "blackberry", "cherry",
        "coconut", "cucumber", "durian", "dragonfruit", "fig", "grape", "guava", "jackfruit", "plum",
        "kiwi", "kumquat", "lime", "mango", "watermelon", "mulberry", "orange", "papaya", "passionfruit",
        "peach", "pear", "persimmon", "pineapple")}
        
tries = 0
# pick a theme
theme = random.choice(themelist)

# pick a random word from the theme we selected
word = random.choice(worddict[theme])

# initialize an array for the letters found so far and an array to hold the letters user guessed but got wrong
found = []
wrong = []

# print out the original blanks
for i in range(len(word)):
    found.append("_")
    print("_ ", end='')

print("\n")

# the main game
while True:
    print("Hint: {}".format(theme))
    print(hangpics[tries])
    # user loses/guy is hanged
    if tries == 6:
        print(f"Game over! The word your were looking for was {word}.")
        break

    # asks user for input
    guess = (input("Guess a letter: ").strip()).lower()

    # makes sure input is 1 letter, then see if the user's guess is in the word, if so then remember the user found it in the found list
    if len(guess) == 1 and re.match(r"[a-z]", guess):
        for i in range(len(word)):
            if guess == word[i]:
                found[i] = guess
        
        # if the user's guess is wrong and check to make sure he hasn't guessed it yet
        if guess not in word and guess not in wrong:
            wrong.append(guess)
            tries += 1

    # foundstr is the user's progress so far as a string
    foundstr = ''.join(found)

    # print out an updated version of the blanks
    for i in foundstr:
        print(i, end = ' ')

    # print out the letters the users has guessed and gotten wrong
    print("Letters wrong:", *wrong)

    # check if the user has guessed all the letters
    if foundstr == word:
        print("You've found the word! It was %s!" % (word))
        break

        
        