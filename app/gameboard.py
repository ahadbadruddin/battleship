BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'
import random

class GameBoard:
    x = random.randint(0,4)
    y = random.randint(0,4)
    def __init__(self, width=5, height=5):
        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
            print(new_row)
        self.grid = grid
        print(self.x, self.y)
        
    def input(self,x,y):
        if x== self.x and y == self.y:
            self.grid[x][y] = ["X"]
        else:
            self.grid[x][y] = ['M']
        self.print()

        
    def print(self):
        for row_index in range(5):
            print(self.grid[row_index])
        
    
        
if __name__=='__main__':
   g = GameBoard()
   g.input(0,0)
