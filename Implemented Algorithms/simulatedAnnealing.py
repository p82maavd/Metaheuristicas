
    

import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

from functions import *

def showGraph(func,range, ax):

    # Clarification: Range is a negative number
    x = np.linspace(range, abs(range), 50)
    y = np.linspace(range, abs(range), 50)

    X, Y = np.meshgrid(x, y)
    Z = func([X, Y])
    ax.plot_surface(X, Y, Z, linewidth=0.1, cmap='coolwarm')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    #Code for Heatmap
    #plt.pcolormesh( X, Y, Z , cmap = 'coolwarm' )
    #plt.show()
    

def simulatedAnnealing(func, range, fig):

    t_0 = 100
    t_min = 0.5
    alpha = 0.95
    bestz= math.inf


    t = t_0
    
    temporaryPoints = None

    x=random.randrange(range,abs(range))
    y=random.randrange(range,abs(range))
    z=func([x,y])

    while t > t_min:
        print("Temp is: ", t)
        auxx = x
        auxy = y 
        auxz = z
    
        while True:
            neighbourSize=abs(range)*0.1

            change = np.random.normal([x,y],neighbourSize)

            # Check if the change gets out of our axis range and generate changes till one is valid.            
            for cord in change:
                if cord <= abs(range) and cord > range:
                    continue
                else:
                    break
            else:
                break
        
        auxx=change[0]
        auxy=change[1]

        auxz=func([auxx,auxy])

        if auxz<bestz:
            x, y, z = auxx, auxy, auxz
            print("new best",x,y,z)
            #ax.scatter(x , y, z, marker='o', color='green')
            if temporaryPoints != None:
                temporaryPoints.remove()
            temporaryPoints, = plt.plot(x,y,z,marker='o',color='k')
            plt.draw()
            plt.pause(1)
            bestz=z
        else:
            r = random.uniform(0,1)

            if r < pow(math.e,-((auxz-z)/t)):
                x, y, z = auxx, auxy, auxz
                print("new solution",x,y,z)
                #ax.scatter(x , y, z, marker='o', color='green')
                if temporaryPoints != None:
                    temporaryPoints.remove()
                temporaryPoints, = plt.plot(x,y,z,marker='o',color='k')
                plt.draw()
                plt.pause(1)
                bestz=z

        t=t*alpha
        
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        #fig, ax = plt.subplots()

        showGraph(x[0], x[1], ax)
        simulatedAnnealing(x[0], x[1], ax)
        plt.show()

if __name__ == "__main__":
    main()


