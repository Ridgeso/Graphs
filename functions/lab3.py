from math import inf
import networkx as nx
from random import randint

def SetRandomWeights(G : nx.Graph, minWeight : int, maxWeight : int):
    for u in G.nodes:
        for v in G.neighbors(u):
            G.add_weighted_edges_from([(u, v, randint(minWeight, maxWeight))])

def PrintWeights(distances : map):
    print("Wagi grafu:")

    info = 'u\\v'
    firstLine = f"{info:<4}| "
    for v in distances:
        firstLine += f"{v:<4} "
    print(firstLine)
    print("-" * len(firstLine))
    
    for u in distances:
        print(f"{u:<4}| ", end = "")
        for v in distances:
            print(f"{distances[u][0][v]:<4}", end = " ")
        print()

def InitPaths(G : nx.Graph, s : int) :
    d = {node : inf for node in G.nodes}
    d[s] = 0
    p = {node : None for node in G.nodes}
    return d, p


def Dijkstra(G : nx.Graph, s : int) :
    d, p = InitPaths(G, s)
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


def ShowAllPaths(weights : dict, parents : dict) :
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
        
        path = f"d({p:>3}) = {weight:>4} ==> [{' -> '.join(map(str, reversed(nodesOrder)))}]"
        print(path)

def GetGrapPropagation(G : nx.Graph):
    nodeDistances = {}
    for n in G.nodes:
        nodeDistances[n] = Dijkstra(G, n)
    return nodeDistances

def GraphCenter(distances : map) :
    centerDistances = {node: sum(dis.values()) for node, (dis, _) in distances.items()}
    centerMinMax = {node: max(dis.values()) for node, (dis, _) in distances.items()}

    centerNode = min(centerDistances, key=centerDistances.get)
    centerMinMaxNode = min(centerMinMax, key=centerMinMax.get)
    print(f"""Center: {centerNode} (sum of distances: {centerDistances[centerNode]})\n"""
          f"""center minmax: {centerMinMaxNode} (max distance: {centerMinMax[centerMinMaxNode]})""")

def PrimeAlgorithm(G : nx.Graph):
    T = nx.Graph()
    W = nx.Graph()

    oldNode = next(iter(G))
    T.add_node(oldNode)
    for neigh in G.neighbors(oldNode):
        W.add_node(neigh)

    while W.nodes:
        u = None
        v = None
        closest = None
        for node in W.nodes:
            for tNode in G.neighbors(node):
                if not T.has_node(tNode):
                    continue
                if u is None or G[node][tNode]['weight'] < closest:
                    u = tNode
                    v = node
                    closest = G[node][tNode]['weight']

        T.add_edge(u, v, weight = closest)
        
        W.remove_node(v)
        for neigh in G.neighbors(v):
            if neigh in T.nodes:
                continue
            W.add_node(neigh)

    return T