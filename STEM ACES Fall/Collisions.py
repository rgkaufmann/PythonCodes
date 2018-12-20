import numpy as np
import matplotlib.pyplot as plt

class Particle:
    xPos = 0
    yPos = 0
    xVel = 0
    yVel = 0
    color = (0, 0, 0)
    
    def __init__(self, xPos=0, yPos=0, xVel=0, yVel=0):
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.color = tuple(np.random.randint(0, 256, size=3)/255)
    
    def getXPos(self):
        return self.xPos
    
    def getYPos(self):
        return self.yPos
    
    def getXVel(self):
        return self.xVel
    
    def getYVel(self):
        return self.yVel
    
    def getPosition(self):
        return (self.xPos, self.yPos)
    
    def getVelocity(self):
        return (self.xVel, self.yVel)
    
    def getColor(self):
        return self.color
    
    def setXPos(self, xPos):
        self.xPos = xPos
    
    def setYPos(self, yPos):
        self.yPos = yPos
    
    def setXVel(self, xVel):
        self.xVel = xVel
        
    def setYVel(self, yVel):
        self.yVel = yVel
    
    def plotParticle(self):
        plt.scatter(self.xPos, self.yPos, c=self.color)
        
