# snake game using pygame version 2.0.1(make sure to install it)
# learning project from following edureka article
# link to edureka article https://www.edureka.co/blog/snake-game-with-pygame/

# Step 1 Create the Screen
import pygame
import time
import random

pygame.init()
diswidth = 800
disheight = 600
display = pygame.display.set_mode((diswidth,disheight))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake game')

# score/length display
font_style = pygame.font.SysFont("Arial", 35)
def your_score(length):
    score = font_style.render("Length: " + str(length), True, (255,0,0))
    display.blit(score, [10, 0])


# message for after the game is over
font_style = pygame.font.SysFont("comicsansms", 35)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [diswidth/16, disheight/2.2])

# function for the game windows
def gameLoop():
    closewindow = False
    game_over = False

    # x1 and y1 starting position of the snake. dafault is middle of the display
    x1 = diswidth/2
    y1 = disheight/2

    # variables x1_change and y1_change to hold updating values of x and y coordinates
    x1_change = 0
    y1_change = 0

    # snake_list to hold current coordinates of the snake and also Length_of_snake to track current length of snake
    snake_List = []
    Length_of_snake = 1

    # variables for food location
    foodx = random.randrange(0, diswidth, 10)
    foody = random.randrange(0, disheight, 10)

    # while the user hasn't closed the game window. 
    while not closewindow:

        # while user is on the you lost screen
        while game_over == True:
            # display the lost message
            message("You Lost! Press Q to Quit or C to Play Again", (255,0,0))
            pygame.display.update()

            # checking for if the user presses q or c (q to quit or c to replay)
            for event in pygame.event.get():
                # if user just presses the close window button
                if event.type == pygame.QUIT:
                    closewindow = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        closewindow = True
                        game_over = False
                    if event.key == pygame.K_c: 
                        # replay the game
                        gameLoop()

        # for all the events that the user does (got from event.get)
        for event in pygame.event.get():
            # check if the user clicked the close button
            if event.type == pygame.QUIT:
                # close the pygame window by setting game_over to false and ending while loop
                closewindow =  True 

            # code for making the snake move
            # if the user presses down a key
            if event.type == pygame.KEYDOWN:
                # check which key user pressed and change the x1_change/y1_change variable
                if event.key == pygame.K_UP:
                    # check if the snake is currently going down, if it is don't let snake direction change to up, else let snake start going up
                    if x1_change == 0 and y1_change == 10 and Length_of_snake != 1:
                        continue
                    else:
                        x1_change = 0
                        y1_change = -10
                elif event.key == pygame.K_DOWN:
                    # check if the snake is currently going up, if it is don't let snake direction change to down, else let snake start going down
                    if x1_change == 0 and y1_change == -10 and Length_of_snake != 1:
                        continue
                    else:
                        x1_change = 0
                        y1_change = 10
                elif event.key == pygame.K_LEFT:
                    # check if the snake is currently going right, if it is don't let snake direction change to up, else let snake start going left
                    if x1_change == 10 and y1_change == 0 and Length_of_snake != 1:
                        continue
                    else:
                        x1_change = -10
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    # check if the snake is currently going left, if it is don't let snake direction change to up, else let snake start going right
                    if x1_change == -10 and y1_change == 0 and Length_of_snake != 1:
                        continue
                    else:
                        x1_change = 10
                        y1_change = 0
        # if the snake ever hits the boundary, end the game
        if x1 >= diswidth or x1 < 0 or y1 >= disheight or y1 < 0:
            game_over = True
        # update the snakes head location based on what key the user pressed last
        x1 += x1_change
        y1 += y1_change

        # resets the screen to black
        display.fill((0,0,0))

        """ use draw.rect() to draw rectangles  
        syntax is pygame.draw.rect(surface, color, rect) """
        #draws food
        pygame.draw.rect(display, (255,255,255), [foodx, foody, 10, 10])

        # have empty snake_head list so that we can temporarily store current location of the snake head
        snake_Head = []
        # put the x coordinate and y coordinate of the current location of the head into the snake_head list
        snake_Head.append(x1)
        snake_Head.append(y1)
        # add the current x,y coordinates (as an array) to the end of the list to print out the whole snake
        snake_List.append(snake_Head)

        # checks so that the snake_List doesn't hold more coordinates than it's supposed to 
        if len(snake_List) > Length_of_snake:
            # delete the coordinate at the start (which should be the tail of the snake)
            del snake_List[0]

        # check if the head hits any part of the body
        # does this by seeing if the current coordinate of the head hits any of coordinates in the body (excluding the cooordinate of the head at the end)
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True 

        #draws snake
        for x in snake_List:
            # we loop through the snake_List and set each each element in list to x
            # x should be a set of coordinates. because snake_List is a list of lists
            # we can get the x coordinate with x[0] and the y coordinate with x[1]
            pygame.draw.rect(display, (0,255,0), [x[0], x[1], 10, 10] )

        # call function to display score/length
        your_score(Length_of_snake)

        pygame.display.update()

        # when snake touches the food
        if x1 == foodx and y1 == foody:
            # makes food just eaten disappear and spawn new food
            foodx = random.randrange(0, diswidth, 10)
            foody = random.randrange(0, disheight, 10)
            Length_of_snake += 4
        clock.tick(24)
    
    pygame.quit()
    quit() 

# call for the game to start
gameLoop()