import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


import networkx as nx
import random
from draw import graph_drawer as drw
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

def DFS_visit(G : nx.DiGraph, v : int, d : list, t : list, stack : list):
    t[0] += 1
    d[v] = t[0]
    for neighbour in G.neighbors(v):
        if d[neighbour] == -1:
            DFS_visit(G, neighbour, d, t, stack)
    t[0] += 1
    stack.append(v)

def components_r(G : nx.DiGraph, nr : int, v : int, comp : list):
    for neighbour in G.neighbors(v):
        if comp[neighbour] == -1:
            comp[neighbour] = nr
            components_r(G, nr, neighbour, comp)

def Kosaraju(G : nx.DiGraph):
    d = {v: -1 for v in G.nodes}
    comp = {v: -1 for v in G.nodes}
    stack = []
    t = [0]
    nr = 0

    for node in G.nodes:
        if d[node] == -1:
            DFS_visit(G, node, d, t, stack)
    
    G_transposed = TransposeDigraph(G)

    while stack:
        node = stack.pop()
        if comp[node] == -1:
            nr += 1
            comp[node] = nr
            components_r(G_transposed, nr, node, comp)

    return comp
#--------------------------------------------------------------#


#------------------------- ZAD 3 --------------------------------#
def GenerateWeightMatrix(G: nx.DiGraph):
    matrix = {u: {v: float('inf') for v in G.nodes} for u in G.nodes}
    for node, neighbour in G.edges:
        matrix[node][neighbour] = random.randint(-5,10)

    return matrix


def BellmanFord(G : nx.DiGraph, w, s : int, ret_ds_ps = False, draw = False, add_edges = True):
    G_clone = G.copy()  
    if draw:
        drw.DrawGraphWithWeights(G_clone, name="Bellman-Ford")
    for node, neighbour in G_clone.edges:
        weigth = w[node][neighbour]
        G_clone.add_weighted_edges_from([(node, neighbour, weigth)])

    ds, ps = lab3.InitPaths(G_clone, s)

    for _ in range(0, len(G_clone.nodes)-1):
        for node, neighbour, weigth in G_clone.edges(data='weight'):
            if ds[neighbour] > ds[node] + weigth:
                ds[neighbour] = ds[node] + weigth
                ps[neighbour] = node
     
    if draw:
        print("Bellman-Ford: ", ps)
        drw.DrawGraphWithWeights(G_clone, name="Bellman-Ford")

    for node, neighbour, weigth in G_clone.edges(data='weight'):
        if ds[neighbour] > ds[node] + weigth:
            if ret_ds_ps:
                return False, ds, ps
            else:
                return False
    if ret_ds_ps:
        return True, ds, ps
    else:
        return True

def PrintDistanceMatrix(G : nx.DiGraph, w):
    matrix = {u: {v: float('inf') for v in G.nodes} for u in G.nodes}
    for u in G.nodes:
        x, ds, ps = BellmanFord(G, w, u, ret_ds_ps=True)
        for v in G.nodes:
            print(f"{ds[v]:>4}", end=' ')
        print()

#--------------------------------------------------------------#


#------------------------- ZAD 4 --------------------------------#
def Dijkstra(G : nx.DiGraph, s : int, w) :
    d, p = lab3.InitPaths(G, s)
    nodes = [s]
    visited = set()

    while nodes:
        u = nodes.pop(nodes.index(min(nodes, key=lambda n: d[n])))
        visited.add(u)

        for v in G.neighbors(u):
            if v in visited:
                continue
            
            notInNodes = v not in nodes
            newWeight = d[u] + w[u][v]
            if d[v] > newWeight or notInNodes:
                d[v] = newWeight
                p[v] = u
                if notInNodes:
                    nodes.append(v)
    return d, p


def Johnson(G : nx.DiGraph, w):
    G_new = G.copy()
    s = max(G_new.nodes)+1
    G_new.add_node(s)

    matrix = {u: {v: float('inf') for v in G_new.nodes} for u in G_new.nodes}
    for node, neighbour in G_new.edges:
        matrix[node][neighbour] = w[node][neighbour]
        G_new.add_weighted_edges_from([(node, neighbour, matrix[node][neighbour])])

    for node in G_new.nodes:
        if node != s:
            matrix[node][s] = 0
            G_new.add_weighted_edges_from([(s, node, matrix[node][s])])

    BellmanFordValue, ds, ps = BellmanFord(G_new, matrix, s, ret_ds_ps=True, add_edges=False)

    if BellmanFordValue == False:
        return None

    h = ds
    print(h)

    w_new = [[None]*len(G.nodes) for _ in range(len(G.nodes))]

    for node in G.nodes:
        for neighbour in G.neighbors(node):
            w_new[node][neighbour] = w[node][neighbour] + h[node] - h[neighbour]
    
    D = [[None]*len(G.nodes) for _ in range(len(G.nodes))]

    for node in G.nodes:
        du, _ = Dijkstra(G, node, w_new)
        for node2 in G.nodes:
            D[node][node2] = du[node2] - h[node] + h[node2]
    
    # for i in D:
    #     for j in i:
    #         print(j, end=' ')
    #     print(' ')
    
    return D
#--------------------------------------------------------------#