## Mario Jerez
## Mini Project
## Space Impact
import os
os.chdir("/Users/mariojerez/Documents/Computer Science/MarioMiniProject")
from graphics import *
import math, time, random

##Button code borrowed from class
class Button:

    # constructor
    def __init__(self, win, graphicsObject, color, label):
        graphicsObject.setFill(color)
        graphicsObject.draw(win)
        centerPoint = graphicsObject.getCenter()
        text = Text(centerPoint, label)
        text.draw(win)
        # information Button objects need to remember:
        self.graphicsObject = graphicsObject
        self.color = color
        self.label = label

    def __str__(self):
        s = "{:s} Button".format(self.label)
        return s

    def press(self):
        self.graphicsObject.setFill("gray")
        time.sleep(0.2)
        self.graphicsObject.setFill(self.color)
        
#---------------------------------------------------------------------
# RoundButton inherits from Button

class RoundButton(Button):

    def __init__(self, win, centerX, centerY, diameter, color, label):
        radius = diameter/2
        circle = Circle(Point(centerX, centerY), radius)
        Button.__init__(self, win, circle, color, label)
        # information RoundButton objects need to remember:
        self.x = centerX
        self.y = centerY
        self.radius = radius

    def contains(self, point):
        pointX = point.getX()
        pointY = point.getY()
        distance = math.sqrt((pointX - self.x)**2 + (pointY - self.y)**2)
        if distance <= self.radius:
            return True
        else:
            return False

#---------------------------------------------------------------------
# SquareButton inherits from Button

class SquareButton(Button):

    def __init__(self, win, centerX, centerY, size, color, label):
        leftX = centerX - size/2
        rightX = centerX + size/2
        topY = centerY - size/2
        bottomY = centerY + size/2
        rect = Rectangle(Point(leftX, bottomY), Point(rightX, topY))
        Button.__init__(self, win, rect, color, label)
        # information SquareButton objects need to remember:
        self.x1 = leftX
        self.x2 = rightX
        self.y1 = topY
        self.y2 = bottomY

    def contains(self, point):
        pointX = point.getX()
        pointY = point.getY()
        if (pointX >= self.x1 and pointX <= self.x2 and
            pointY >= self.y1 and pointY <= self.y2):
            return True
        else:
            return False

#---------------------------------------------------------------------
# ButtonPanel extends GraphWin, so all GraphWin methods, including
# setBackground, getMouse, close, etc. are inherited by ButtonPanel

class ButtonPanel(GraphWin):

    def __init__(self, title, width, height):
        GraphWin.__init__(self, title, width, height)
        self.allButtons = []
        self.buttonFunctions = {}

    def addButton(self, button, callbackFunction):
        self.allButtons.append(button)
        self.buttonFunctions[button] = callbackFunction

    def processEvent(self, point):
        for button in self.allButtons:
            if button.contains(point) == True:
                callbackFunction = self.buttonFunctions[button]
                callbackFunction()
                return True
        return False

#---------------------------------------------------------------------
# main program

def main():
    panel = ButtonPanel("Space Impact", 300, 300)
    panel.setBackground("dark gray")

    # create the buttons
    b1 = RoundButton(panel, 100, 100, 50, "green", "Play Now")
    b2 = RoundButton(panel, 200, 100, 50, "red", "Scores")
    b3 = SquareButton(panel, 220, 180, 55, "orange", "quit")

    # create the callback functions
    def HighScores():
        f = open('scores.txt')
        allLines = f.readlines()
        f.close()
        scores = []
        addSpace = 0
        for line in allLines:
            scores.append(line)
        for score in scores:
            message = Text(Point(150,200 + addSpace), score)
            message.setTextColor('white')
            message.setSize(10)
            message.draw(panel)
            addSpace = addSpace + 10

    def playGame():
        game = SpaceImpact()
        game.play()

    def close():
        panel.close()

    # add the buttons to the panel
    panel.addButton(b1, playGame)
    panel.addButton(b2, HighScores)
    panel.addButton(b3, close)

    # event loop
    while panel.isClosed() == False:
        p = panel.getMouse()
        buttonPressed = panel.processEvent(p)
        if buttonPressed == False:
            message.setText("Click a button")

