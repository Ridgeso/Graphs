import networkx as nx
import random

def Erodos_Renyia_Edges(n,l):
    G = nx.Graph()
    matrix = [[-1 for x in range(n)] for y in range(n)]
    if(l > n*(n-1)/2):
        print("The number of edges exceeds the maximum value for this amount of vertexes whis is " + n*(n-1)/2)
        return None
    else:
        for i in range(n):
            G.add_node(i)
        for i in range(l):
            rand1, rand2 = random.sample(range(0,n), 2)
            while matrix[rand1][rand2] != -1:
                rand1, rand2 = random.sample(range(0,n), 2)
            matrix[rand1][rand2] = matrix[rand2][rand1] = i
            G.add_edge(int(rand1), int(rand2))
        return G

def Erodos_Renyia_Probability(n,l):
    G = nx.Graph()
    matrix = [[-1 for x in range(n)] for y in range(n)]
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i>j and random.random() < l:
                G.add_edge(int(i), int(j))
    return G



