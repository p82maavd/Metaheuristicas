
    

from copy import copy
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

def randomPopulation(np,ranges):

    pop = []

    while(len(pop)!=np):
        position=[random.randrange(ranges,abs(ranges)),random.randrange(ranges,abs(ranges))]
        pop.append(position)

    return pop
    

def selfOrganizingMigration(func, ranges):
    
    m=0
    M_max=100
    npop=20
    prt=0.4
    path=3
    step=0.11
    
    pop=randomPopulation(npop,ranges)
    
    temporaryPoints = None


    while m < M_max:
     
        best = pop[0]
                
        for x in pop:
            if func(x) < func(best):
                best = x
       

        for j,x in enumerate(copy(pop)):
            
            if x!=best:
                t=0
                prtvector=[0,0]
                for w in range(0,len(x)):
                    if random.uniform(0,1) < prt:
                        prtvector[w]=1
                
                directionvector=[0,0]
               
                for w in range(0,len(x)):
                    directionvector[w]=best[w]-x[w]

                bestx=x
                #print("punto inicial",x, " mejor=",best, prtvector, directionvector)
                while t<path:
                    newposition=copy(x)

                    for p,d in enumerate(newposition):
                        #mirar lo del vector director
                        newposition[p]=d+t*prtvector[p]*directionvector[p]

                        if newposition[p] > abs(ranges):
                            newposition[p]=abs(ranges)
                        elif newposition[p] < ranges:
                            newposition[p]=ranges

                    #print(newposition)
                    
                    if func(newposition) < func(x):
                        bestx=newposition
                    
                    t+=step
                pop[j]=bestx



        if temporaryPoints != None:
            for x in temporaryPoints:
                x.remove()
        #temporaryPoints, = plt.plot(pop[0][0],pop[0][1],marker='o',color='k')
        temporaryPoints = [plt.plot(*p, marker='o', color='k')[0] for p in pop]
        plt.draw()
        plt.pause(1/5)

        m+=1
    
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig, ax = plt.subplots()
        
        showGraph(x[0], x[1], ax)
        selfOrganizingMigration(x[0], x[1])
        plt.show()

if __name__ == "__main__":
    main()


