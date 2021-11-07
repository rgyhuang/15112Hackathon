from cmu_112_graphics import *
from axolotlClass import*
from myAxolotl import*
from PathsAndScenes import*

mainmenu = "main_menu_bg.jpg"
axo1 = 'axo1.png'
title = "title.jpg"
codeTrButton = "code_tracing_button.jpg"
feedButton = "feed_button.jpg"
renameButton = "rename_button.jpg"
statb = "stats_button.jpg"
gate = "gate.png"
proceed = "path.png"
path = os.path.dirname(os.path.abspath(__file__)) + '\\'


def appStarted(app):
    # images:
    app.redWorm = app.loadImage("redworm.jpg")
    app.yellowWorm = app.loadImage("yellowWorm.jpg")
    app.greenWorm = app.loadImage("greenWorm.jpg")
    app.blueWorm = app.loadImage("blueWorm.jpg")
    app.purpleWorm = app.loadImage("purpleWorm.jpg")
    app.whiteWorm = app.loadImage("whiteWorm.jpg")
    app.codeTrButton = app.loadImage(codeTrButton)
    app.pathUnsized = app.loadImage(proceed)
    app.gateUnsized = app.loadImage(gate)
    app.gate = app.scaleImage(app.gateUnsized,0.25)
    app.path = app.scaleImage(app.pathUnsized, 0.05)
    app.feedButton = app.loadImage(feedButton)
    app.statButton = app.loadImage(statb)
    app.mainmenuBG = app.loadImage(mainmenu)
    app.renameButton = app.loadImage(renameButton)
    app.title = app.loadImage(title)
    app.axo1Unscaled = app.loadImage(axo1)
    app.axo1 = app.scaleImage(app.axo1Unscaled,2/3)
    app.mainMenu = True
    app.ct = False
    app.feed = False
    app.image = None
    app.stats = False
    app.eatWorm = False
    app.mouseX = 0
    app.mouseY = 0

    #worm States
    app.red = False
    app.yellow = False
    app.green = False
    app.blue = False
    app.purple = False
    app.white = False

def drawBackground(app, canvas):
    # pink background
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.mainmenuBG))

def drawMainScreen(app, canvas):
    canvas.create_image(app.width//2,100,image=ImageTk.PhotoImage(app.title))
    # Axolotl 1:
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.axo1))
    # Code T-Racing: start = (200,500) ; end = (650,750)
    canvas.create_image(350,700,image=ImageTk.PhotoImage(app.codeTrButton))

    # Feed: start = (600,650) ; end = (900,750)
    canvas.create_image(750,700,image=ImageTk.PhotoImage(app.feedButton))

    # Check Stats: (1000)
    canvas.create_image(1150,700,image=ImageTk.PhotoImage(app.statButton))

def mouseMoved(app, event):
    app.mouseX = event.x
    app.mouseY = event.y
