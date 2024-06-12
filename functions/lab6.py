from random import randint, random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


###### ZADANIE 1


def toChr(nr):
    return chr(nr + 65)


def parsGraph(graph: nx.Graph):
    graphList = {toChr(node) : [] for node in graph.nodes}
    for u, v in graph.edges:
        graphList[toChr(u)].append(toChr(v))
    return graphList


def logParsedPraph(graph: dict):
    for v in graph:
        print(f"{v}: {' '.join(graph[v])}")


def randomWalk(graph: nx.Graph, d=0.15, numIterations=100):
    countList = np.zeros(numIterations)
    graphList = parsGraph(graph)
    vertexList = list(graphList.keys())
    currentVertex = np.random.choice(vertexList)

    for _ in range(numIterations):
        countList[vertexList.index(currentVertex)] += 1
        currentVertex = np.random.choice(
            vertexList if np.random.random() <= d else graphList[currentVertex])
    countList /= numIterations

    rankedList = list(zip(vertexList, countList))
    return rankedList


def logRandomWalk(pagerank_random):
    for edge, prop in pagerank_random:
        print(f"{edge} ==> PageRank = {prop}")


def vectorIteration(graph: nx.Graph, d=0.15, eps=0.000001):
    graph = parsGraph(graph)

    n = len(graph)
    P, A = np.zeros((n, n)), np.zeros((n, n))
    
    for i, vertex in enumerate(graph):
        for j, neighbour in enumerate(graph):
            if neighbour in graph[vertex]:
                A[i][j] = 1
    
    P = (1 - d) * (A.transpose() / np.sum(A, axis=1)).transpose() + d / n

    p = np.ones(n) / n
    pNext = np.dot(p, P)
    iter = 0
    while np.max(np.abs(pNext - p)) > eps:
        p = pNext
        pNext = np.dot(p, P)
        iter += 1

    rankedList = list(zip(graph.keys(), pNext))
    print(f"Ilosc iteracji: {iter}")
    return rankedList
    
    
def logVectorIter(pageRank):
    logRandomWalk(pageRank)
    weights = map(lambda v: v[1], pageRank)
    print(f"Suma wag: {sum(weights)}")


###### ZADANIE 2


def calculateCycleLength(points):
    newPoints = points[ : -1] - points[1 : ]
    norm = np.sum(np.linalg.norm(newPoints, axis=1))
    lastNorm = np.linalg.norm(points[-1] - points[0])
    return norm + lastNorm


def twoOptSwap(points, a, b):
    a += 1
    b -= 1

    while (a < b):
        points[a], points[b] = points[b].copy(), points[a].copy()
        a += 1
        b -= 1
    

def simulatedAnnealing(points, maxIter=10000):
    pointsSize = len(points)
    if pointsSize <= 1:
        print("Nie otrzymano punktów")
        return

    currCycle = np.copy(points)
    currCycleLen = calculateCycleLength(currCycle);

    bestCycle = np.copy(points)
    bestCycleLen = currCycleLen;

    print(f"Początkowa długość cyklu: {bestCycleLen}")

    for i in range(100, 0, -1):
        print(f"Iteracja: {i}")
        T = 0.001 * pow(i, 2)
        for it in range(maxIter):
            a = randint(0, pointsSize - 1)
            b = randint(0, pointsSize - 1)

            newCycle = currCycle.copy()
            twoOptSwap(newCycle, a, b)
            newCycleLen = calculateCycleLength(newCycle)

            if (newCycleLen < currCycleLen):
                currCycle = newCycle.copy()
                currCycleLen = newCycleLen
                if (newCycleLen < bestCycleLen):
                    bestCycle = newCycle.copy()
                    bestCycleLen = newCycleLen
            elif random() < np.exp((currCycleLen - newCycleLen) / T):
                currCycle = newCycle
                currCycleLen = newCycleLen

    print("Najlepsza długość cyklu: %f\n", bestCycleLen);
    with open("bestCycle.dat", "w") as cf:
        for point in bestCycle:
            cf.write(f"{point[0]} {point[1]}\n")

    plt.scatter(bestCycle[:, 0], bestCycle[:, 1])
    bestCycle = np.vstack((bestCycle[ : -1], bestCycle[1 : ])).T
    plt.plot(bestCycle[0], bestCycle[1], '-r')
    plt.show()
