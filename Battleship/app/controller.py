#! usr/bin/env python3

from gameboard import GameBoard
g = GameBoard()

def user():

    guess = 0 
    x = None
    y = None
    acceptable_x = ["0", "1", "2", "3", "4"]
    acceptable_y = ["0", "1", "2", "3", "4"]    

    while x != g.x_ran or y != g.y_ran:
        
        print("\nPlease make your battleship attack!\n")

        while x not in acceptable_x:
            x = input('Enter an x coordinate for where you think the ship is: ')
            if x not in acceptable_x:
                print('Please enter a digit between 0 and 4!')    
        
        while y not in acceptable_y:
            y = input('Enter an y coordinate for where you think the ship is: ')
            if y not in acceptable_y:        
                print('Please enter a digit between 0 and 4!')

        x = int(x)
        y = int(y)
        g.input(x, y)
        
        guess +=1
    
    if guess == 1:
        print (f"Game Over. You won on the first try!!!\n")
    else:
        print (f"Game Over. You won!!! \n It took you {guess} guesses\n")


if __name__== '__main__':
    user()
