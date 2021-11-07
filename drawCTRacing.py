from cmu_112_graphics import *
from PathsAndScenes import*

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