import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


import networkx as nx
import random
from draw import graph_drawer as drw
from collections import Counter #do zliczania najczesciej wystepujacego elementu
import math
import lab3


#------------------------- ZAD 1 -------------------------------------#
def DigraphRandomGenerate(n : int, p : float):
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j)
    #Łuk do samego siebie
    # for i in range(n):
    #     if random.random() < p:
    #             G.add_edge(i, i)
    return G

def NeighborhoodListFromDigraph(G : nx.DiGraph):
     i = 0
     for node in G.nodes:
        print(i, end=". ")
        for neighbour in G.neighbors(node):
            print(neighbour, end=" ")
        print("")
        i += 1

def NeighborhoodMatrixFromDigraph(G : nx.DiGraph):
    nodes_count = len(G.nodes)
    matrix = [[0 for _ in range(nodes_count)] for _ in range(nodes_count)]
    for node in range(nodes_count):
        neighbours = G.neighbors(node)
        for neighbour in neighbours:
            matrix[node][neighbour] = 1

    for i in range(nodes_count):
        for j in range(nodes_count):
            print(matrix[i][j], end=" ")
        print("")

def format_number(number):
    if number < 0:
        return "{:d}".format(number) 
    else:
        return " {:d}".format(number)

def IncidencesMatrixFromDigraph(G : nx.DiGraph):
    nodes_count = len(G.nodes)
    edges_count = len(G.edges)
    index = 0
    matrix = [[0 for _ in range(edges_count)] for _ in range(nodes_count)]
    for node in range(nodes_count):
        neighbours = G.neighbors(node)
        for neighbour in neighbours:
            matrix[node][index] = -1
            matrix[neighbour][index] = 1
            index += 1
    
    for i in range(nodes_count):
        for j in range(edges_count):
            print(format_number(matrix[i][j]), end=" ")
        print("")
#--------------------------------------------------------------#


#------------------------- ZAD 2 -------------------------------------#
def TransposeDigraph(G : nx.DiGraph):
    G_temp = nx.DiGraph()
    for node in G.nodes:
        G_temp.add_node(node)
    for node in G.nodes:
        for neighbour in G.neighbors(node):
            G_temp.add_edge(neighbour, node)
    return G_temp

def DFS_visit(G : nx.DiGraph, v : int, d : list, f : list, t : list):
    t[0] += 1
    d[v] = t[0]
    for neighbour in G.neighbors(v):
        if d[neighbour] == -1:
            DFS_visit(G, neighbour, d, f, t)
    t[0] += 1
    f[v] = t[0]

def components_r(G : nx.DiGraph, nr : int, v : int, comp : list):
    for neighbour in G.neighbors(v):
        if comp[neighbour] == -1:
            comp[neighbour] = nr
            components_r(G, nr, neighbour, comp)

def Kosaraju(G : nx.DiGraph):
    d = [-1 for _ in range(len(G.nodes))]
    f = [-1 for _ in range(len(G.nodes))]
    comp = [-1 for _ in range(len(G.nodes))]
    vertices = list(G.nodes)
    t = [0]
    nr = 0

    for node in G.nodes:
        if d[node] == -1:
            DFS_visit(G, node, d, f, t)
    
    G_transposed = TransposeDigraph(G)

    f, vertices = zip(*sorted(zip(f, vertices)))
    vertices = vertices[::-1]

    for node in vertices:
        if comp[node] == -1:
            nr += 1
            comp[node] = nr
            components_r(G_transposed, nr, node, comp)
    
    vertices = vertices[::-1]

    return comp
#--------------------------------------------------------------#


#------------------------- ZAD 3 --------------------------------#
def GenerateWeightMatrix(G: nx.DiGraph):
    matrix = [[None]*len(G.nodes) for _ in range(len(G.nodes))]
    for node in range(len(G.nodes)):
        for neighbour in G.neighbors(node):
            matrix[node][neighbour] = random.randint(-5,10)
    return matrix

ds = []
ps = []

def BellmanFord(G : nx.DiGraph, w, s : int):
    list_of_SCC = Kosaraju(G)
    counter = Counter(list_of_SCC)
    most_common_factor = counter.most_common(1)[0][0]
    indexes_to_delete = [i for i, element in enumerate(list_of_SCC) if element != most_common_factor]
    G_clone = G.copy()

    for node in G.nodes:
        if node in indexes_to_delete:
            G_clone.remove_node(node)
        else:
            for neighbour in list(G.neighbors(node)):
                weight = w[node][neighbour]
                G_clone.add_weighted_edges_from([(node, neighbour, weight)])


    ds = [math.inf for _ in range(len(G.nodes))]
    ps = [None for _ in range(len(G.nodes))]
    ds[0] = 0

    for _ in range(0, len(G_clone.nodes)-1):
        for node in G_clone.nodes:
            for neighbour in G_clone.neighbors(node):
                if ds[node] > ds[neighbour] + w[node][neighbour]:
                    ds[node] = ds[neighbour] + w[node][neighbour]
                    ps[node] = neighbour

    for node in G_clone.nodes:
            for neighbour in G_clone.neighbors(node):
                if ds[node] > ds[neighbour] + w[node][neighbour]:
                    return False
    return True
#--------------------------------------------------------------#


#------------------------- ZAD 4 --------------------------------#
def Johnson(G : nx.DiGraph, w):
    G_new = G.copy()
    
    new_w = [[None]*(len(G_new.nodes)+1) for _ in range(len(G_new.nodes)+1)]
    for node in G.nodes:
        for neighbour in G.neighbors(node):
            new_w[node][neighbour] = w[node][neighbour]
    
    w = new_w

    s = max(list(G_new.nodes)) + 1
    G_new.add_node(s)
    for node in G_new.nodes:
        if node != s:
            w[s][node] = 0
            G_new.add_weighted_edges_from([(s, node, w[s][node])])

    if BellmanFord(G_new, new_w, s) == False:
        return None
    
    h = [ds[i] for i in range(len(G_new.nodes))]
    
    w_new = [[None]*len(G_new.nodes) for _ in range(len(G_new.nodes))]

    for node in G_new.nodes:
        for neighbour in G_new.neighbors(node):
            w_new[node][neighbour] = w[node][neighbour] + h[node] - h[neighbour]
    
    D = [[None]*len(G_new.nodes) for _ in range(len(G_new.nodes))]

    for node in G_new.nodes:
        du, _ = lab3.Dijkstra(G_new, node)
        for node2 in G_new.nodes:
            D[node][node2] = du[node2] - h[node] + h[node2]
    
    return D
#--------------------------------------------------------------#