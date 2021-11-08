import os
import random
import tkinter as tk
from tkinter import*
from pydub import AudioSegment
from pydub.playback import play
from webbrowser import*

# axolotl desktop pet!
# adapted from https://medium.com/analytics-vidhya/create-your-own-desktop-pet-with-python-5b369be18868
# draw da pet on desktop, press to open another app (15112 companion)
class PetWindow(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cycle = 0
        self.check = 1
        # movement event nums
        self.idle_num ={1,2,3,4}
        self.walk_left = {6,7}
        self.walk_right = {8,9}
        self.walk_down = {10, 11}
        self.walk_up = {12, 13}
        self.walk_upLeft = {14,15}
        self.walk_upRight = {16,17}
        self.walk_downRight = {18,20}
        self.walk_downLeft = {21,22}
        self.sleep_num = {23,24,25}
        self.event_number = random.randrange(1,3,1)
        self.numToEvent = dict()
        for i in range(1, 26):
            if i < 5:
                self.numToEvent[i] = 0
            elif i == 5:
                self.numToEvent[i] = 1
            elif i < 8:
                self.numToEvent[i] = 4
            elif i < 10:
                self.numToEvent[i] = 5
            elif i < 12:
                self.numToEvent[i] = 6
            elif i < 14:
                self.numToEvent[i] = 7
            elif i < 16:
                self.numToEvent[i] = 8
            elif i < 18:
                self.numToEvent[i] = 9
            elif i == 18:
                self.numToEvent[i] = 3
            elif i < 20:
                self.numToEvent[i] = 10
            elif i < 22:
                self.numToEvent[i] = 11
            else:
                self.numToEvent[i] = 2

        # change to match gif directory
        impath = os.path.dirname(os.path.abspath(__file__)) + '\\Assets\\Visuals\\'
        #call axolotl action gif
        self.idle = [tk.PhotoImage(file=impath+'idleAxo_small.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
        self.walk_down = [tk.PhotoImage(file=impath+'rollingAxo.gif',format = 'gif -index %i' %(i)) for i in range(8)] #idle to sleep gif
        self.sleep = [tk.PhotoImage(file=impath+'idleAxo_small.gif',format = 'gif -index %i' %(i)) for i in range(3)] #sleep gif
        self.sleep_to_idle = [tk.PhotoImage(file=impath+'idleAxo_small.gif',format = 'gif -index %i' %(i)) for i in range(8)] #sleep to idle gif
        self.walk_positive = [tk.PhotoImage(file=impath+'walking_positive_axo.gif',format = 'gif -index %i' %(i)) for i in range(8)] #walk to left gif
        self.walk_negative = [tk.PhotoImage(file=impath+'walking_negative_axo.gif',format = 'gif -index %i' %(i)) for i in range(8)] #walk to right gif
    
    #transfer random no. to event
    def event(self):
            self.check = self.numToEvent[self.event_number]
            print(self.check)
            window.after(200, self.update)

    # goes to next cycle of gif animation 
    def gif_work(self, cycle, frames, event_number, first_num, last_num):
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            # find new event num
            event_number = random.randrange(first_num,last_num+1,1)
        return cycle,event_number

# update position of the window/pet
    def update(self):
        # idle
        if self.check == 0:
            frame = self.idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.idle,self.event_number,1,22)
        # idle to sleep
        elif self.check == 1:
            frame = self.idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle, self.idle,self.event_number,23,23)
        # sleep
        elif self.check == 2:
            frame = self.sleep[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep, self.event_number, 1, 1)
        # sleep to idle (doesn't work rn)
        elif self.check == 3:
            frame = self.sleep_to_idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep_to_idle,self.event_number,1, 22)
        # if moving
        dy, dx = random.randrange(1,20), random.randrange(1,20)
        # walk toward right
        if self.check == 4:
            frame = self.walk_positive[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_positive,self.event_number,1,22)
            if self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.x += dx
        # walk towards left
        elif self.check == 5:
            frame = self.walk_negative[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_negative,self.event_number,1,22)
            if self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.x -= dx
        # walk down
        elif self.check == 6:
            frame  = self.walk_down[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_down,self.event_number,1,22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight():
                self.y += dy
        # walk up
        elif self.check == 7:
            frame = self.idle[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.idle,self.event_number,1, 22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight():
                self.y -= dy
        # walk up and left
        elif self.check == 8:
            frame = self.walk_negative[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_negative,self.event_number,1, 22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight() and self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.y -= dy
                self.x -= dx
        # walk up and right
        elif self.check == 9:
            frame = self.walk_positive[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_positive,self.event_number,1, 22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight() and self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.y -= dy
                self.x += dx
        # walk down and right
        elif self.check == 10:
            frame = self.walk_down[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_down,self.event_number,1, 22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight() and self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.y += dy
                self.x += dx
        # walk down and left
        elif self.check == 11:
            frame = self.walk_down[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_down,self.event_number,1, 22)
            if self.y+dy > 0 and self.y+dy < window.winfo_screenheight() and self.x+dx > 0 and self.x+dx < window.winfo_screenwidth():
                self.y += dy
                self.x -= dx
        
        window.geometry('%dx%d+'% (frame.width(), frame.height())+str(self.x)+'+'+str(self.y))
        label.configure(image=frame)
        window.after(1,self.event)

# sounds :D feel free to add more, just make sure file is a .wav and is in same folder
sounds = ['wah.wav', 'AxolotlSqee.wav', 'mars.wav']

# opens game and hides pet when user clicks pet        
def openApp(event):
    window.withdraw()
    sound = AudioSegment.from_file('Assets//Audio//'+random.choice(sounds), format='wav')
    play(sound)
    os.system('PetFunctions\\axolotlApp.py')
    window.deiconify()
    window.attributes('-topmost', 1)

# dragabble axolotl from 
# https://stackoverflow.com/questions/4055267/tkinter-mouse-drag-a-window-without-borders-eg-overridedirect1
lastClickX = 0
lastClickY = 0

def moveWindow(event, petObj):
    petObj.x, petObj.y = event.x - lastClickX+window.winfo_x(), event.y - lastClickY+window.winfo_y()

window = tk.Tk()
# window configuration
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
# hides window from taskbar, make black background transparent
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
# stack top window
window.attributes('-topmost', 1)
# make the axolotl desktop pet lmaooooo
axo = PetWindow(1000, 500)

# bind window click to function
label.bind("<Double-1>", openApp)
label.bind("<B1-Motion>", lambda event, petObj=axo: moveWindow(event, petObj))
label.focus_set()
label.pack()

#loop the program
window.after(1, axo.update)
window.mainloop()