def backButton(app, canvas):
    canvas.create_rectangle(100,700,300, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(200, 720,text="Back",font="Gabriola 30 bold")

# Actions:
def mousePressed(app, event):
    # On main menu:
    if(app.mainMenu == True):
        if(event.x >= 200 and event.x <= 500 and event.y >= 650 and event.y <= 750):
            app.ct = True
            app.mainMenu = False
        elif(event.x >= 600 and event.x <= 900 and event.y >= 650 and event.y <= 750):
            app.feed = True
            app.mainMenu = False
        elif(event.x >= 1000 and event.x <= 1300 and event.y >= 650 and event.y <= 750):
            app.stats = True
            app.mainMenu = False
    # on CT:
    elif(app.ct):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.ct = False
    elif(app.stats):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.ct = False
        elif(event.x >= 650 and event.x <= 850 and event.y >= 695 and event.y<=745):
            name = app.getUserInput("Enter a name for your axolotl: ")
            axolotl.changeName(name)
    # on Feed:
    elif(app.feed):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.feed = False
        elif(event.x >= 1110 and event.x <= 1290):
            if(event.y >= 90 and event.y<=110):
                app.red = True
            elif(event.y >= 190 and event.y<=210):
                app.yellow = True
            elif(event.y >= 290 and event.y<=310):
                app.green = True
            elif(event.y >= 390 and event.y<=410):
                app.blue = True
            elif(event.y >= 490 and event.y <=510):
                app.purple = True
            elif(event.y >= 590 and event.y <=610):
                app.white = True


        
    # on Stats:
    elif(app.stats):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.stats = False

def mouseReleased(app, event):
    if(app.feed):
        print("hi")
        if(event.x >= 450 and event.x <= 500 and event.y >= app.height//4 and event.y <= app.height//4 + 20):
            print("Eat")
            app.eatWorm = False
            app.red = False
            app.yellow = False
            app.green = False
            app.blue = False
            app.purple = False
            app.white = False
            app.feed = False
        
# Screens:
def drawCT(app,canvas):
    for row in range(len(underwater.boardForScene)):
        for col in range(0,len(underwater.boardForScene[0])):
            cx, cy = underwater.centerGrid(row, col)
            if underwater.boardForScene[row][col] == "G":
                # input image of gate at cx and cy
                canvas.create_image(50+cx,cy,image=ImageTk.PhotoImage(app.gate))
            elif underwater.boardForScene[row][col] == "P":
                canvas.create_image(50+cx,cy,image=ImageTk.PhotoImage(app.path))
                # input image of path
    drawCTProblems(app,canvas)
    backButton(app,canvas)

def drawCTProblems(app, canvas):
    canvas.create_rectangle(900,100,1400,700,fill="white")
def drawFeed(app, canvas):
    canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.axo1Unscaled))
    canvas.create_image(1200,100,image=ImageTk.PhotoImage(app.redWorm))
    canvas.create_image(1200,200,image=ImageTk.PhotoImage(app.yellowWorm))
    canvas.create_image(1200,300,image=ImageTk.PhotoImage(app.greenWorm))
    canvas.create_image(1200,400,image=ImageTk.PhotoImage(app.blueWorm))
    canvas.create_image(1200,500,image=ImageTk.PhotoImage(app.purpleWorm))
    canvas.create_image(1200,600,image=ImageTk.PhotoImage(app.whiteWorm))
    if(app.eatWorm):
        #red
        if(app.red):
            canvas.create_image(app.mouseX, app.mouseY, image=ImageTk.PhotoImage(app.redWorm))
        
    backButton(app,canvas)
def drawStats(app, canvas):
    # canvas.create_text(app.width//2, app.height//2,text="TESTING STATS",font="Arial 40")
    canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.axo1Unscaled))
    canvas.create_text(650, 150, text=f"Name: {axolotl.name}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 210, text=f"Color: {axolotl.color}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 270, text=f"Happiness:                {axolotl.happiness}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 330, text=f"Hunger:                {axolotl.hunger}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 390, text=f"Best Time: {axolotl.bestTime}",font=("MV Boli",35),anchor="w")
    backButton(app,canvas)
    canvas.create_image(750,720,image=ImageTk.PhotoImage(app.renameButton))
    # happiness bar:
    canvas.create_rectangle(900,265,1200,285,fill="white")
    canvas.create_rectangle(900,265,900 + 3*axolotl.happiness,285,fill="green")
    #hunger bar:
    canvas.create_rectangle(850,325,1150,345,fill="white")
    canvas.create_rectangle(850,325,850 + 15*axolotl.hunger,345,fill="red")

def redrawAll(app, canvas):
    drawBackground(app,canvas)
    if(app.mainMenu == True):
        drawMainScreen(app,canvas)
    elif(app.ct):
        drawCT(app,canvas)
    elif(app.feed):
        drawFeed(app, canvas)
    elif(app.stats):
        drawStats(app,canvas)

runApp(width=1400, height=800)
