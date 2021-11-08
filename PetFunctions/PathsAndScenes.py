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
        return 4*x, 4*y

    def generatePath(self):
        startRow = 3
        startCol = 0
        direction = 0  
        dRow = 0
        dCol = 0
        i = 0
        end = False
        while startCol < len(self.boardForScene[0])-1:
            dRow = random.randint(2,4)
            dCol = random.randint(3,4)

            #moving up
            if i%2 == 0:
                direction = 1
            # moving down:
            else:
                direction = -1

            # change row and col
            endRow = startRow + dRow*direction
            endCol = startCol + dCol
            #constrains:
            if(endRow >= len(self.boardForScene)-2):
                endRow = len(self.boardForScene)-2
            elif(endRow <= 0):
                endRow = 1
            elif(endCol >= len(self.boardForScene[0])-1):
                end = True
                endCol = len(self.boardForScene[0]) - 1
            # moving right
            for x in range(startCol, endCol):
                print(x)
                print(f"startRow: {(startRow,x)}")
                if(x == (startCol+endCol)//2):
                    self.boardForScene[startRow][x] = "G"
                else:
                    self.boardForScene[startRow][x] = "P"
            # check if reached the end
            if(end == False):
                # if going up:
                if endRow < startRow:
                    for y in range(startRow, endRow,-1):
                        print((y,endCol))
                        self.boardForScene[y][endCol] = "P"
                # if going down
                else:
                    for y in range(startRow,endRow):
                        self.boardForScene[y][endCol] = "P"
            # update start 
            startRow = endRow
            startCol = endCol
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

underwater = Scene(10, 10, 20)
underwater.generatePath()

print2dList(underwater.boardForScene)