#-----------------------------------------------------------------

class Heart(Polygon):

    def __init__(self, win, center, size):
        x = center.getX()
        y = center.getY()
        self.win = win
        unit = size #unit is the number of pixels in a unit
        p1 = Point(x, y-unit/2)
        p2 = Point(x + unit, y - unit*1.5)
        p3 = Point(x + unit*2, y - unit/2)
        p4 = Point(x + unit, y + unit/2)
        p5 = Point(x, y + unit*1.5)
        p6 = Point(x - unit, y + unit/2)
        p7 = Point(x - unit*2, y - unit/2)
        p8 = Point(x - unit, y - unit*1.5)
        Polygon.__init__(self, p1, p2, p3, p4, p5, p6, p7, p8)
        self.setFill('red')
        self.draw(self.win)
        self.alive = True
        

    def die(self):
        self.setFill('dim gray')
        self.alive = False

    def revive(self):
        self.setFill('red')
        self.alive = False

#-------------------------------------------------------------------------

class Spaceship(Rectangle):

    def __init__(self, win, RGB, centerPoint, width, height, shootRate, movePixels, lives):
        p1 = Point(centerPoint.getX() - width / 2, centerPoint.getY() + height / 2)
        p2 = Point(centerPoint.getX() + width / 2, centerPoint.getY() - height / 2)
        Rectangle.__init__(self, p1, p2)
        self.RGB = RGB
        self.r, self.g, self.b = self.RGB[0], self.RGB[1], self.RGB[2]
        self.setFill(color_rgb(self.r, self.g, self.b))
        self.setOutline(color_rgb(self.r, self.g, self.b))
        self.draw(win)
        self.win = win
        self.center = centerPoint
        self.width = width
        self.height = height
        self.shootRate = shootRate
        self.health = lives
        self.movePixels = movePixels
        
    def leftEdge(self):
        p1 = self.getP1()
        leftBound = p1.getX()
        return leftBound

    def rightEdge(self):
        p2 = self.getP2()
        rightBound = p2.getX()
        return rightBound

    def topEdge(self):
        p2 = self.getP2()
        topBound = p2.getY()
        return topBound

    def bottomEdge(self):
        p1 = self.getP1()
        bottomEdge = p1.getY()
        return bottomEdge

    def isDestroyed(self):
        destroyed = False
        if self.health == 0:
            destroyed = True
        return destroyed
    
    def hurt(self):
        self.setFill('gray')
        self.health = self.health - 1

        ## lighten color to suggest weakened structure
        self.RGB = lighten(self.RGB)
        self.r, self.g, self.b = self.RGB[0], self.RGB[1], self.RGB[2]
        self.setFill(color_rgb(self.r, self.g, self.b))
        self.setOutline(color_rgb(self.r, self.g, self.b))

    def reachedAtmosphere(self):
        p1 = self.getP1()
        x = p1.getX()
        if x <= 0:
            return True
        else:
            return False

    def shoot(self):
        
        misile = Rocket(self.win, Point(self.leftEdge(), self.topEdge() + self.height / 2),self.height / 5, 'orange', 'left', random.uniform(-4,4))
        return misile

#--------------------------------------------------------------------------
# Used to lighten the color of the ships when they are hit        
def lighten(RGB):
    for i in range(len(RGB)):
        newIntensity = RGB[i] + 30
        if newIntensity > 255:
            newIntensity = 255
        RGB[i] = newIntensity
    return RGB

#-------------------------------------------------------------------------

