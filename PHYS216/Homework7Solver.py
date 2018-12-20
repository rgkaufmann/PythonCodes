import numpy as np

def LagrangePointFunction(xVal, SID):
    mu = (SID//100000)/1000
    if (mu < 0.5):
        mu += 0.5
    grad = mu*(xVal+1-mu)*(xVal+1-mu)**-3
    grad += (1-mu)*(xVal-mu)*(mu-xVal)**-3
    grad += -(1-mu)*(xVal-mu)
    grad += mu*(xVal+1-mu)
    return grad

def stepUp(lastPoint, lastLagrange, stepSize, operation, midOrNot):
    if operation == 'Add':
        newPoint = lastPoint+stepSize
        Lagrange = LagrangePointFunction(newPoint, studentID)
    elif operation == 'Subtract':
        newPoint = lastPoint-stepSize
        Lagrange = LagrangePointFunction(newPoint, studentID)
    if ((midOrNot and Lagrange < 0) or ((not midOrNot) and Lagrange > 0)):
        operation = 'Subtract'
    if ((midOrNot and Lagrange > 0) or ((not midOrNot) and Lagrange < 0)):
        operation = 'Add'
    if (np.sign(Lagrange) != np.sign(lastLagrange)):
        stepSize /= 10.
    if (np.abs(Lagrange) > np.abs(lastLagrange)):
        Lagrange = lastLagrange
        newPoint = lastPoint
    return Lagrange, newPoint, stepSize, operation

noID = True
while (noID):
    try:
        studentID = int(input("What is your student ID? "))
        if (9999999 > studentID or 100000000 < studentID):
            raise ValueError
        noID = False
    except ValueError:
        print('Value is not a proper student number. Try again.')
    
MidPoint = 0.3
LeftPoint = -1.8
RightPoint = 1.8
MidStepSize = 0.1
LeftStepSize = 0.1
RightStepSize = 0.1
MidOperation = 'Add'
LeftOperation = 'Subtract'
RightOperation = 'Subtract'
LagrangeMid = LagrangePointFunction(MidPoint, studentID)
LagrangeLeft = LagrangePointFunction(LeftPoint, studentID)
LagrangeRight = LagrangePointFunction(RightPoint, studentID)

for index in range(100000):
    LagrangeMid, MidPoint, MidStepSize, MidOperation = stepUp(MidPoint, LagrangeMid, MidStepSize, MidOperation, True)
    LagrangeLeft, LeftPoint, LeftStepSize, LeftOperation = stepUp(LeftPoint, LagrangeLeft, LeftStepSize, LeftOperation, False)
    LagrangeRight, RightPoint, RightStepSize, RightOperation = stepUp(RightPoint, LagrangeRight, RightStepSize, RightOperation, False)

print()    
print(LagrangeMid)
print(LagrangeLeft)
print(LagrangeRight)
print()
print(MidPoint)
print(LeftPoint)
print(RightPoint)