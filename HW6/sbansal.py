# Program for Homework 07
# DSA SP20
# Author: Sparsh Bansal

import pytest
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def ComponentCounter(Graph):
    '''
    A function that finds the number of components in an undirected graph
    G = (V;E)

    '''

    #  Initializing a variable to keep track of the component count
    counter = 0

    # Initializing a hashmap to mark nodes as visited or unvisited
    # By default, I mark all nodes in the given graph as unvisited
    # I have used the .nodes() function from the networkx library
    visited = {}
    for node in Graph.nodes():
        visited[node] = 'Unvisited'
        # print(visited)

    # Iterate through all nodes in the given graph
    for node in visited:

        # This if statement checks the initial node of every component
        if visited[node] == 'Unvisited':
            
            # At the beginning of each component, one is added to the 
            # counter
            counter += 1
            
            # Intializing a stack to hold the neighbors of the
            # current node - in turn to call DFS on them
            check_neighbors = []
            
            # Appending the initial node (source node)
            check_neighbors.append(node)

            # This while loop runs until there are unvisited neighbors
            # of the source node
            while len(check_neighbors) > 0:
                
                # Popping one element from the stack
                temp_node = check_neighbors.pop()

                # Appending all unvisited neighbors of the current node
                # to check_neighbors while marking them visited
                for neighbor in Graph.neighbors(temp_node):
                    if visited[neighbor] == 'Unvisited':
                        check_neighbors.append(neighbor)
                    visited[neighbor] = 'Visited'

    return counter

def TF1():
    '''
    Test function for tesing edge/special cases in counting trees
    Library used: pyTest

    '''

    # Test case 1 - Single Component
    G = nx.Graph()
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_edge(0,1)
    G.add_edge(1,2)
    assert ComponentCounter(G) == 1

    # Test case 2 - Multiple nodes linked to the first node
    G.add_node(3)
    G.add_node(4)
    G.add_edge(0,3)
    assert ComponentCounter(G) == 2    

    # Test case 3 - A cyclcal component with a non-cyclical component
    G.add_edge(2,3)
    assert ComponentCounter(G) == 2

    # Test case 4 - Isolated Components
    H = nx.Graph()
    H.add_node(0)
    H.add_node(1)
    H.add_node(2)
    H.add_node(3)
    H.add_node(4)
    H.add_node(5)
    H.add_node(6)
    assert ComponentCounter(H) == 7
    
def graph_maker(n,p):
    '''
    This function builds a random binomial graph

    Text from the assignment: A random binomial graph G(n; p) is a graph on 
    n nodes such that for every pair of nodes (i; j) there exists an edge
    between i and j with probability p.
    
    '''
    G = nx.Graph()

    for node in range(n):
        G.add_node(node)

    for i in range(n):
        for j in range(n):
            if np.random.uniform() <= p:
                G.add_edge(i, j)
    
    return G

def plotter(num_graphs, a, b):
    '''
    This function finds the smallest probability p (that is a multiple of 0.01) 
    such that ten generated binomial random graphs G(n; p) each consists of a 
    single component. It also plots this probability as a function of n. Here,
    n is the number of components in the graph and p is the probability that 
    there exists an edge between i and j.

    '''
    
    # Stores data for the plot
    tested_probabilities = []


    for x in range(a,b):
        # Creates a set of probabilities
        for p_test in range(0,100,1):
            pt = p_test / 100
            Count = 0
            if len(tested_probabilities) == x-4:
                break
            for _ in range(num_graphs):
                G = graph_maker(x, pt)
                if ComponentCounter(G) == 1:
                    Count += 1
                    if Count == 10:
                        # Stores the smallest probability
                        tested_probabilities.append(pt)
                        break
                else:
                    break
    
    # Plots the results
    plt.plot(range(5,51), tested_probabilities, 'o')
    plt.xlabel("n")
    plt.ylabel("Probability for a Graph to be connected")
    plt.title("Plot showing Minimum Probability for Graph Connectivity")
    plt.show()

if __name__ == "__main__":
    # G = nx.Graph()
    # G.add_node(0)
    # G.add_node(1)
    # G.add_node(2)
    # G.add_node(3)
    # G.add_node(4)
    # G.add_node(5)

    # # 1st component
    # G.add_edge(0,1)
    # G.add_edge(1,2)

    # # 2nd component
    # G.add_edge(3,4)
    # G.add_edge(4,5)

    # ComponentCounter(G)

    # Test Function
    TF1()

    # Plotter Function
    plotter(10,5,51)