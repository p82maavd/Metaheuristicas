


    

from copy import copy, deepcopy
from operator import index
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

from functions import *

def scaleMatrix(matrix):

    biggest=0
    smallest=math.inf
    new_matrix=deepcopy(matrix)

    for x in matrix:
        for y in x:
            if y <smallest:
                smallest=y
            elif y > biggest:
                biggest=y
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j]=((new_matrix[i][j]-smallest)*2)/(biggest-smallest)
    
    return new_matrix

def showGraph(cities, solution=None, gen = 0,pheromoneMatrix=None):
    plt.clf()
    plt.title(str(gen)+"/200")
    for x in cities:
        plt.plot(x[0],x[1],marker='o',color='k')
    
    if solution!=None:
        for i in range(-1,len(solution)-1):
            listax=[cities[solution[i]][0],cities[solution[i+1]][0]]
            listay=[cities[solution[i]][1],cities[solution[i+1]][1]]
            plt.plot(listax, listay, color='black')

    '''
    if pheromoneMatrix!=None:
        
        scaledPheromoneMatrix=scaleMatrix(pheromoneMatrix)

        for i in range(len(scaledPheromoneMatrix)):
            
            for k in range(len(scaledPheromoneMatrix)):
                if i!=k:
                    listax=[cities[i][0],cities[k][0]]
                    listay=[cities[i][1],cities[k][1]] 
                    plt.plot(listax, listay, color='purple',linewidth=scaledPheromoneMatrix[i][k])

    '''
        

def evaluateSolution(solution,visibilityMatrix):
    fitness=0
    #Checkear si estos rangos estan bien por el menos 1
    for i in range(-1,len(solution)-1):
        fitness+= 1/visibilityMatrix[solution[i]][solution[i+1]]
    return fitness
    

def initialPopulation(np, cities):
    population=[]
    if np == len(cities):
        for i in range(len(cities)):
            population.append([i])
    else:
        print("Number of cities should be equal to number of ants")
    return population

def calculateVisibilityMatrix(cities):
    
    matrix=[]
    
    for i,x in enumerate(cities):
        matrix.append([])
        for y in cities:
            if x ==y:
                matrix[i].append(0)
            else:
                matrix[i].append(1/(math.sqrt(pow(y[0]-x[0],2)+pow(y[1]-x[1],2))))

    return matrix

def initialPheromoneMatrix(cities):
    
    matrix=[]
    
    for i,x in enumerate(cities):
        matrix.append([])
        for y in cities:
            matrix[i].append(1)
           

    return matrix




def antColonyOptimization(np, maxGen, d, cities):

    alpha=1
    beta=2
    evaporationCoefficient=0.5
    gen=0
    

    population = initialPopulation(np, cities)
    best=None
    visibilityMatrix = calculateVisibilityMatrix(cities)
    
    pheromoneMatrix = initialPheromoneMatrix(cities)

    while gen<maxGen:

        population = initialPopulation(np, cities)
        
        for ant in range(len(population)):

            while(len(population[ant])!=len(cities)):

                posibilities=[]
                suma=0
                for city in range(len(cities)):
                    if city not in population[ant]:
                        posibilities.append([city,pow(pheromoneMatrix[population[ant][-1]][city],alpha)*pow(visibilityMatrix[population[ant][-1]][city],beta)])
                        suma+=posibilities[-1][1]
                
                cont=0
                for x in posibilities:
                    x[1]=x[1]/suma+cont
                    cont=x[1]
                
                r=random.uniform(0,1)
            
                for x in posibilities:
                    if x[1]>r:
                        population[ant].append(x[0])
                        
                        break

        for x in range(len(pheromoneMatrix)):
            for y in range(len(pheromoneMatrix[0])):
                pheromoneMatrix[x][y]*=(1-evaporationCoefficient)
                
        
        for ant in population:
            evaluation=evaluateSolution(ant,visibilityMatrix)
            for i in range(-1,len(ant)-1):
                pheromoneMatrix[ant[i]][ant[i+1]]+= evaluation

        gen+=1
        
        population.sort(key=lambda w: [evaluateSolution(w,visibilityMatrix)],reverse=False)

        if best==None:
            best=deepcopy(population[0])
        else:
            if evaluateSolution(population[0],visibilityMatrix) < evaluateSolution(best,visibilityMatrix):
                
                best=deepcopy(population[0])


        showGraph(cities,best,gen,pheromoneMatrix)
        plt.draw()
        plt.pause(0.001)
    
    showGraph(cities,best,gen)

    #population.sort(key=lambda w: [evaluateSolution(w)],reverse=False)
    
    #showGraph(cities,population[0])
    


def main():

    fig, ax = plt.subplots()

    #number of population individuals
    np=20

    #generations
    g=200

    #number of cities
    d=20

    cities = set()

    while(len(cities)!=d):
        cities.add((random.randrange(0,100),random.randrange(0,100)))
    #print(cities)
    cities=list(cities)
    showGraph(cities)
    antColonyOptimization(np, g, d, cities)
    plt.show()

if __name__ == "__main__":
    main()


