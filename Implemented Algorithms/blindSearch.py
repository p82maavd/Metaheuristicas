
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

from functions import *

def showGraph(func,range, ax):

    x = np.linspace(range, abs(range), 50)
    y = np.linspace(range, abs(range), 50)

    X, Y = np.meshgrid(x, y)
    Z = func([X, Y])
    ax.plot_surface(X, Y, Z, linewidth=0.2, cmap='coolwarm')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

def blindSearch(func, range, ax, maxGenerations):

    generation = 0
    bestz= math.inf
    temporaryPoints = None

    while generation < maxGenerations:
        newpopulation = []
        cont=0
        while (len(newpopulation) < 10):
            x=random.uniform(range,abs(range))
            y=random.uniform(range,abs(range))
            z=func([x,y])
            newpopulation.append([x,y,z])
        newpopulation.sort(key=lambda w: [w[2]],reverse=False)
        x=newpopulation[0][0]
        y=newpopulation[0][1]
        z=newpopulation[0][2]
        if z<bestz:
            print("new best",x,y,z)
            #ax.scatter(x , y, z, marker='o', color='green')
            if temporaryPoints != None:
                temporaryPoints.remove()
            temporaryPoints, = plt.plot(x,y,z,marker='o',color='red')
            plt.draw()
            plt.pause(2)
            bestz=z     

        generation+=1
    print("Search Finished")

def main():

    functionsList = [[sphereFunction,-6], [ackleyFunction,-30], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig = plt.figure()
        
        ax = plt.axes(projection='3d')
        
        showGraph(x[0], x[1], ax)
        blindSearch(x[0], x[1], ax, 150)
        plt.show()
    

if __name__ == "__main__":
    main()


    

