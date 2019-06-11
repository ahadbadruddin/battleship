from gameboard import GameBoard
g = GameBoard()

def user():
    guess = 0 
    x = None
    y = None
    while x != g.x or y != g.y:
        x = int(input('Enter an x coordinate for where you think the ship is: '))
        y = int(input('Enter an y coordinate for where you think the ship is: '))
        g.input(x,y)
        guess +=1
    print (f"Game Over. You Won!!! \n It took you {guess} guesses")



if __name__== '__main__':
    user()

