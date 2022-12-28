
    

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

def randomPopulation(np,ranges):

    pop = []

    while(len(pop)!=np):
        position=[random.randrange(ranges,abs(ranges)),random.randrange(ranges,abs(ranges))]
        pop.append(position)

    return pop
    

def teachingLearningBasedOptimitazion(func, ranges):
    
    g=0
    G_max=50
    npop=20
    
    
    pop=randomPopulation(npop,ranges)
    
    temporaryPoints = None


    while g < G_max:

        #Teaching Phase
        mean=[0]*len(pop[0])
        
        for x in pop:
            for i in range(len(x)):
                mean[i]+=x[i]
        
        for i in range(len(mean)):
            mean[i]/=len(pop)
        
        pop.sort(key=lambda w: [func(w)],reverse=False)
        teacher=deepcopy(pop[0])
        r=random.uniform(0,1)
        tf=random.randint(1,2)
        
        difference=[0]*len(pop[0])

        for i in range(len(difference)):
            difference[i] = r * (teacher[i]-tf*mean[i])
        
        newteacher=deepcopy(teacher)

        for i in range(len(newteacher)):
            newteacher[i]=teacher[i]+difference[i]
            if newteacher[i] > abs(ranges):
                newteacher[i]=abs(ranges)
            elif newteacher[i] < ranges:
                newteacher[i]=ranges

        if func(newteacher)<func(teacher):
            pop[0]=deepcopy(newteacher)

        #Learning Phase
        for i in range(len(pop)):

            while True:
                j = random.randint(0,len(pop)-1)
                if j!=i:
                    break

            newlearner=deepcopy(pop[i])

            if func(pop[i]) < func(pop[j]):
                for x in range(len(pop[i])):
                    newlearner[x]+=r*(pop[i][x]-pop[j][x])
                    if newlearner[x] > abs(ranges):
                        newlearner[x]=abs(ranges)
                    elif newlearner[x] < ranges:
                        newlearner[x]=ranges

            else:
                for x in range(len(pop[i])):
                    newlearner[x]+=r*(pop[j][x]-pop[i][x])
                    if newlearner[x] > abs(ranges):
                        newlearner[x]=abs(ranges)
                    elif newlearner[x] < ranges:
                        newlearner[x]=ranges

            

            if func(newlearner) < func(pop[i]):
                pop[i]=deepcopy(newlearner)

            
        if temporaryPoints != None:
            for x in temporaryPoints:
                x.remove()
        #temporaryPoints, = plt.plot(pop[0][0],pop[0][1],marker='o',color='k')
        temporaryPoints = [plt.plot(*p, marker='o', color='k')[0] for p in pop]
        plt.draw()
        plt.pause(1/10)

        g+=1
    
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig, ax = plt.subplots()
        
        showGraph(x[0], x[1], ax)
        teachingLearningBasedOptimitazion(x[0], x[1])
        plt.show()

if __name__ == "__main__":
    main()


