
class Axolotl(object):
    def __init__(self):
        self.color = "pink"
        self.happiness = 100
        self.hunger = 20
        self.bestTime = None
        self.name = "Taylor"
        # self.age
    
    def eatWorm(self, worm):
        self.color =  worm
        if self.happiness > 95:
            self.happiness = 100
        else:
            self.happiness += 5
        if self.hunger < 20:
            self.hunger += 1
    def changeName(self,newname):
        self.name = newname

