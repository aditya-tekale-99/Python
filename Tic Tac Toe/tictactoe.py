import random

#choosing starting player (either X or O will be chosen in random)
def firstplayer(): 
    n = random.randint(1,2)
    firstplay = ""
    if n == 1:
        print("Player 1 will go first as X")
        firstplay = "X"
    else:
        print("Player 2 will go first as O")
        firstplay ="O"
    return firstplay

#building the grid
def buildgrid():
    grid = [[] for x in range(0,3)]
    for index in range(0,3):
        grid[index] = ["-" for y in range(0,3)]

#display the grid
    for value in grid:
        for values in value:
            print(values,end = " ")
        print()
    return grid

#get input
def getinput(grid):
    play_x = input("Enter a number between 0-2 for the row:") #selects the place in the matrix
    if int(play_x) > 2:
        play_x = input("Incorrect choice. Enter number between 0-2 only...")
    play_y = input("Enter a number between 0-2 for column:") #selects the place in the matrix
    if int(play_y) > 2:
        play_y = input("Incorrect choice. Enter number between 0-2 only...")

    if grid[int(play_x)][int(play_y)] != "-":
        print("Place already taken, try again!")
    return play_x,play_y


    
def checkwin(play_x,play_y,grid,counter):
    #checking horizontal win
    if grid[int(play_x)][0] == grid[int(play_x)][1] == grid[int(play_x)][2]:
        print(counter + " wins the game!")
        return True

    #checking vertical win
    elif grid[0][int(play_y)] == grid[1][int(play_y)] == grid[2][int(play_y)]:
        print(counter + " wins the game!")
        return True

    #checking diagonal
    elif grid[0][0] == counter == grid[1][1] == grid[2][2] or grid[0][2] == counter == grid[1][1] == grid[2][0]:
        print(counter + " wins the game!")
        return True


def changecounter(counter):
    if counter == "X":
        counter = "O"
    else:
        counter = "X"
    return counter



def playgame():
    print("Player 1 you will be X and player 2 you will be O")
    firstplay = firstplayer()
    grid = buildgrid()

    i = 0
    winner = False
    counter = firstplay

    while i < 9 and winner == False:
        x,y = getinput(grid)
        grid[int(x)][int(y)] = counter
        if checkwin(x,y,grid,counter) == True:
            winner = True
        else:
            counter = changecounter(counter)
            i += 1
        for r in grid:
            for c in r:
                print(c,end = " ")
            print()
    if i == 9:
        print("No winner game over!")
    else:
        print("game over!")

    playagain = input("Would you like to play again? Y/N:")
    if playagain == "Y":
        playgame()
    else:
        print("Goodbye!")

playgame() #calling the function to execute