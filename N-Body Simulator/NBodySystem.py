import sys
sys.path.append('/Users/ryank/Desktop/Work/Classes/Coding Projects/Python/N-Body Simulator')
import NBodyParticle as particle

class sysOfObj:
    listOfObjs = []
    timeStep = 0        #seconds
    
    def __init__(self, dt, numOfObjs):
        try:
            self.timeStep = float(dt)
            if not (self.setUpObjs(int(numOfObjs))):
                print('Values given are not of the correct type or unreasonable.')
        except (ValueError, TypeError):
            print('Values given are not of the correct type.')
            
    def setUpObjs(self, numOfObjs):
        if numOfObjs>=1:
            for index in range(numOfObjs):
                try:
                    mass = float(input('What is the mass of the object in kg? '))
                    posx = float(input('What is the x-position of the object in m? '))
                    velx = float(input('What is the x-velocity of the object in m/s? '))
                    self.listOfObjs.append(particle.physicalObj(mass,
                                                                [posx],
                                                                [velx]))
                except (ValueError, TypeError):
                    return False
            return True
        else:
            return False
        
    def updateObjs(self):
        for Obj in self.listOfObjs:
            if not (Obj.updateForce(self.listOfObjs)):
                return False
        for Obj in self.listOfObjs:
            if not (Obj.applyForce(self.timeStep)):
                return False
        return True
    
    def getPositions(self):
        listOfPos = []
        for Obj in self.listOfObjs:
            listOfPos.append(Obj.getPosition()[0])
        return listOfPos
    
    def getVelocities(self):
        listOfVel = []
        for Obj in self.listOfObjs:
            listOfVel.append(Obj.getVelocity()[0])
        return listOfVel
    
    def getObjects(self):
        return self.listOfObjs
    
    def getTime(self):
        return self.timeStep