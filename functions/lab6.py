import numpy as np
import networkx as nx

def pagerank_random_walk(graph, d=0.15, num_iterations=1000):
    n = len(graph)
    P = np.zeros((n, n))
    for node in graph.nodes():
        out_degree = graph.degree(node)
        if out_degree == 0:  
            continue
        for neighbor in graph.neighbors(node):
            P[neighbor][node] = (1 - d) / out_degree

    pagerank = np.ones(n) / n
    teleportation_prob = np.ones(n) * d / n

    for _ in range(num_iterations):
        pagerank = np.dot(P, pagerank) + teleportation_prob

    return pagerank




def pagerank_iteration(graph, d=0.15, num_iterations=1000):
    n = len(graph)
    A = np.zeros((n, n))
    for node in graph.nodes():
        degree_sum = sum(graph.degree(neighbor) for neighbor in graph.neighbors(node))
        for neighbor in graph.neighbors(node):
            A[neighbor][node] = (1 - d) * graph.degree(neighbor) / degree_sum + d / n

    pagerank = np.ones(n) / n

    for _ in range(num_iterations):
        pagerank = np.dot(A, pagerank)

    return pagerank



