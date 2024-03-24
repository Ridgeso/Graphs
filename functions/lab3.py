from math import inf
import networkx as nx
from random import randint

def randomWeights(G : nx.Graph):
    for u in G.nodes:
        for v in G.neighbors(u):
            G.add_weighted_edges_from([(u, v, randint(1, 10))])


def initPaths(G : nx.Graph, s : int) :
    d = {node : inf for node in G.nodes}
    d[s] = 0
    p = {node : None for node in G.nodes}
    return d, p


def Dijkstra(G : nx.Graph, s : int) :
    d, p = initPaths(G, s)
    nodes = [s]
    visited = set()

    while nodes:
        u = nodes.pop(nodes.index(min(nodes, key=lambda n: d[n])))
        visited.add(u)

        for v in G.neighbors(u):
            if v in visited:
                continue
            
            notInNodes = v not in nodes

            newWeight = d[u] + G[u][v]['weight']
            if d[v] > newWeight or notInNodes:
                d[v] = newWeight
                p[v] = u
                if notInNodes:
                    nodes.append(v)
            
    return d, p


def showAllPaths(weights : dict, parents : dict) :
    root = None
    for p in parents:
        if parents[p] is None:
            root = p
            break
    if root is None:
        print("Nie ma wierzchołka początkowego!")
        return
    
    print(f"START: s = {root}")
    for p in parents:
        nodesOrder = [p]
        weight = weights[p]
        n = parents[p]
        while n is not None:
            weight += weights[n]
            nodesOrder.append(n)
            n = parents[n]
        
        path = f"d({p + 7}) = {weight:<4} ==> [{' - '.join(map(str, reversed(nodesOrder)))}]"
        print(path)


def GraphCenter(G : nx.Graph) :
    center_distances = {}
    center_minimax_distances = {}
    
    for node in G.nodes:
        distances, _  = Dijkstra(G, node)
        center_distances[node] = sum(distances.values())
        max_distance = max(distances.values())
        center_minimax_distances[node] = max_distance
    
    center_node = min(center_distances, key=center_distances.get)
    center_minimax_node = min(center_minimax_distances, key=center_minimax_distances.get)
    print("Center: "  + str(center_node)  + " center minmax: " + str(center_minimax_node))