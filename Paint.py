 #Alex Popovic
#Paint.py
#Paint Project- This program is designed to allow the user to create shapes and allow the user to enjoy in the process of drawing. It is a creative spin on Windows Paint, covering a range of tools. 

from pygame import*
from random import*
from math import*
from glob import*
from mck import*

screen=display.set_mode((1248,780))

mainpic=image.load("Pictures/GameOfThronesWallpaper17.jpg")   
loadpic=image.load("Pictures/GameOfThronesWallpaper.jpg")   #Load pic which will be seen while the rest of the code loads.
screen.blit(loadpic,(0,0))
display.flip()


init()
mixer.music.load("GameOfThronesMusic.mp3")     
mixer.music.play(-1)    #Music! Spins forever.


canvasRect=Rect(90,90,790,500)   #Define all Rectangles.
colourRect=Rect(230,700,30,30)
whitecolRect=Rect(245,750,15,15)
blackcolRect=Rect(230,750,15,15)
coloursRect=Rect(268,640,273,139)

pencilRect=Rect(15,100,50,50)
brushRect=Rect(15,155,50,50)
eraserRect=Rect(15,210,50,50)
sprayRect=Rect(15,265,50,50)
linedrawRect=Rect(15,320,50,50)
RectdrawRect=Rect(15,375,50,50)
Rectdraw2Rect=Rect(15,430,50,50)
circledrawRect=Rect(15,485,50,50)
circledrawFullRect=Rect(15,540,50,50)
polygonRect=Rect(15,595,50,50)

dropperRect=Rect(130,12,50,50)
textboxRect=Rect(185,12,50,50)
cropRect=Rect(240,12,50,50)
bucketRect=Rect(295,12,50,50)

undoRect=Rect(930,455,50,50)
redoRect=Rect(990,455,50,50)
bombRect=Rect(900,515,50,50)
loadRect=Rect(960,515,50,50)
saveRect=Rect(1020,515,50,50)
infoRect=Rect(804,623,300,85)

stampRect=Rect(560,650,220,129)
arrowRRect=Rect(750,600,40,35)
arrowLRect=Rect(550,600,40,35)


screen.blit(mainpic,(0,0))                    #Put on the main background and canvas.
draw.rect(screen,(255,255,255),canvasRect,0)

toolSel=[pencilRect,brushRect,eraserRect,sprayRect,linedrawRect,RectdrawRect,Rectdraw2Rect,circledrawRect,circledrawFullRect,polygonRect,dropperRect,textboxRect,cropRect,bucketRect] #All of the tools are drawn.
RectCol=[(160,30,0)]+[(0,0,0)]*13     #Colours! This part makes a list such that the outline for the chosen tool is always red and the others are normal black.
for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)

tool="pencil"     #Set variables such as the starting tool
size=1            #Sets the size which is controlled by the user later on.
colour=(0,0,0)    #Sets orignal colour as black.  
coords=[]         #List of coords which will be used for bucket.
polcoords=[]      #List of coords which will be used for polygon.
undolist=[]       #List for images for undo and redo to keep track of previous/"future" images. 
redolist=[]
undopos=0         #List for position to keep track of which image is where in the previous list(s).  
redopos=0
undolist.append(screen.subsurface(canvasRect).copy()) #Adds starting image of blank canvas to allow total undo-ing.
font.init()     #Start the font
comicFont=font.SysFont("ComicSansMS",20)  
comicFontSmall=font.SysFont("ComicSansMS",12) #Smaller font
info1=[" This is the Mighty Pencil tool!",      #Info box text, split into two lists to blit one under the other.
      " This is the Brush tool!",
      " You have selected the Eraser!",
      " The Spray Paint tool",
      " The Line tool.",
      " The Rectangle tool draws",
      " The Full Rectangle tool draws filled rectangles.",
      " This is the Ellipse tool.",
      " The Full Ellipse tool draws filled ellipses.",
      " The Polygon tool. Adds on the your shape,",
      " The Eyedrop tool steals the colour",
      " This is the Textbox tool!",
      " The Crop tool, it selects parts from the canvas.",
      " The Paint Bucket!",
       "                                 Stamps!!!"]
