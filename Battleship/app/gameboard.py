#! usr/bin/env python3

BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'

import random

class GameBoard:
    
    x_ran = random.randint(0,4)
    y_ran = random.randint(0,4)

    def __init__(self, width=5, height=5):
        grid = []
        print("")
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append("   ")
            grid.append(new_row)
            print(new_row)
        self.grid = grid
        print(self.x_ran, self.y_ran)
        
    def input(self, x, y):
        if x == self.x_ran and y == self.y_ran:
            self.grid[x][y] = ["X"]
        else:
            self.grid[x][y] = ['M']
        self.print()

    def print(self):
        print("")
        for row_index in range(5):
            print(self.grid[row_index])
        print("")
        

if __name__=='__main__':
   g = GameBoard()
   g.input(0,0)
