import math
import numpy as np

def OmegaFamily(N1, q1, N2, q2):
    family1 = (q1+N1-1)*math.log(q1+N1-1)-(q1+N1-1)+0.5*math.log(2*math.pi*(q1+N1-1))
    family1 -= (q1)*math.log(q1)-q1+0.5*math.log(2*math.pi*q1)
    family1 -= (N1-1)*math.log(N1-1)-(N1-1)+0.5*math.log(2*math.pi*(N1-1))
    family2 = (q2+N2-1)*math.log(q2+N2-1)-(q2+N2-1)+0.5*math.log(2*math.pi*(q2+N2-1))
    family2 -= (q2)*math.log(q2)-q2+0.5*math.log(2*math.pi*q2)
    family2 -= (N2-1)*math.log(N2-1)-(N2-1)+0.5*math.log(2*math.pi*(N2-1))
    family1 = math.exp(family1)
    family2 = math.exp(family2)
    return family1*family2

def factorial(value):
    fact = 1
    for i in range(value):
        fact *= (i+1)
    return fact

def OmegaReal(N1, q1, N2, q2):
    family1 = factorial(q1+N1-1)/(factorial(q1)*factorial(N1-1))
    family2 = factorial(q2+N2-1)/(factorial(q2)*factorial(N2-1))
    return family1*family2

number5 = OmegaFamily(15, 12, 18, 15)
number6 = OmegaFamily(15, 9, 18, 18)

number52 = OmegaReal(15, 12, 18, 15)
number62 = OmegaReal(15, 9, 18, 18)

Results = "Multiplicity of number 5: {:d}\n".format(int(number5))
Results += "Multiplicity of number 6: {:d}\n\n".format(int(number6))

Real = "Real Multiplicity of number 5: {:d}\n".format(int(number52))
Real += "Real Multiplicity of number 6: {:d}\n\n".format(int(number62))

Accuracy = "Accuracy of number 5: {:f}\n".format(number5/number52)
Accuracy += "Accuracy of number 6: {:f}\n\n".format(number6/number62)

file = open("Attempt3.txt", "w")
file.write(Results)
file.write(Real)
file.write(Accuracy)
file.close()