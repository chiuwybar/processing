x = 0
y = 0
balloon = 0
bus = 0
def setup():
    size (640, 480)

def draw():
    global x
    global balloon
    global y
    global bus
    print (x)
    if x >= 640:
        x = 0
    x = x + 0.5
    if y >= 640:
        y = 0
    y = y + 0.5
    if balloon >= 640:
        balloon = 0
    balloon = balloon + 1
    if bus >= 640:
        bus = 0
    bus = bus + 2
    background (135, 206, 250)
    noStroke()      #remove border of outline
    fill ("#FFFFFF")
    ellipse (x, 70, 80, 80)
    ellipse (x+40, 70, 80, 80)
    ellipse (x+40, 70 + 20, 80, 80)
    ellipse (x+40, 70 -20, 80, 80)
    ellipse (x+90, 70, 80, 80)
    #cloud
       
    ellipse (y+200, 70, 80, 80)
    ellipse (y+240, 70, 80, 80)
    ellipse (y+240, 70 + 20, 80, 80)
    ellipse (y+240, 70 -20, 80, 80)
    ellipse (y+290, 70, 80, 80)
    #cloud
    
    fill ("#F7CF88")
    rect (balloon+40, 110, 4, 50)
    rect (balloon+70, 110, 4, 50)
    rect (balloon+40, 130, 30, 30)
    fill ("#FF0000")
    ellipse (balloon+60, 70, 130, 110)
    #HotAirBalloon
    
    #(x, y, width, height)
    
    fill ("#FFFF00")
    ellipse (10, 10, 200, 200)
    #sun
    
    fill ("#008000")
    rect (0, 390, 2000, 100)
    #grass
    
    fill ("#808080")
    rect (0, 400, 2000, 50)
    fill ("#FFFFFF")
    rect (0, 415, 40, 10)
    rect (60, 415, 40, 10)
    rect (120, 415, 40, 10)
    rect (180, 415, 40, 10)
    rect (240, 415, 40, 10)
    rect (300, 415, 40, 10)
    rect (360, 415, 40, 10)
    rect (420, 415, 40, 10)
    rect (480, 415, 40, 10)
    rect (540, 415, 40, 10)
    rect (600, 415, 40, 10)
    #road
    
    fill ("#F7CF88")
    rect (220, 260, 220, 130)
    # building
    
    fill("#000000")
    triangle (220, 260, 440, 260, 330, 180)
    #roof
    
    fill ("#000000")
    rect (315, 340, 30, 50)
    #door
    
    #(x, y, width, height)
    
    fill ("#ADD4DC")
    rect (240, 265, 30, 30)
    #window
    
    fill ("#ADD4DC")
    rect (390, 265, 30, 30)
    #window
    
    fill ("#D2691E")
    rect (120, 310, 30, 80)
    #tree
    
    fill ("#008000")
    ellipse (135, 275, 80, 80)
    #leaves
     
    fill ("#D2691E")
    rect (515, 310, 30, 80)
    #tree
    
    fill ("#008000")
    ellipse (530, 275, 80, 80)
    #leaves
    
    fill ("#FFD800")
    rect (bus+0, 330, 200, 90)
    fill ("#FFD800")
    rect (bus+200, 370, 50, 50)
    fill ("#000000")
    rect (bus+0, 380, 250, 10)
    ellipse (bus + 30, 420, 50, 50)
    ellipse (bus + 200, 420, 50, 50)
    rect (bus+0, 337, 35, 35)
    rect (bus+40, 337, 35, 35)
    rect (bus+80, 337, 35, 35)
    rect (bus+120, 337, 35, 35)
    rect (bus+160, 337, 35, 35)
    #Bus    

    #(x, y, width, height)