info2=[" It is used to draw free hand.",
       " Its Size is changable by scrolling the mouse.",
       " It is used to wipe undesired material.",
       " produces a spray effect changable in size.",
       " It draws lines with changeable widths.",
       " clear rectangles with different widths.",
       " ",
       " It creates ellipses of changeable widths.",
       " ",
       "  with the right click closing the shape.",
       " from any location of your choosing.",
       " It allows the user to write on the canvas.",
       " You move with the right click of the mouse.",
       " Can be very slow, but fills any space you want."]

stampcount=0                                      #Start stamp counter and load all the stamps.
stamp1=image.load("Pictures/stamp1.png")
stamp2=image.load("Pictures/stamp2.png")
stamp3=image.load("Pictures/stamp3.png")
stamp4=image.load("Pictures/stamp4.png")
stamp5=image.load("Pictures/stamp5.png")
stamp6=image.load("Pictures/stamp6.png")
stamp7=image.load("Pictures/stamp7.png")
stamp8=image.load("Pictures/stamp8.png")
stamp9=image.load("Pictures/stamp9.png")
stamp10=image.load("Pictures/stamp10.png")
stamp11=image.load("Pictures/stamp11.png")
stamp12=image.load("Pictures/stamp12.png")
stamp13=image.load("Pictures/stamp13.png")
stamp14=image.load("Pictures/stamp14.png")
stamp15=image.load("Pictures/stamp15.png")
stamp16=image.load("Pictures/stamp16.png")
stamp17=image.load("Pictures/stamp17.png")
stamp18=image.load("Pictures/stamp18.png")

stamppics=[] #stamp list to manage easily

stamppics.append(stamp1)   #add all stamps in order
stamppics.append(stamp2)
stamppics.append(stamp3)
stamppics.append(stamp4)
stamppics.append(stamp5)
stamppics.append(stamp6)
stamppics.append(stamp7)
stamppics.append(stamp8)
stamppics.append(stamp9)
stamppics.append(stamp10)
stamppics.append(stamp11)
stamppics.append(stamp12)
stamppics.append(stamp13)
stamppics.append(stamp14)
stamppics.append(stamp15)
stamppics.append(stamp16)
stamppics.append(stamp17)
stamppics.append(stamp18)
stampRectOG=screen.subsurface(stampRect).copy()  #The Rect before any stamp so that when changing the previous stamp doesnt stay behind.




draw.rect(screen,(0,0,0),bombRect,2) #More drawing.
draw.rect(screen,(0,0,0),undoRect,2)
draw.rect(screen,(0,0,0),redoRect,2)
draw.rect(screen,(0,0,0),saveRect,2)
draw.rect(screen,(0,0,0),loadRect,2)
draw.rect(screen,(0,0,0),stampRect,2)
draw.rect(screen,(0,0,0),infoRect,2)
infoRectOG=screen.subsurface(infoRect).copy()   #The Rect before any info so that when changing the previous info sentance doesnt stay behind.
draw.rect(screen,colour,colourRect,0)
draw.rect(screen,(0,0,0),blackcolRect,0)
draw.rect(screen,(255,255,255),whitecolRect,0)
draw.rect(screen,(0,0,0),(230,750,30,15),1)  #Border for black and white

screen.blit(infoRectOG,(804,623))   #Put starting info
infoPic1 = comicFontSmall.render(info1[0],True,(0,0,0))
infoPic2 = comicFontSmall.render(info2[0],True,(0,0,0))
screen.blit(infoPic1,(804,630))
screen.blit(infoPic2,(804,660))

newscreen=screen.copy()

