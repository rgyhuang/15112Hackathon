import pyautogui
import random
import tkinter as tk

class Pet(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cycle = 0
        self.check = 1
        self.idle_num =[1,2,3,4]
        self.sleep_num = [10,11,12,13,15]
        self.walk_left = [6,7]
        self.walk_right = [8,9]
        self.event_number = random.randrange(1,3,1)
        # change to match gif directory
        impath = 'C:\\Users\\Roy Huang\\Documents\\CS\\CMU-Coding\\15112Hackathon\\Hack112\\'
        #call buddy's action gif
        self.idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
        self.idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
        self.sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
        self.sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
        self.walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
        self.walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
    #transfer random no. to event
    def event(self):
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

    #making gif work 
    def gif_work(self, cycle, frames, event_number, first_num,last_num):
        if cycle < len(frames) -1:
            cycle += 1
        else:
            cycle = 0
            event_number = random.randrange(first_num,last_num+1,1)
        return cycle,event_number

    def update(self):
        #idle
        if self.check ==0:
            frame = self.idle[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.idle,self.event_number,1,9)
        #idle to sleep
        elif self.check ==1:
            frame = self.idle_to_sleep[self.cycle]
            self.cycle ,self.event_number = self.gif_work(self.cycle,self.idle_to_sleep,self.event_number,10,10)
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
        window.geometry('100x100+'+str(self.x)+'+'+str(self.y))
        label.configure(image=frame)
        window.after(1,self.event)
        
def hello(event):
    print("yes")
    
window = tk.Tk()

#window configuration
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
window.attributes('-topmost', 1)
label.bind("<Button-1>", hello)
label.pack()

axo = Pet(1000, 500)
#loop the program
window.after(1, axo.update)
window.mainloop()
