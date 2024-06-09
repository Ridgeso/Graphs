from collections import deque
import random
import networkx as nx

def can_edge_be_added(u, v, G):
    if u == 't':
        return False
    if v == 's':
        return False
    if G.has_edge(u, v):
        return False
    if G.has_edge(v, u):
        return False
    if u == v:
        return False
    return True

def generate_flow_network(n: int):
    if n < 2:
        raise ValueError('Liczba warstw powinna być przynajmniej 2')

    G = nx.DiGraph()
    
    G.add_node('s')
    G.add_node('t')

    prev_layer = ['s']

    for i in range(n):
        current_layer_size = random.randint(2, n)
        current_layer = [f'{i+1}_{j+1}' for j in range(current_layer_size)]
        
        for node in current_layer:
            G.add_node(node)

        for u in prev_layer:
            for v in current_layer:
                if can_edge_be_added(u, v, G):
                    capacity = random.randint(1, 10)
                    G.add_edge(u, v, capacity=capacity, flow=0)

        prev_layer = current_layer

    for u in prev_layer:
        if can_edge_be_added(u, 't', G):
            capacity = random.randint(1, 10)
            G.add_edge(u, 't', capacity=capacity, flow=0)
    
    all_nodes = list(G.nodes())
    
    max_iter = 1000
    for _ in range(2 * n):
        i = 0
        while i < max_iter:
            u = random.choice(all_nodes)
            v = random.choice(all_nodes)
            if can_edge_be_added(u, v, G):
                capacity = random.randint(1, 10)
                G.add_edge(u, v, capacity=capacity, flow=0)
                break
            i += 1
        if i == max_iter:
            raise Exception('Nie udało się wylosować dodatkowych 2n krawędzi')

    return G

def bfs(G, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in G[u]:
            if v not in visited and G[u][v]['capacity'] - G[u][v]['flow'] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(G, source, sink):
    parent = {}
    max_flow = 0
    
    while bfs(G, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, G[parent[s]][s]['capacity'] - G[parent[s]][s]['flow'])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            G[u][v]['flow'] += path_flow
            if G.has_edge(v, u):
                G[v][u]['flow'] -= path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow
