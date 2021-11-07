import pyautogui
import random
import tkinter as tk
from axolotlApp import *
# adapted from https://medium.com/analytics-vidhya/create-your-own-desktop-pet-with-python-5b369be18868
class PetWindow(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cycle = 0
        self.check = 1
        self.idle_num =[1,2,3,4]
        self.sleep_num = [10,11,12,13,15]
        self.walk_left = [6,7]
        self.walk_right = [8,9]
        # to be implemented
        self.walk_down = [16, 17]
        self.walk_up = [18, 19]
        # self.walk_upLeft = []
        # self.walk_upRight = []
        # self.walk_downRight = []
        # self.walk_downLeft = []
        self.event_number = random.randrange(1,3,1)
        # change to match gif directory
        impath = os.path.dirname(os.path.abspath(__file__)) + '\\'
        #call buddy's action gif
        self.idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
        self.idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
        self.sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
        self.sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
        self.walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
        self.walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
    #transfer random no. to event
    def event(self):
        lengthOfWalk = random.randrange(1, 100)
        if self.event_number in self.idle_num:
            self.check = 0
            print('idle')
            window.after(400,self.update) #no. 1,2,3,4 = idle
        elif self.event_number == 5:
            self.check = 1
            print('from idle to sleep')
            window.after(100,self.update) #no. 5 = idle to sleep
        elif self.event_number in self.walk_left:
            self.check = 4
            print('walking towards left')
            window.after(100,self.update)#no. 6,7 = walk towards left
        elif self.event_number in self.walk_right:
            self.check = 5
            print('walking towards right')
            window.after(100,self.update)#no 8,9 = walk towards right
        elif self.event_number in self.sleep_num:
            self.check  = 2
            print('sleep')
            window.after(1000,self.update)#no. 10,11,12,13,15 = sleep
        elif self.event_number == 14:
            self.check = 3
            print('from sleep to idle')
            window.after(100,self.update)#no. 15 = sleep to idle
        # elif self.event_number in self.walk_down:
        #     self.check  = 6
        #     print('walking down')
        #     window.after(100, self.update)
        # elif self.event_number in self.walk_up:
        #     self.check = 7
        #     print('walking up')
        #     window.after(100, self.update)

    # goes to next cycle of gif animation 
    def gif_work(self, cycle, frames, event_number, first_num, last_num):
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            event_number = random.randrange(first_num,last_num+1,1)
        return cycle,event_number

# update position of the window/pet
    def update(self):
        #idle
        if self.check == 0:
            frame = self.idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.idle,self.event_number,1,9)
        #idle to sleep
        elif self.check ==1:
            frame = self.idle_to_sleep[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle, self.idle_to_sleep,self.event_number,10,10)
        #sleep
        elif self.check == 2:
            frame = self.sleep[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep, self.event_number,10,15)
        #sleep to idle
        elif self.check ==3:
            frame = self.sleep_to_idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.sleep_to_idle,self.event_number,1,1)
        #walk toward left
        elif self.check == 4:
            frame = self.walk_positive[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_positive,self.event_number,1,9)
            self.x -= 3
        #walk towards right
        elif self.check == 5:
            frame = self.walk_negative[self.cycle]
            self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_negative,self.event_number,1,9)
            self.x += 3
        # #walk down
        # elif self.check == 6:
        #     frame  = self.walk_negative[self.cycle]
        #     self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_negative,self.event_number,1,19)
        #     self.y += 3

        # elif self.check == 7:
        #     frame = self.walk_positive[self.cycle]
        #     self.cycle , self.event_number = self.gif_work(self.cycle,self.walk_positive,self.event_number,1,19)
        #     self.y -= 3
    
        window.geometry('100x100+'+str(self.x)+'+'+str(self.y))
        label.configure(image=frame)
        window.after(1,self.event)

# opens game and hides pet when user clicks pet        
def openApp(event):
    window.withdraw()
    runApp(width=1400, height=800)
    window.deiconify()
    window.attributes('-topmost', 1)

window = tk.Tk()
# window configuration
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
# hides window from taskbar, make black background transparent
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
# stack top window
window.attributes('-topmost', 1)
# bind window click to function
label.bind("<Button-1>", openApp)
label.pack()

axo = PetWindow(1000, 500)

#loop the program
window.after(1, axo.update)
window.mainloop()
