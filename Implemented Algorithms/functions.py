
from cmath import sqrt
import math 
import numpy as np

def sphereFunction(solution):
    sum = 0

    for x in solution:
        sum += x * x

    return sum

def ackleyFunction(solution, a = 20, b = 0.2, c = 2 * math.pi):
    sumsquare = 0
    sumcos = 0

    for x in solution:
        sumsquare += x * x
        sumcos += np.cos(c*x)

    return -a * (math.e ** (-b * np.sqrt(sumsquare/len(solution)))) - (math.e ** (sumcos/len(solution))) + a + math.e

def rastriginFunction(solution):
    sum = 0

    for x in solution:
        sum += x * x - 10*np.cos(2*math.pi*x) 
    
    return 10*len(solution) + sum

def rosenbrockFunction(solution):
    sum = 0
    
    for x in range(len(solution)-1):
        sum += 100 * ((solution[x+1] - (solution[x]**2)) ** 2) + ((solution[x] - 1) ** 2)
    
    return sum

def griewankFunction(solution):
    sum=0
    mult=1

    for x in range(len(solution)):
        sum += (solution[x] ** 2) / 4000
        mult *= np.cos(solution[x]/np.sqrt(x+1))

    return sum - mult + 1

def schwefelFunction(solution):
    sum = 0
    
    for x in solution:

        sum += x * np.sin(np.sqrt(np.abs(x)))
    
    return 418.9829*len(solution) - sum

def auxLevy(number):
    return 1 + (number-1)/4

def levyFunction(solution): 
    sum = 0

    for x in range(len(solution)-1):
        sum += (auxLevy(solution[x]-1) ** 2) * (1+10*(np.sin(math.pi*auxLevy(solution[x]) + 1) ** 2)) +  (auxLevy(solution[-1]-1) ** 2) * (1+(np.sin(2*math.pi*auxLevy(solution[-1])) ** 2))


    return (np.sin(math.pi * auxLevy(solution[0])) ** 2) + sum

def michalewiczFunction(solution,m=10):
    sum = 0
    for x in range(len(solution)):
        sum += np.sin(solution[x])*(np.sin(x*(solution[x]**2)/math.pi) ** (2*m))
    return -sum

def zakharovFunction(solution):
    sumsquare = 0
    sumhalf = 0

    for x in range(len(solution)):
        sumsquare += (solution[x] ** 2)
        sumhalf += 0.5 * x * solution[x]

    return sumsquare + (sumhalf ** 2) + (sumhalf ** 4)