class Rocket(Circle):
    def __init__(self, win, center, radius, color, dxDirection, dy):
        Circle.__init__(self, center, radius)
        xDirection = 1
        if dxDirection == 'left':
            xDirection = -1
        elif dxDirection == 'right':
            pass   
        dxSlow = 45 * xDirection
        dxFast = 50 * xDirection
        dxSuper = 55 * xDirection
        dxSuperSlow = 5 * xDirection
        colorToSpeed = {'red': dxSlow, 'blue': dxFast, 'purple': dxSuper, 'orange': dxSuperSlow}

        self.xDirection = dxDirection
        self.radius = radius
        self.setFill(color)
        self.setOutline(color)
        self.draw(win)
        self.win = win
        if color in colorToSpeed:
            self.dx = colorToSpeed[color]
        else:
            self.dx = dxSlow
        self.dy = dy

    def leftEdge(self):
        xCoord = self.getCenter().getX()
        leftBound = xCoord - self.radius
        return leftBound

    def rightEdge(self):
        xCoord = self.getCenter().getX()
        rightBound = xCoord + self.radius
        return rightBound

    def topEdge(self):
        yCoord = self.getCenter().getY()
        topBound = yCoord - self.radius
        return topBound

    def bottomEdge(self):
        yCoord = self.getCenter().getY()
        bottomBound = yCoord + self.radius
        return bottomBound

    def move(self):
        if self.topEdge() <= 0 or self.bottomEdge() >= self.win.getHeight():
            self.dy = self.dy * -1
        Circle.move(self, self.dx, self.dy)

    def checkContact(self, ships, invaders, misiles):
        contact = False
        fatal = False
        if len(ships) == 0:
            pass 
        else:
            for ship in ships:
                
                fatal = False
                x1 = ship.getP1().getX() # left edge of ship
                y1 = ship.getP1().getY() # bottom edge of ship
                x2 = ship.getP2().getX() # right edge of ship
                y2 = ship.getP2().getY() # top edge of ship
                contact = False
        
                if (self.rightEdge() >= x1 and self.leftEdge() <= x2
                    and self.topEdge() <= y1 and self.bottomEdge() >= y2):
                    contact = True
                    self.undraw()
                    misiles.remove(self)
                    ship.hurt()
                    if ship.isDestroyed() == True:
                        fatal = True
                        ship.undraw()
                        ships.remove(ship)
                        if ship in invaders:
                            invaders.remove(ship)

        return contact, misiles, ships, invaders, fatal
    
#--------------------------------------------------------------

