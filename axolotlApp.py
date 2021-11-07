from cmu_112_graphics import *
from axolotlClass import*

def appStarted(app):
    # images:
    mainmenu = 'https://cdn.discordapp.com/attachments/906604588247965747/906716392034811964/Untitled_Artwork_23.jpg'
    axo1 = 'https://media.discordapp.net/attachments/906604588247965747/906703597465649172/axoaxo-removebg-preview.png'
    myaxo = "https://cdn.discordapp.com/attachments/906604588247965747/906713338732486696/Untitled_Artwork_20.png"
    app.mainmenuBG = app.loadImage(mainmenu)
    app.myaxo = app.loadImage(myaxo)
    app.axo1Unscaled = app.loadImage(axo1)
    app.axo1 = app.scaleImage(app.axo1Unscaled,2/3)
    app.mainMenu = True
    app.ct = False
    app.feed = False
    app.stats = False

def drawBackground(app, canvas):
    # pink background
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.mainmenuBG))

def drawMainScreen(app, canvas):
    canvas.create_image(app.width//2,100,image=ImageTk.PhotoImage(app.myaxo))
    # Axolotl 1:
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.axo1))
    # Code T-Racing: start = (200,500) ; end = (650,750)
    canvas.create_rectangle(175,650,500, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(app.width//8+150, 700,text="Play Code T-Racing",font="Gabriola 30 bold")

    # Feed: start = (600,650) ; end = (900,750)
    canvas.create_rectangle(600,650,900, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(app.width//8+550, 700,text="Feed",font="Gabriola 30 bold")

    # Check Stats: (1000)
    canvas.create_rectangle(1000,650,1300, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(app.width//8+950, 700,text="Check Stats",font="Gabriola 30 bold")

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
    canvas.create_text(app.width//2, app.height//2,text="TESTING STATS",font="Arial 40")
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
