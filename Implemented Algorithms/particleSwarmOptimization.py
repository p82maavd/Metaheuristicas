
    

from copy import copy, deepcopy
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

    #Code for Heatmap
    plt.pcolormesh( X, Y, Z , cmap = 'coolwarm' )
    plt.draw()

def randomPopulation(np,ranges,vmin,vmax):

    pop = []

    while(len(pop)!=np):
        position=[random.randrange(ranges,abs(ranges)),random.randrange(ranges,abs(ranges))]
        velocity=[random.uniform(vmin,vmax),random.uniform(vmin,vmax)]
        pop.append([position,velocity,position])

    return pop
    

def particleSwarmOptimization(func, ranges):
    
    m=0
    M_max=50
    npop=15
    vmin=abs(ranges)/50
    vmax=abs(ranges)/3
    c1,c2 = 2, 2
    pop=randomPopulation(npop,ranges,vmin,vmax)

    pop.sort(key=lambda w: [func(w[0])],reverse=False)

    gBest = deepcopy(pop[0][0])
    
    temporaryPoints = None


    while m < M_max:
                
        for i, x in enumerate(pop):

            #Change velocity

            r1=random.uniform(0,1)
            w=0.9-((0.5)*m)/M_max

            x[1][0]=x[1][0]*w+r1*c1*(x[2][0]-x[0][0]) + r1*c2*(gBest[0]-x[0][0]) 
            if x[1][0] > vmax:
                x[1][0]=vmax
            elif x[1][0] < vmin and x[1][0] > 0:
                x[1][0]=vmin
            elif x[1][0] > -vmin and x[1][0] < 0:
                x[1][0]=-vmin
            elif x[1][0] < -vmax:
                x[1][0]=-vmax
                

            x[1][1]=x[1][1]*w+r1*c1*(x[2][1]-x[0][1]) + r1*c2*(gBest[1]-x[0][1])
            if x[1][1] > vmax:
                x[1][1]=vmax
            elif x[1][1] < vmin and x[1][1] > 0:
                x[1][1]=vmin
            elif x[1][1] > -vmin and x[1][1] < 0:
                x[1][1]=-vmin
            elif x[1][1] < -vmax:
                x[1][1]=-vmax
            
            #Change position

            x[0][0]+=x[1][0]
            if x[0][0] > abs(ranges):
                x[0][0]=abs(ranges)
            elif x[0][0] < ranges:
                x[0][0]=ranges

            x[0][1]+=x[1][1]
            if x[0][1] > abs(ranges):
                x[0][1]=abs(ranges)
            elif x[0][1] < ranges:
                x[0][1]=ranges

            #Compare positions
            

            if func(x[0]) <= func(x[2]):
                x[2]=x[0]
                if func(x[0]) <= func(gBest):
                    gBest=deepcopy(x[0])

        if temporaryPoints != None:
            for x in temporaryPoints:
                x.remove()
        #temporaryPoints, = plt.plot(pop[0][0],pop[0][1],marker='o',color='k')
        temporaryPoints = [plt.plot(*p[0], marker='o', color='k')[0] for p in pop]
        plt.draw()
        plt.pause(1/5)

        m+=1
    plt.plot(gBest, marker='o', color='g')
    print(gBest,func(gBest))
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig, ax = plt.subplots()
        
        showGraph(x[0], x[1], ax)
        particleSwarmOptimization(x[0], x[1])
        plt.show()

if __name__ == "__main__":
    main()


