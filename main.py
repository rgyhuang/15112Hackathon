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
        self.idle_num =[1,2,3,4]
        self.walk_left = [6,7]
        self.walk_right = [8,9]
        self.walk_down = [10, 11]
        self.walk_up = [12, 13]
        self.walk_upLeft = [14,15]
        self.walk_upRight = [16,17]
        self.walk_downRight = [18,20]
        self.walk_downLeft = [21,22]
        self.sleep_num = [23,24,25,26,28]
        self.event_number = random.randrange(1,3,1)
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
        if self.event_number in self.idle_num:
            self.check = 0
            #print('idle')
            window.after(400,self.update) #no. 1,2,3,4 = idle
        elif self.event_number == 5:
            self.check = 1
            #print('from idle to sleep')
            window.after(200,self.update) #no. 5 = idle to sleep
        elif self.event_number in self.walk_left:
            self.check = 4
            #print('walking towards left')
            window.after(200,self.update)#no. 6,7 = walk towards left
        elif self.event_number in self.walk_right:
            self.check = 5
            #print('walking towards right')
            window.after(200,self.update)#no 8,9 = walk towards right
        elif self.event_number in self.sleep_num:
            self.check  = 2
            #print('sleep')
            window.after(1000,self.update)#no. 14,15,16,17,19 = sleep
        elif self.event_number == 18:
            self.check = 3
            #print('from sleep to idle')
            window.after(200,self.update)#no. 18 = sleep to idle
        elif self.event_number in self.walk_down:
            self.check  = 6
            #print('walking down')
            window.after(200, self.update) #no. 10, 1 = walking down
        elif self.event_number in self.walk_up:
            self.check = 7
            #print('walking up')
            window.after(200, self.update) #no. 12, 13 = walking up
        elif self.event_number in self.walk_upLeft:
            self.check = 8
            #print('walking up and left')
            window.after(200, self.update) #no. 14, 15 = walking upLeft
        elif self.event_number in self.walk_upRight:
            self.check = 9
            #print('walking up and right')
            window.after(200, self.update) #no. 16, 17 = walking upRight
        elif self.event_number in self.walk_downRight:
            self.check = 10
            #print('walking down and right')
            window.after(200, self.update) #no. 18, 19 = walking downRight
        elif self.event_number in self.walk_downLeft:
            self.check = 11
            #print('walking down and left')
            window.after(200, self.update) #no. 20, 21 = walking downLeft

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
        elif self.check ==1:
            frame = self.idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle, self.idle,self.event_number,23,23)
        # sleep
        elif self.check == 2:
            frame = self.sleep[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep, self.event_number,23, 28)
        # sleep to idle
        elif self.check ==3:
            frame = self.sleep_to_idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep_to_idle,self.event_number,1,1)
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
window.overrideredirect(True)
# make the axolotl desktop pet lmaooooo
axo = PetWindow(1000, 500)

# bind window click to function
label.bind("<Double-1>", openApp)
label.bind("<B1-Motion>", lambda event, petObj=axo: moveWindow(event, petObj))
label.focus_set()
label.pack()

#loop the program
window.after(1000, axo.update)
window.mainloop()
