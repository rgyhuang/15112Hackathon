from cmu_112_graphics import *
from axolotlClass import*
from PathsAndScenes import*

visualPath = os.path.dirname(os.path.dirname(__file__)) + "\\Assets\\Visuals\\"
mainmenu = visualPath+"main_menu_bg.jpg"
axo1 = visualPath+"axo1.png"
title = visualPath+"title.jpg"
codeTrButton = visualPath+"code_tracing_button.jpg"
feedButton = visualPath+"feed_button.jpg"
statb = visualPath+"stats_button.jpg"
gate = visualPath+"gate.png"
proceed = visualPath+"path.png"

axolotl = Axolotl()
def appStarted(app):
    # images:
    app.redAxo = app.loadImage(visualPath+"axo1.png")
    app.yellowAxo = app.loadImage(visualPath+"yellowAxo.jpg")
    app.greenAxo = app.loadImage(visualPath+"greenAxo.jpg")
    app.blueAxo = app.loadImage(visualPath+"blueAxo.jpg")
    app.purpleAxo = app.loadImage(visualPath+"purpleAxo.jpg")
    app.whiteAxo = app.loadImage(visualPath+"whiteAxo.png")
    app.redWorm = app.loadImage(visualPath+"redworm.jpg")
    app.yellowWorm = app.loadImage(visualPath+"yellowWorm.jpg")
    app.greenWorm = app.loadImage(visualPath+"greenWorm.jpg")
    app.blueWorm = app.loadImage(visualPath+"blueWorm.jpg")
    app.purpleWorm = app.loadImage(visualPath+"purpleWorm.jpg")
    app.whiteWorm = app.loadImage(visualPath+"whiteWorm.jpg")
    app.codeTrButton = app.loadImage(codeTrButton)
    app.pathUnsized = app.loadImage(proceed)
    app.gateUnsized = app.loadImage(gate)
    app.gate = app.scaleImage(app.gateUnsized,0.25)
    app.path = app.scaleImage(app.pathUnsized, 0.05)
    app.feedButton = app.loadImage(feedButton)
    app.statButton = app.loadImage(statb)
    app.mainmenuBG = app.loadImage(mainmenu)
    app.title = app.loadImage(title)
    app.axo1Unscaled = app.loadImage(axo1)

    app.ct1 = app.loadImage(visualPath+"ct1.jpg")
    app.ct2 = app.loadImage(visualPath+"ct2.jpg")
    app.ct3 = app.loadImage(visualPath+"ct3.jpg")
    app.ct4 = app.loadImage(visualPath+"ct4.jpg")
    app.cts = [app.ct1,app.ct2,app.ct3,app.ct4]
    app.axo1 = app.scaleImage(app.axo1Unscaled,2/3)
    app.mainMenu = True
    app.ct = False
    app.feed = False
    app.image = None
    app.stats = False
    app.eatWorm = False
    app.mouseX = 0
    app.mouseY = 0
    app.meme = app.loadImage(visualPath+"axolotlmeme.gif")
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

def backButton(app, canvas):
    canvas.create_rectangle(100,700,300, 750,
                            fill="white",outline="black",width=2)
    canvas.create_text(200, 720,text="Back",font="Gabriola 30 bold")

# Actions:
def mousePressed(app, event):
    # On main menu:
    if(app.mainMenu == True):
        app.ct = False
        app.feed = False
        app.stats = False
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
    # on Feed:
    elif(app.feed):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.feed = False
        elif(event.x >= 1110 and event.x <= 1290):
            if(event.y >= 90 and event.y<=110):
                app.red = True
                app.yellow, app.green, app.blue, app.purple, app.white = False, False, False, False, False
            elif(event.y >= 190 and event.y<=210):
                app.yellow = True
                app.red, app.green, app.blue, app.purple, app.white = False, False, False, False, False
            elif(event.y >= 290 and event.y<=310):
                app.green = True
                app.yellow, app.red, app.blue, app.purple, app.white = False, False, False, False, False
            elif(event.y >= 390 and event.y<=410):
                app.blue = True
                app.yellow, app.green, app.red, app.purple, app.white = False, False, False, False, False
            elif(event.y >= 490 and event.y <=510):
                app.purple = True
                app.yellow, app.green, app.blue, app.red, app.white = False, False, False, False, False
            elif(event.y >= 590 and event.y <=610):
                app.white = True
                app.yellow, app.green, app.blue, app.purple, app.red = False, False, False, False, False
    # on Stats:
    elif(app.stats):
        if(event.x >= 100 and event.x <= 300 and event.y >= 700 and event.y<=750):
            app.mainMenu = True
            app.stats = False
        
