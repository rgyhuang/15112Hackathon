from cmu_112_graphics import *
from axolotlClass import*

mainmenu = "main_menu_bg.jpg"
axo1 = 'axo1.png'
title = "title.jpg"
codeTrButton = "code_tracing_button.jpg"
feedButton = "feed_button.jpg"
statb = "stats_button.jpg"
path = os.path.dirname(os.path.abspath(__file__)) + '\\'

def appStarted(app):
    # images:
    app.codeTrButton = app.loadImage(codeTrButton)
    app.feedButton = app.loadImage(feedButton)
    app.statButton = app.loadImage(statb)
    app.mainmenuBG = app.loadImage(mainmenu)
    app.title = app.loadImage(title)
    app.axo1Unscaled = app.loadImage(axo1)
    app.axo1 = app.scaleImage(app.axo1Unscaled,2/3)
    app.mainMenu = True
    app.ct = False
    app.feed = False
    app.stats = False
    app.axolotl = Axolotl("Taylor")

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

def backButton(app, canvas):
    canvas.create_rectangle(100,700,300, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(200, 720,text="Back",font="Gabriola 30 bold")

# Screens:
def drawCT(app,canvas):
    canvas.create_text(app.width//2, app.height//2,text="TESTING CT",font="Arial 40")
    backButton(app,canvas)
def drawFeed(app, canvas):
    canvas.create_text(app.width//2, app.height//2,text="TESTING FEED",font="Arial 40")
    backButton(app,canvas)
def drawStats(app, canvas):
    # canvas.create_text(app.width//2, app.height//2,text="TESTING STATS",font="Arial 40")
    canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.axo1Unscaled))
    canvas.create_text(650, 150, text=f"Name: {app.axolotl.name}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 210, text=f"Color: {app.axolotl.color}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 270, text=f"Happiness:                {app.axolotl.happiness}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 330, text=f"Hunger:                   {app.axolotl.hunger}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 390, text=f"Best Time: {app.axolotl.bestTime}",font=("MV Boli",35),anchor="w")
    backButton(app,canvas)

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
    # on Feed:
    elif(app.feed):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.feed = False
    # on Stats:
    elif(app.stats):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.stats = False

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