class SpaceImpact(GraphWin):

    def __init__(self):
        GraphWin.__init__(self, "Space Impact", 800, 500)
        self.width = 800
        self.height = 500
        spacePic = Image(Point(400,250), 'space.gif')
        spacePic.draw(self)
        self.ship = Spaceship(self,[0,0,255],Point(100,250),50,20,8,20,5)

        ##draw hearts
        numHeartsDrawn = 0
        self.hearts = []
        self.deadHearts = []
        for _ in range(self.ship.health):
            size = 5
            heart = Heart(self, Point(self.width - 4*size - 25*numHeartsDrawn, size*4), size)
            self.hearts.append(heart)
            numHeartsDrawn = numHeartsDrawn + 1
        self.aliveHearts = self.hearts
            
        self.invaders = []
        self.misiles = []
        self.kills = 0
        self.myBullet = 'red'
        self.invaderRate = 50

    def highScores(self):
        f = open('scores.txt')
        allLines = f.readlines()
        f.close()
        scores = []
        addSpace = 0
        for line in allLines:
            scores.append(line)
        for score in scores:
            message = Text(Point(400,250 + addSpace), score)
            message.setTextColor('white')
            message.setSize(20)
            message.draw(self)
            addSpace = addSpace + 50

    def play(self):
        prompt = Text(Point(400,400), "Click the mouse to begin. The fate of humanity is in your hands.")
        prompt.setSize(20)
        prompt.setTextColor('white')
        prompt.draw(self)
        self.getMouse()  # wait for a mouse click to begin
        prompt.undraw()
        timeStep = 0
        ships = [self.ship]
        while self.gameOver() == False:
            if len(self.aliveHearts) < self.ship.health:
                heart = self.deadHearts[0]
                heart.revive()
                self.deadHearts.remove(heart)
                self.aliveHearts.append(heart)

            if len(self.aliveHearts) > self.ship.health:
                heart = self.aliveHearts[0]
                heart.die()
                self.aliveHearts.remove(heart)
                self.deadHearts.append(heart)

            key = self.checkKey()
            if key == 'Up' and key == 'Right':
                self.ship.move(self.ship.movePixels * -1, self.ship.movePixels)
            elif key == 'Down' and key == 'Right':
                self.ship.move(self.ship.movePixels, self.ship.movePixels)
            elif key == 'Up' and key == 'Left':
                self.ship.move(self.ship.movePixels * -1, self.ship.movePixels * -1)
            elif key == 'Down' and key == 'Left':
                self.ship.move(self.ship.movePixels, self.ship.movePixels * -1)
            elif key == 'Up':
                self.ship.move(0, self.ship.movePixels * -1)
            elif key == 'Down':
                self.ship.move(0, self.ship.movePixels)
            elif key == 'Left':
                self.ship.move(self.ship.movePixels * -1, 0)
            elif key == 'Right':
                self.ship.move(self.ship.movePixels, 0)
            elif key == 'space':
                misile = Rocket(self, Point(self.ship.rightEdge(), self.ship.topEdge() + self.ship.height / 2),self.ship.height / 5, self.myBullet, 'right', 0)
                self.misiles.append(misile)
            for misile in self.misiles:
                if misile.xDirection == 'right' and misile.leftEdge() <= self.getWidth():
                    misile.move()
                elif misile.xDirection == 'left' and misile.rightEdge() >= 0:
                    misile.move()
                else:
                    misile.undraw()
                    self.misiles.remove(misile)
                contact, self.misiles, ships, self.invaders, fatal = misile.checkContact(ships, self.invaders, self.misiles)
                if contact == True:
                    if fatal == True:
                        self.kills = self.kills + 1

            if self.kills < 5:
                shootRate = random.randrange(100,140) #make shootrate a ship object
                lives = 5
            elif self.kills < 10:
                shootRate = random.randrange(80,100)
                lives = 7
                self.myBullet = 'blue'
            else:
                shootRate = random.randrange(70,90)
                lives = 10
                self.myBullet = 'purple'
            
            if timeStep % 100 == 0:
                invader = Spaceship(self, [0,200,0], Point(self.getWidth(), random.randrange(5,self.getHeight() - 5)), 50, 20, shootRate, random.randrange(2,4), lives) 
                self.invaders.append(invader)
                ships.append(invader)
            for invader in self.invaders:
                invader.move(-invader.movePixels, 0)
                if timeStep % 80 == 0:
                    self.misiles.append(invader.shoot())

            if timeStep % 1000 == 0:
                for invader in self.invaders:
                    invader.movePixels = invader.movePixels + random.uniform(1,2)
                    self.invaderRate = self.invaderRate - 2
            
            timeStep = timeStep + 1
            time.sleep(0.01)
        self.aliveHearts[0].die()
        message = Text(Point(400, 100), 'GAME OVER! ALIENS INVADED EARTH!\nKills: {:d}\n Click anywhere to continue'.format(self.kills))
        message.setSize(25)
        message.setTextColor('white')
        message.draw(self)
        self.highScores()
        self.getMouse()
        self.close()


    def gameOver(self):
        gameIsOver = False
        for invader in self.invaders:
            if invader.reachedAtmosphere() or self.ship.isDestroyed():
                gameIsOver = True  
        return gameIsOver
        
    