# # Screens:
# def drawCT(app,canvas):
#     for row in range(len(underwater.boardForScene)):
#         for col in range(0,len(underwater.boardForScene[0])):
#             cx, cy = underwater.centerGrid(row, col)
#             if underwater.boardForScene[row][col] == "G":
#                 # input image of gate at cx and cy
#                 canvas.create_image(50+cx,cy,image=ImageTk.PhotoImage(app.gate))
#             elif underwater.boardForScene[row][col] == "P":
#                 canvas.create_image(50+cx,cy,image=ImageTk.PhotoImage(app.path))
#                 # input image of path
#     drawCTProblems(app,canvas)
#     backButton(app,canvas)

def drawCTProblems(app, canvas):
    index = random.randint(0,3)
    image = app.cts[index]
    canvas.create_image(1100,400,image=ImageTk.PhotoImage(image))
    canvas.create_text(1100,100,text="Indicate what the following code prints:",font="Arial 14")
    memeIndex = random.randint(700,720)
    memeIndey = random.randint(600,610)
    canvas.create_image(memeIndex,memeIndey,image=ImageTk.PhotoImage(app.meme))
    canvas.create_text(100,40,text="CODE TRACE FASTER OR ELSE",font="Arial 60",anchor="w")
def drawFeed(app, canvas):
    canvas.create_image(1200,100,image=ImageTk.PhotoImage(app.redWorm))
    canvas.create_image(1200,200,image=ImageTk.PhotoImage(app.yellowWorm))
    canvas.create_image(1200,300,image=ImageTk.PhotoImage(app.greenWorm))
    canvas.create_image(1200,400,image=ImageTk.PhotoImage(app.blueWorm))
    canvas.create_image(1200,500,image=ImageTk.PhotoImage(app.purpleWorm))
    canvas.create_image(1200,600,image=ImageTk.PhotoImage(app.whiteWorm))
    if(app.red):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.redAxo))
        axolotl.color = "pink"
    elif(app.yellow):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.yellowAxo))
        axolotl.color = "yellow"
    elif(app.green):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.greenAxo))
        axolotl.color = "green"
    elif(app.blue):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.blueAxo))
        axolotl.color = "blue"
    elif(app.purple):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.purpleAxo))
        axolotl.color = "purple"
    elif(app.white):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.whiteAxo))
        axolotl.color = "white"
    backButton(app,canvas)
    
def drawStats(app, canvas):
    # canvas.create_text(app.width//2, app.height//2,text="TESTING STATS",font="Arial 40")
    if(app.red):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.redAxo))
        axolotl.color = "pink"
    elif(app.yellow):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.yellowAxo))
        axolotl.color = "yellow"
    elif(app.green):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.greenAxo))
        axolotl.color = "green"
    elif(app.blue):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.blueAxo))
        axolotl.color = "blue"
    elif(app.purple):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.purpleAxo))
        axolotl.color = "purple"
    elif(app.white):
        canvas.create_image(400, app.height//2,image=ImageTk.PhotoImage(app.whiteAxo))
        axolotl.color = "white"
    canvas.create_text(650, 150, text=f"Name: {axolotl.name}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 210, text=f"Color: {axolotl.color}",font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 270, text=f"Happiness:                {axolotl.happiness}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 330, text=f"Hunger:                {axolotl.hunger}",
                      font=("MV Boli",35),anchor="w")
    canvas.create_text(650, 390, text=f"Best Time: {axolotl.bestTime}",font=("MV Boli",35),anchor="w")
    backButton(app,canvas)
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
    # elif(app.ct):
    #     drawCT(app,canvas)
    elif(app.feed):
        drawFeed(app, canvas)
    elif(app.stats):
        drawStats(app,canvas)

runApp(width=1400, height=800)