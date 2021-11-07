import pyautogui
import random
import tkinter as tk
# x = 1400
# cycle = 0
# check = 1
# idle_num =[1,2,3,4]
# sleep_num = [10,11,12,13,15]
# walk_left = [6,7]
# walk_right = [8,9]
# event_number = random.randrange(1,3,1)
# impath = 'C:\\Users\\yuchi\\Downloads\\'
# #impath = 'C:\\Users\\fx770\\Desktop\\Project\\Buddy\\image\\'

# def event(cycle,check,event_number,x):
#     if event_number in idle_num:
#         check = 0
#         print('idle')
#         window.after(400,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
    
#     elif event_number == 5:
#         check = 1
#         print('from idle to sleep')
#         window.after(100,update,cycle,check,event_number,x) #no. 5 = idle to sleep

#     elif event_number in walk_left:
#         check = 4
#         print('walking towards left')
#         window.after(100,update,cycle,check,event_number,x) #no. 6,7 = walk towards left
#     elif event_number in walk_right:
#         check = 5
#         print('walking towards right')
#         window.after(100,update,cycle,check,event_number,x) #no 8,9 = walk towards right
#     elif event_number in sleep_num:
#         check  = 2
#         print('sleep')
#         window.after(1000,update,cycle,check,event_number,x) #no. 10,11,12,13,15 = sleep
#     elif event_number == 14:
#         check = 3
#         print('from sleep to idle')
#         window.after(100,update,cycle,check,event_number,x) #no. 15 = sleep to idle
        
# #making gif work 
# def gif_work(cycle,frames,event_number,first_num,last_num):
#     if cycle < len(frames) -1:
#         cycle+=1
#     else:
#         cycle = 0
#         event_number = random.randrange(first_num,last_num+1,1)
#     return cycle,event_number
    
# def update(cycle,check,event_number,x):
#     #idle
#     if check ==0:
#         frame = idle[cycle]
#         cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
#     #idle to sleep
#     elif check ==1:
#         frame = idle_to_sleep[cycle]
#         cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,10,10)
#     #sleep
#     elif check == 2:
#         frame = sleep[cycle]
#         cycle ,event_number = gif_work(cycle,sleep,event_number,10,15)
#     #sleep to idle
#     elif check ==3:
#         frame = sleep_to_idle[cycle]
#         cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1)
#     #walk toward left
#     elif check == 4:
#         frame = walk_positive[cycle]
#         cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
#         x -= 3
#     #walk towards right
#     elif check == 5:
#         frame = walk_negative[cycle]
#         cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
#         x -= -3
#     window.geometry('100x100+'+str(x)+'+1050')
#     label.configure(image=frame)
#     window.after(1,event,cycle,check,event_number,x)
    
# window = tk.Tk()

# #call buddy's action gif
# idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
# #idle gif
# idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)] 
# #idle to sleep gif
# sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]
# #sleep gif
# sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)] 
# #sleep to idle gif
# walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)] 
# #walk to left gif
# walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)] 
# #walk to right gif

# #window configuration
# window.config(highlightbackground='black')
# label = tk.Label(window,bd=0,bg='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor','black')
# label.pack()
# #loop the program
# window.after(1,update,cycle,check,event_number,x)

# window.mainloop()


# class of path
# generates a random path of of length 5 and 

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
        y = 2
        i = 0
        direction = 0
        while x < len(self.boardForScene[0]) - 1:
            initY = y
            initX = x
            if y <= 0:
                randomYDirection = random.randint(2,4) * 1
                direction = 1
            elif y >= len(self.boardForScene) - 1:
                randomYDirection = random.randint(2,4) * -1
                direction = -1
            else:
                if i % 2 == 0:
                    randomYDirection = random.randint(2,4)
                    direction = 1
                else:
                    randomYDirection = random.randint(2,4) * -1
                    direction = -1
            print(randomYDirection)
            randomXDirection = random.randint(2,5)
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

            for xPos in range(initX, x + 1):
                if xPos == (x + initX) // 2:
                    self.boardForScene[y][xPos] = "G"
                else:
                    self.boardForScene[y][xPos] = "p"
            
            if direction == -1:
                for yPos in range(initY, y, direction):
                    self.boardForScene[yPos][x] = "p"
                    print2dList(self.boardForScene)
            else:
                for yPos in range(initY, y):
                    self.boardForScene[yPos][x] = "p"
                    print2dList(self.boardForScene)
            i += 1

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

underWater = Scene(20, 10, 20)
underWater.generatePath()
print2dList(underWater.boardForScene)