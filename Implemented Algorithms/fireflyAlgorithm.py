
    

from copy import deepcopy
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
    

def initialPopulation(np,ranges):

    pop = []

    while(len(pop)!=np):
        position=[random.randrange(ranges,abs(ranges)),random.randrange(ranges,abs(ranges))]
        pop.append(position)

    return pop

def fireflyAlgorithm(func, ranges, fig):

    print("Start Search")
    t=0
    maxGeneration=100
    temporaryPoints = None
    n=10
    alpha=0.3

    population = initialPopulation(n,ranges)
    

    while t < maxGeneration:
      
        for i in range(len(population)):
            for j in range(len(population)):
                if i !=j:
                    if func(population[i]) < func(population[j]):
                        #Move j to i.
                        for k in range(len(population[j])):
                            distance=abs(population[i][k]-population[j][k])
                            sign=population[i][k]-population[j][k]
                            if sign < 0:
                                sign=-1
                            elif sign>0:
                                sign=1
                            
                            population[j][k]=population[j][k]*((1/(1+distance)) + alpha*np.random.normal())
                
                elif i==j:

                    aux = deepcopy(population[j])
                    for k in range(len(population[j])):
                        aux[k]=population[j][k]+ alpha*np.random.normal()
                    
                    if func(aux) < func(population[j]):
                        population[j]=deepcopy(aux)



        if temporaryPoints != None:
            for x in temporaryPoints:
                x.remove()
        #temporaryPoints, = plt.plot(pop[0][0],pop[0][1],marker='o',color='k')
       
        for i in range(len(population)):
            population[i].append(func(population[i]))
        temporaryPoints = [plt.plot(*p, marker='o', color='k')[0] for p in population]
        plt.draw()
        plt.pause(1/5)
        for i in range(len(population)):
            population[i].pop(-1)

        t+=1

        
    print("Search Finished")


def main():
    functionsList = [[sphereFunction,-6], [ackleyFunction,-40], [rastriginFunction,-5], [rosenbrockFunction,-10], [griewankFunction,-10], [schwefelFunction,-500], [levyFunction,-10], [michalewiczFunction,-4], [zakharovFunction,-10]]

    for x in functionsList:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        #fig, ax = plt.subplots()

        showGraph(x[0], x[1], ax)
        fireflyAlgorithm(x[0], x[1], ax)
        plt.show()

if __name__ == "__main__":
    main()


