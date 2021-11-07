import pyautogui
import random
class Scene(object):

    def __init__(self, numCol, numRow, size):
        self.numCol = numCol
        self.numRow = numRow
        self.size = size
        self.boardForScene = []
        for i in range(numRow):
            self.boardForScene.append(["w"] * numCol)

    def centerGrid(self, row, col):
        x = self.size * col + self.size / 2
        y = self.size * row + self.size / 2
        return x, y
    
    def generatePath(self):
        x = 0
        # a hard coded number so that the maze start around the middle
        y = 3
        i = 0
        direction = 0
        # loops until the x of the path reaches the end
        while x < len(self.boardForScene[0]) - 1:
            # stores x and y before it is changed
            initY = y
            initX = x
            # if y is too high or low, go in the opposite direction
            if y <= 1:
                randomYDirection = random.randint(2,4) * 1
                direction = 1
            elif y >= len(self.boardForScene) - 2:
                randomYDirection = random.randint(2,4) * -1
                direction = -1
            else:
                # else make sure that y goes in an opposite direction 
                # compared to the previous path
                if i % 2 == 0:
                    randomYDirection = random.randint(2,4)
                    direction = 1
                else:
                    randomYDirection = random.randint(2,4) * -1
                    direction = -1
            # print(randomYDirection)
            # generates the x direction change
            randomXDirection = random.randint(3,4)
            # add the changes to the x and y
            y += randomYDirection
            x += randomXDirection

            # constrains x and y so that they are not out of bounds
            if x >= len(self.boardForScene[0]) - 1:
                x = len(self.boardForScene[0]) - 1
                initY = y
            if y <= 0:
                y = 1
            if y >= len(self.boardForScene) - 2:
                y = len(self.boardForScene) - 2

            print(x , y)

            # loop from x initial to x to draw the horizontal paths
            for xPos in range(initX, x):
                if xPos == (x + initX) // 2:
                    self.boardForScene[y][xPos] = "G"
                else:
                    self.boardForScene[y][xPos] = "p"
            
            # loops from initialY to y 
            if direction == -1:
                for yPos in range(initY, y - 1, direction):
                    print(yPos)
                    self.boardForScene[yPos][x] = "p"
                    #print2dList(self.boardForScene)
            else:
                for yPos in range(initY, y + 1):
                    print(yPos)
                    self.boardForScene[yPos][x] = "p"
                    #print2dList(self.boardForScene)
            i += 1

    def convertBoardToScene(self):
        for row in self.boardForScene:
            for col in self.boardForScene[0]:
                cx, cy = self.centerGrid(row, col)
                if self.boardForScene[row][col] == "G":
                    # input image of gate at cx and cy
                    pass
                elif self.boardForScene[row][col] == "p":
                    # input image of path
                    pass
                elif self.boardForScene[row][col] == "w":
                    #input image of water
                    pass
        # add corals or sprinkle bubbles around the scene as well

def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def print2dList(L):
    print(repr2dList(L))

underWater = Scene(10, 10, 20)
underWater.generatePath()
print2dList(underWater.boardForScene)

