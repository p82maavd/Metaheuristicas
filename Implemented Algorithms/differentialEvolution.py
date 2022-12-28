
    

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

    pop = set()

    while(len(pop)!=np):
        pop.add((random.randrange(ranges,abs(ranges)),random.randrange(ranges,abs(ranges))))

    return list(pop)
    

def differentialEvolution(func, ranges):
    
    g=0
    g_max=50
    npop=20
    mutationFactor=0.5
    crossoverRange=0.5
    dimension=2
    pop=randomPopulation(npop,ranges)
    
    temporaryPoints = None

    while g < g_max:
        
        new_pop = copy(pop)
        
        for i, x in enumerate(pop):
           
            lista= list(range(npop))
            lista.remove(i)
            r1 =random.randrange(0,len(lista))
            r1=lista[r1]
            lista.remove(r1)
            r2 =random.randrange(0,len(lista))
            r2=lista[r2]
            lista.remove(r2)
            r3 =random.randrange(0,len(lista))
            r3=lista[r3]

            v=list(range(dimension))
            for k in range(len(v)):
                v[k]=(pop[r1][k]-pop[r2][k])*mutationFactor+pop[r3][k]
                if v[k]<ranges:
                    v[k]=ranges
                elif v[k]>abs(ranges):
                    v[k]=abs(ranges)
            
            u = [0]*dimension
            j_rnd = np.random.randint(0,dimension)

            for j in range(dimension):
                if np.random.uniform(0,1) < crossoverRange or j == j_rnd:
                    u[j]=v[j]
                else:
                    u[j]=x[j]

            if func(u) <= func(x):
                new_pop[i]=u
        
        pop = copy(new_pop)
        pop.sort(key=lambda w: [func(w)],reverse=False)

        

        if temporaryPoints != None:
            for x in temporaryPoints:
                x.remove()
        #temporaryPoints, = plt.plot(pop[0][0],pop[0][1],marker='o',color='k')
        temporaryPoints = [plt.plot(*p, marker='o', color='k')[0] for p in pop]
        plt.draw()
        plt.pause(1/5)

        g+=1
        
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig, ax = plt.subplots()
        
        showGraph(x[0], x[1], ax)
        differentialEvolution(x[0], x[1])
        plt.show()

if __name__ == "__main__":
    main()


