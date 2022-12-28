


    

from copy import copy
from operator import index
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

from functions import *

def showGraph(cities, solution=None, gen = 0):

    plt.clf()
    plt.title(str(gen)+"/500")
    for x in cities:
        plt.plot(x[0],x[1],marker='o',color='k')
    
    if solution!=None:
        for i in range(-1,len(solution)-1):
            listax=[solution[i][0],solution[i+1][0]]
            listay=[solution[i][1],solution[i+1][1]]
            plt.plot(listax, listay, color='black')


def evaluateSolution(solution):
    fitness=0
    #Checkear si estos rangos estan bien por el menos 1
    for i in range(-1,len(solution)-1):
        fitness+= math.sqrt(pow(solution[i+1][0]-solution[i][0],2)+pow(solution[i+1][1]-solution[i][1],2))
    return fitness
    

def randomPopulation(np, cities):
    newpopulation=[]
    for x in range(0, np):
        copycities=copy(cities)
        newsolution = []
        while(len(copycities)!=0):
            if len(copycities) == 1:
                newsolution.append(copycities[0])
                copycities.pop(0)
            else:
                index=random.randrange(0,len(copycities)-1)
                newsolution.append(copycities[index])
                copycities.pop(index)
        newpopulation.append(newsolution)

    return newpopulation

def crossover(parent_A, parent_B):

    first=parent_A[0:random.randrange(0,len(parent_A)-1)]
    copyparent_B=copy(parent_B)
    for x in parent_B:
        if x in first:
            copyparent_B.remove(x)
    
    return first+copyparent_B

def mutate(offspring_AB):
    
    index1 = random.randrange(0,len(offspring_AB)-1)
    while True:
        index2 = random.randrange(0,len(offspring_AB)-1)
        if index1!=index2:
            break
    offspring_AB[index1], offspring_AB[index2] = offspring_AB[index2], offspring_AB[index1]

    return offspring_AB

def geneticAlgorithm(np, gen, d, cities):

    population = randomPopulation(np, list(cities))
    print(evaluateSolution(population[0]),evaluateSolution(population[1]))

    for i in range(gen):
        new_population = copy(population)
        for j in range(0,np):
            
            parent_A = population[j]
            
            #To get a different parent
            while True:
                index=random.randrange(0,len(population)-1)
                if index!=j:
                    break
            
            parent_B = population[index]

            offspring_AB = crossover(copy(parent_A),copy(parent_B))

            if random.uniform(0,1) < 0.5:
                
                offspring_AB = mutate(offspring_AB)

            if evaluateSolution(offspring_AB) < evaluateSolution(parent_A):
                new_population[j] = offspring_AB

        population=copy(new_population)
        new_population.sort(key=lambda w: [evaluateSolution(w)],reverse=False)

        showGraph(cities,new_population[0],i)
        plt.draw()
        plt.pause(0.001)


    population.sort(key=lambda w: [evaluateSolution(w)],reverse=False)
    
    showGraph(cities,population[0])
    


def main():

    fig, ax = plt.subplots()

    #number of population individuals
    np=20

    #generations
    g=500

    #number of cities
    d=20

    cities = set()

    while(len(cities)!=d):
        cities.add((random.randrange(0,100),random.randrange(0,100)))
    #print(cities)

    showGraph(cities)
    geneticAlgorithm(np, g, d, cities)
    plt.show()

if __name__ == "__main__":
    main()


