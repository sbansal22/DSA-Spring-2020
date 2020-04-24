# Program for Homework 10
# DSA SP20
# Author: Sparsh Bansal
# Reference: read_tsp function by Teaching Team

import numpy as np
import time
import timeit

def read_tsp(filename):
    ''' Reads a TSPLIB instance given by filename and returns the corresponding
    distance matrix C. Assumes that the edge weights are given in lower diagonal row
    form. '''

    f = open(filename,'r')

    n, C = 0, None
    i, j = -1, 0

    for line in f:
        words = line.split()
        if words[0] == 'DIMENSION:':
            n = int(words[1])
            C = np.zeros(shape=(n,n))
        elif words[0] == 'EDGE_WEIGHT_SECTION':
            i = 0 # Start indexing of edges
        elif i >= 0:
            for k in range(len(words)):
                if words[k] == 'EOF':
                    break
                elif words[k] == '0':
                    i += 1 # Continue to next row of the matrix
                    j = 0
                else:
                    C[i,j] = int(words[k])
                    C[j,i] = int(words[k])
                    j += 1

    return C


    # -------------------------------------------------------------------------


def greedheur(C, firstcity=0):
    '''
    A greedy heuristic algorithm for the traveling salesman problem

    Input - A TSP instance from the TSPLIB1, starting city
            By default, the first city would be the city
            represented by the first index in the instance
    Output - A tour path and total distance for the given or 
             default starting city

    '''

    # Initializing a list to store the tour city sequence
    path = [firstcity]

    # Initializing a variable to store the covered distance
    # in the given units
    dist = 0

    # Storing the number of cities
    num_cities = len(C[0])
    # A dictionary to store the cities that the salesman has
    # visited according to the plan, or in other words, the
    # cities that are already planned on the tour
    visited = dict()

    # Marking that initially none of the cities are visited,
    # with an exception of the starting city
    for i in range(num_cities):
        visited[i] = False
    visited[path[-1]] = True

    # Initializing the counter to keep track of the iterator 
    # through each row of the instance array
    count = 0
    while count < num_cities - 1:
        
        # A variable to store the next city at the min distance
        curmin = 1000
        for city in range(num_cities):
            if not visited[city] and not C[path[-1]][city] == 0 and C[path[-1]][city] < curmin:
                curmin =  C[path[-1]][city]
                curcity = city
        
        # Updating the tour route
        path.append(curcity)
        # Updating the tour distance
        dist += curmin
        # Marking the current city as visited
        visited[curcity] = True
        # Incrementing the counter
        count += 1

    # The salesman want to come to the starting point
    dist += C[firstcity][path[-1]]
    path.append(firstcity)

    return path, dist


    # -------------------------------------------------------------------------


def localheur(C, firstcity=0):
    '''
    A local search heuristic algorithm for the traveling salesman problem.

    Input - An initial solution computer by greedheur() function
    Output - A potentially optimized tour path and total distance
             for the given or default starting city

    '''

    # Gets an initial solution using the greedy algorithm
    path_copy, path_dist = greedheur(C,firstcity)

    # Sets the currently known best path
    mindist = path_dist
    minpath = path_copy

    # Initializes a counter for the while loop processing
    count = 0
    while count < len(path)-3:
        copy = path_copy
        # Switches the city and the current index with the next city
        copy[count+1], copy[count+2] = path_copy[count+2], path_copy[count+1]
        # Calculates the new tour distance
        tempdist = distance(C, copy)

        # Compares the tour distance to the current minimum tour distance
        if tempdist < mindist:
            minpath = copy
            mindist = tempdist
            # If a more optimized solution is found, it is printed to the 
            # terminal
            print('Locally Optimized Solution: ')
            printer(minpath, mindist)

        # The switch is reverted to the initial state
        copy[count+1], copy[count+2] = path_copy[count+2], path_copy[count+1]

        # Counter is incremented
        count += 1
    
    return minpath, mindist


    # -------------------------------------------------------------------------


def distance(C, path):
    '''
    Finds the total distance travelled for a particular path

    '''

    dist = 0

    for i in range(len(path)-1):
        dist += C[path[i]][path[i+1]]

    return dist

def printer(path, dist):
    '''
    Prints the path and distance

    '''
    return print('Tour will be: ' + str(path) + ', and the distance will be: ' + str(dist))


    # -------------------------------------------------------------------------


if __name__ == "__main__":
    
    start_time = int(round(time.time() * 1000000))
    print('Processing gr17.tsp')
    C = read_tsp('gr17.tsp')
    path, dist = greedheur(C,3)
    print('Greedy Solution:')
    printer(path, dist)
    print(int(round(time.time() * 1000000))-start_time)
    start_time = int(round(time.time() * 1000000))
    localheur(C, 3)
    print(int(round(time.time() * 1000000))-start_time)

    print('Processing gr21.tsp')
    C = read_tsp('gr21.tsp')
    path, dist = greedheur(C,10)
    print('Greedy Solution:')
    printer(path, dist)
    localheur(C, 10)

    print('Processing gr24.tsp')
    C = read_tsp('gr24.tsp')
    path, dist = greedheur(C)
    print('Greedy Solution:')
    printer(path, dist)
    localheur(C)


    print('Processing gr24.tsp')
    C = read_tsp('gr48.tsp')
    path, dist = greedheur(C, 46)
    print('Greedy Solution:')
    printer(path, dist)
    localheur(C, 46)