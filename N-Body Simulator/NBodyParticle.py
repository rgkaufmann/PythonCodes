import numpy as np

global GRAVITATIONAL
GRAVITATIONAL = 6.674e-11   #Newton meters squared per kilograms squared

class physicalObj:
    mass = 0.0                  #kilograms
    position = 0.0              #meters
    velocity = 0.0              #meters per second
    netForce = 0.0              #Newtons
    
    def __init__(self, mass, pos, vel):
        try:
            self.mass = float(mass)
            self.position = np.array([float(i) for i in pos])
            self.velocity = np.array([float(i) for i in vel])
            self.netForce = np.zeros(len(pos))
        except (ValueError, TypeError):
            print("An unexpected error has occurred. Values do not seem to be of proper type")
        
    def setMass(self, mass):
        try:
            self.mass = float(mass)
            return True
        except (ValueError, TypeError):
            return False
    
    def setPosition(self, pos):
        try:
            self.position = np.array([float(i) for i in pos])
            return True
        except (ValueError, TypeError):
            return False
        
    def setVelocity(self, vel):
        try:
            self.velocity = np.array([float(i) for i in vel])
            return True
        except (ValueError, TypeError):
            return False
    
    def getMass(self):
        return self.mass
    
    def getPosition(self):
        return self.position
        
    def getVelocity(self):
        return self.velocity
    
    def getNetForce(self):
        return self.netForce
    
    def updateForce(self, listOfObj):
        try:
            self.netForce = np.zeros(len(self.position))
            for Obj in listOfObj:
                if (self.position != Obj.getPosition()):
                    self.netForce +=  Obj.grabForce(self.position, self.mass)
            return True
        except (ValueError, TypeError):
            return False
        
    def applyForce(self, dt):
        try:
            self.position += self.velocity*float(dt)
            self.velocity += self.netForce/self.mass*float(dt)
            return True
        except (ValueError, TypeError):
            return False
    
    def grabForce(self, pos, mass):
        distanceMod = self.position-pos
        return GRAVITATIONAL*self.mass*mass/(sum(np.square(distanceMod))**(3/2))*distanceMod