running=True
while running:
    click = False #Keep track of everytime button is clicked or let go of.
    unclick=False
    
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False

        if evnt.type == MOUSEBUTTONDOWN :
            if evnt.button==1:
                click=True
                text=""
            if evnt.button==4:
                size+=1
            if evnt.button==5:
                size-=1
        if evnt.type == MOUSEBUTTONUP :
            if canvasRect.collidepoint(mx,my):
                newscreen = screen.copy()   #Everytime someting is done... Make a copy.
                unclick=True
        event.get()
            
    mx,my=mouse.get_pos()  #Keep track of mouse pos
    mb=mouse.get_pressed() #Keep track of mouse clicks

    if click:
        smx,smy=mx,my  #Keeps track of orignal coords of click, the stationary coords or starting coords.
        if tool=="textbox":
            textscreen=screen.copy() #If using a textbox, makes a copy so when backspacing the letters do not stay behind. There is an image to resort back to before anyt typing.

    if unclick and canvasRect.collidepoint(mx,my):
            undolist.append(screen.subsurface(canvasRect).copy()) #Everytime someting is done... Make a copy for undolist and if it was on the actual canvas, then take into account.
            undopos+=1
    
    if click and coloursRect.collidepoint(mx,my): #Changes colour when chosen on Spectrum
        colour=screen.get_at((mx,my))
        draw.rect(screen,colour,colourRect,0)
    if click and whitecolRect.collidepoint(mx,my): #Base colours, easy access.
        colour=screen.get_at((mx,my))
        draw.rect(screen,colour,colourRect,0)
    if click and blackcolRect.collidepoint(mx,my):
        colour=screen.get_at((mx,my))
        draw.rect(screen,colour,colourRect,0)

    coordsdisplay=["X-Coordinate:" + str(mx-80),   #Makes string of current coords.
                   "Y-Coordinate:" + str(my-80)]
    coordbox=Rect(1000,10,120,40)                  #Defines Rect for it.
    draw.rect(screen,(0,0,0),coordbox,0)
    TxtPic1=comicFontSmall.render(coordsdisplay[0],True,(255,255,255))  #Displays the new current coordinates 
    screen.blit(TxtPic1,(1000,10))                                   #after getting them from above
    TxtPic2=comicFontSmall.render(coordsdisplay[1],True,(255,255,255)) # Double so it ensures every moment is being caught and it isnt being skipped.
    screen.blit(TxtPic2,(1000,30))

    if click and pencilRect.collidepoint(mx,my):      #When changing tools! It changes the tool, then the colours to show which tool is selected. Also displays new info in infoRect. Also alwyas sets size back to 1.
        tool="pencil"
        RectCol=[(160,30,0)]+[(0,0,0)]*13
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[0],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[0],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and brushRect.collidepoint(mx,my):
        tool="brush"
        size=1
        RectCol=[(0,0,0)]+[(160,30,0)]+[(0,0,0)]*12
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[1],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[1],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and eraserRect.collidepoint(mx,my):
        tool="eraser"
        RectCol=[(0,0,0)]*2+[(160,30,0)]+[(0,0,0)]*11
        size=1
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[2],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[2],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and sprayRect.collidepoint(mx,my):
        tool="spray"
        size=1
        RectCol=[(0,0,0)]*3+[(160,30,0)]+[(0,0,0)]*10
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[3],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[3],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and linedrawRect.collidepoint(mx,my):
        size=1
        tool="linedraw"
        RectCol=[(0,0,0)]*4+[(160,30,0)]+[(0,0,0)]*9
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[4],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[4],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and RectdrawRect.collidepoint(mx,my):
        size=1
        tool="Rectdraw"
        RectCol=[(0,0,0)]*5+[(160,30,0)]+[(0,0,0)]*8
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[5],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[5],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and Rectdraw2Rect.collidepoint(mx,my):
        size=1
        tool="Rectdraw2"
        RectCol=[(0,0,0)]*6+[(160,30,0)]+[(0,0,0)]*7
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[6],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[6],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and circledrawRect.collidepoint(mx,my):
        size=1
        tool="circledraw"
        RectCol=[(0,0,0)]*7+[(160,30,0)]+[(0,0,0)]*6
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[7],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[7],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and circledrawFullRect.collidepoint(mx,my):
        tool="circledrawFull"
        RectCol=[(0,0,0)]*8+[(160,30,0)]+[(0,0,0)]*5
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[8],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[8],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and polygonRect.collidepoint(mx,my):
        size=1
        tool="polygon"
        RectCol=[(0,0,0)]*9+[(160,30,0)]+[(0,0,0)]*4
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[9],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[9],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and dropperRect.collidepoint(mx,my):
        tool="eyedrop"
        RectCol=[(0,0,0)]*10+[(160,30,0)]+[(0,0,0)]*3
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[10],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[10],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and textboxRect.collidepoint(mx,my):
        tool="textbox"
        slowdown=True             #Puts in a flag to slow down program so it can handle the normal typing.
        RectCol=[(0,0,0)]*11+[(160,30,0)]+[(0,0,0)]*2
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[11],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[11],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and cropRect.collidepoint(mx,my):
        tool="crop"
        RectCol=[(0,0,0)]*12+[(160,30,0)]+[(0,0,0)]*1
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[12],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[12],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
    if click and bucketRect.collidepoint(mx,my):
        tool="bucket"
        RectCol=[(0,0,0)]*13+[(160,30,0)]
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[13],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[13],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
            
    if arrowRRect.collidepoint(mx,my):   #When clicking on appropirate arrow, it changes which stamp is being looked at and the position.
        if click:
            stampcount+=1
            if stampcount>=18:
                stampcount=0
    if arrowLRect.collidepoint(mx,my):
        if click:
            if stampcount==0:
                stampcount=18
            stampcount-=1
                

    for i in range(0,19): #Keeps track of the position and ensures the correct image is being displayed with putting in a base background to erase old stamp.
        if stampcount==i:
            screen.blit(stampRectOG,(560,650))
            if stampcount<=7:
                screen.blit(stamppics[i],(560,650))
            else:
                screen.blit(stamppics[i],(630,655))
            draw.rect(screen,(0,0,0),stampRect,2)
        
    if click and stampRect.collidepoint(mx,my):  #Sets tool to stamp and changes colours to show no other tool is selected. Also shows info.
        tool="stamp"
        RectCol=[(0,0,0)]*14
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],2)
            screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[14],True,(0,0,0))
        screen.blit(infoPic1,(804,630))

    if mb[0]==1 and canvasRect.collidepoint(mx,my):    #Starts the basis for most functions in the program. If the certain tool is selected, and being clicked on the canvas, follow the code.
        screen.set_clip(canvasRect) #Sets clipping to ensure only the canvas is being changed.
        redolist=[] #Resets redo back to blank list as redo disappears when new actions are made.
        redopos=0 #Resets pos.
        
        if tool=="pencil":
            draw.line(screen,colour,(omx,omy),(mx,my),(1)) #Draw line from mouse to the old mouse location because the program is too slow to catch every movement.

        if tool=="brush":
            if size<=1:   #Ensures size of tool stays in reasonable range.
                size=1
            if size>=50:
                size=50
            distance=((mx-omx)**2+(my-omy)**2)**0.5       #Calcualte distance to fill all locations between two movements using similar triangles.
            for i in range(int(distance)):
                centrex=(i*mx+(distance-i)*omx)/distance
                centrey=(i*my+(distance-i)*omy)/distance
                draw.circle(screen,colour,(int(centrex),int(centrey)),size)
            

        if tool=="eraser": #Same as above only white for eraser.
            if size<=1:
                size=1
            if size>=50:
                size=50
            distance=((mx-omx)**2+(my-omy)**2)**0.5
            for i in range(int(distance)):
                centrex=(i*mx+(distance-i)*omx)/distance
                centrey=(i*my+(distance-i)*omy)/distance
                draw.circle(screen,(255,255,255),(int(centrex),int(centrey)),size)

        if tool=="spray":
            if size<=5:
                size=5
            if size>=50:
                size=50
            radius=size     #Produces random lcations within circle of radius size, giving a spray effect.
            nx=randint(-size,size)
            ny=randint(-size,size)
            
            if radius>=(nx**2+ny**2)**(1/2)>0:  #Makes sure random point is in circle.
                draw.circle(screen,colour,(mx+nx,my+ny),0)

        if tool=="linedraw":
            if size<=1:
                size=1
            if size>=5:
                size=5
            screen.blit(newscreen,(0,0))#Blits the screen as action is being done to show the user his movement.
            draw.line(screen,colour,(smx,smy),(mx,my),size) #Draws line from anchored point to mouse.

        if tool=="Rectdraw":
            if size<=1:
                size=1
            if size>=5:
                size=5
            screen.blit(newscreen,(0,0))
            draw.rect(screen,colour,(smx,smy,mx-smx,my-smy),size) #Draws rect from anchored point to mouse, calcualting the right dimenstions by getting the distance.

        if tool=="Rectdraw2":
            screen.blit(newscreen,(0,0))
            draw.rect(screen,colour,(smx,smy,mx-smx,my-smy),0) #^ but filled.

        if tool=="circledrawFull":
            screen.blit(newscreen,(0,0))
            draw.ellipse(screen,colour,(min(mx,smx),min(my,smy),(max(mx,smx)-min(mx,smx)),(max(my,smy)-min(my,smy))),0) #Draw an elipse but the rectangle in which it is made must always be positive so we start from the smallest coords and make a rect using positve differences.

        if tool=="circledraw":
            if size<=1:
                size=1
            if size>=5:
                size=5
            screen.blit(newscreen,(0,0))
            try:
                draw.ellipse(screen,colour,(min(mx,smx),min(my,smy),(max(mx,smx)-min(mx,smx)),(max(my,smy)-min(my,smy))),size)    #Same but full and we put a try and except so it only displays when there is no error.
            except: ''
            
        if tool=="eyedrop":
            colour=screen.get_at((mx,my))  #Takes colour of anypoiint u pick and makes it ur colour.
            screen.set_clip(None)    
            draw.rect(screen,colour,colourRect,0)
 
        if tool=="bucket":
            draw.rect(screen,(0,0,0),canvasRect,1)
            replacecol=screen.get_at((mx,my))  #Takes colour u are replacing 
            coords.append(mx)                  #Adds coords to list
            coords.append(my)
            
            if colour != replacecol:            #Ensures that the same pixel isnt being repeatly recoloured.
                while len(coords)>0:            #As long as there are coords, colour away
                    bukx = coords[0]
                    buky = coords[1]
                    del coords[:2]              #Delete coords used
                    
                    if screen.get_at((bukx,buky))==replacecol:  #If the pixel needs to be replaced, replace it.
                        screen.set_at((bukx,buky),colour)       #Replaces col
                        coords.append(bukx+1)                   #Adds coords ontop, beside, to the right and on the bottom to cover every possible point.
                        coords.append(buky)
                        coords.append(bukx-1)
                        coords.append(buky)
                        coords.append(bukx)
                        coords.append(buky+1)
                        coords.append(bukx)
                        coords.append(buky-1)

        if tool=="stamp":
            screen.blit(newscreen,(0,0))
            if stampcount<=7:
                screen.blit(stamppics[stampcount],(mx-107,my-65))  #If stamp is selected, place it, subtracting half the dimension to centre it.
            else:
                screen.blit(stamppics[stampcount],(mx-40,my-57))    #If stamp is selected, place it, subtracting half the dimension to centre it.
        screen.set_clip(None)

    if tool=="polygon" and canvasRect.collidepoint(mx,my):
        if size<1:
            size=1
        if size>5:
            size=5
        if click:
            polcoords.append((mx,my)) #Keep adding points to the list
            if len(polcoords)>1:
                draw.line(screen,colour,(polcoords[-2]),(polcoords[-1]),size)  #Draw lines between the recent and most recent points, froming a series of connected lines.
 
        if mb[2]==1 and len(polcoords)>1:  #If right click, finish the shape by connecting the first and last points, forming a closed figure and reseting the function.
            draw.line(screen,colour,(polcoords[0]),(polcoords[-1]),size)
            polcoords=[]

    if tool=="crop" and canvasRect.collidepoint(mx,my):      
        screen.set_clip(canvasRect)
        if mb[0] == 1:
            screen.blit(newscreen,(0,0))      
            cropRect = draw.rect(screen,(0,0,0),(smx,smy,mx-smx,my-smy),1) #When mouse gets clicked draw a rect, the rect u will be cropping.
            cropping = screen.subsurface(cropRect).copy()                   #Make it a surface so we can move it around
            cx,cy = cropping.get_size()                                      #Calcualte the width and height so we can centre it when placing.                                           
            
        elif mb[2] == 1 and cropRect.collidepoint((smx,smy)):         #When rightclicking on the rect the user just made.
            screen.blit(newscreen,(0,0))
            screen.subsurface(cropRect).fill((255,255,255))         #Fill past location with clear box, taking away everything. 
            screen.blit(cropping,(mx-cx//2,my-cy//2))               #Places the cropped Rect where ever the user wants with it being centered.
            
        screen.set_clip(None)
            
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)              
        if tool=="textbox":
            keys=key.get_pressed()                       #Keeps track of they keyboard
            if keys.index(1)<300 and slowdown:  #Use flag to slowdown pyton and get accurate keys.
                if keys.index(1)==8:               #Keeps track of backspace
                    if len(text)>=1:
                      text=text[:-1]               #Delete most recent letter/space
                      screen.blit(textscreen,(90,90),canvasRect)  #Puts back screen before any typing so when the text is added the erased letter is gone.
                else:
                    text+=chr(keys.index(1))  #Adds on to string.
                slowdown=False
            if keys.index(1)==300 and slowdown==False:              #Makes sure the flag works by keeping it on before typing, only turning it off when off the tool.
                slowdown=True                                
            textRec = comicFont.render(text, True, (colour))
            screen.blit(textRec,(smx,smy))                          #Puts the new text.
        screen.set_clip(None)

    if click and bombRect.collidepoint(mx,my):             #Makes a new page by drawing a brand new white canvas, resets the tool to pencil and dhanges the selection, changing everything back to "new"
        draw.rect(screen,(255,255,255),canvasRect,0)
        screen.set_clip(None)
        RectCol=[(160,30,0)]+[0,0,0]*13
        for i in range(14):
            draw.rect(screen,RectCol[i],toolSel[i],1)
        tool="pencil"

        screen.blit(infoRectOG,(804,623))
        infoPic1 = comicFontSmall.render(info1[0],True,(0,0,0))
        infoPic2 = comicFontSmall.render(info2[0],True,(0,0,0))
        screen.blit(infoPic1,(804,630))
        screen.blit(infoPic2,(804,660))
        undolist.append(screen.subsurface(canvasRect).copy())     #Adds to undo to allow reversal.
        undopos+=1
        newscreen = screen.copy()

    if click and undoRect.collidepoint(mx,my):
        if len(undolist)>1:
            screen.blit(undolist[undopos-1],(90,90))  #Blits previous image
            redolist.append(undolist[undopos])        #Adds the image to redo in case of reversal  
            if len(undolist)>1:      #doesnt delete last pic (empty screen)
                del undolist[undopos] #gets rid of from undo to allow cycle to continue
            undopos-=1   #Changes pos to follow suit.
            redopos+=1
            newscreen = screen.copy() #Ensures the orignial picture of canvas (before next function) is updated.

    if click and redoRect.collidepoint(mx,my):
        if len(redolist)>0:
            screen.blit(redolist[redopos-1],(90,90)) #Blits Previous Image.
            undolist.append(redolist[redopos-1])     #Adds the image to undo in case of reversal
            del redolist[redopos-1]                  #Gets rid of from redo to allow cycle to continue
            redopos-=1                           #Changes pos to follow suit.
            undopos+=1
            newscreen = screen.copy() #Ensures the orignial picture of canvas (before next function) is updated.

    if click and saveRect.collidepoint(mx,my):
        savename = getName(screen) #Gets the text that the user entered
        if "." not in savename:
            savename+=".png"   #adds format if non is specified
        dotpos=savename.index(".")
        if savename[dotpos+1:] not in ["bmp","tga","png","jpeg"]:   #makes sure program will not crash with unknown format
            savename-=savename[dotpos+1:]
            savename+=".png"
        image.save(screen.subsurface(canvasRect),savename) #Saves the text as the file name the user provided

    if click and loadRect.collidepoint(mx,my):
        try:                                  #Only loads if it works and actual image is being taken. To ensure program doesnt crash with bad pic or wrong name.
            loadname = getName(screen)          #Gets the text that the user entered
            loadimage=image.load(loadname)           #Loads the image of the filename that the user enetered
            screen.blit(loadimage,(80,80))    #Blits the image on the screen
        except:
            ''

            
    omx,omy=mx,my  #Keeps track of old coords, for pencil.

    display.flip()
quit()
