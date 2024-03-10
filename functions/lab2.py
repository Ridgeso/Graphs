import networkx as nx
import random
from collections import defaultdict

def CheckZerosInSeq(A : list) :
	return not any(A)

def GraphicSeqCheck(A : list) :
	while True :
		A = sorted(A, reverse = True)
		if CheckZerosInSeq(A) :
			return True
		if A[0] >= len(A) or A[len(A) - 1] < 0 :
			return False
		for i in range(1, A[0] + 1) :
			A[i] -= 1
		A[0] = 0

def GraphFromGraphicSeq(A : list) :
	G = nx.Graph()
	if not GraphicSeqCheck(A) :
		return G
	for i in range(len(A)) :
		G.add_node(i)
	A = sorted(A, reverse = True)
	dictA = {i : A[i] for i in range(len(A))}
	while not CheckZerosInSeq(A) :
		A = sorted(A, reverse = True)
		dictA = dict(sorted(dictA.items(), key=lambda item: item[1], reverse = True))
		for i in range(1, A[0] + 1) :
			G.add_edge(list(dict.keys(dictA))[0], list(dict.keys(dictA))[i])
			A[i] -= 1
			dictA[list(dict.keys(dictA))[i]] -= 1
		A[0] = 0
		dictA[list(dict.keys(dictA))[0]] = 0
	return G

def RandomizeEdges(G : nx.Graph, numberOfRandomizes : int) :
	print(G.edges)
	def FindEdges(G) :
		edge1 = random.randrange(0, len(G.edges))
		edge2 = random.randrange(0, len(G.edges))
		while edge2 == edge1 :
			edge2 = random.randrange(0, len(G.edges))
		return list(G.edges)[edge1], list(G.edges)[edge2]
	
	for i in range(numberOfRandomizes) :
		newEdges = FindEdges(G)
		tol = 10
		while G.has_edge(newEdges[0][0], newEdges[1][1]) or G.has_edge(newEdges[0][1], newEdges[1][0]) or newEdges[0][1] == newEdges[1][0] or newEdges[0][0] == newEdges[1][1]:
			newEdges = FindEdges(G)
		G.add_edge(newEdges[0][0], newEdges[1][1]) 
		G.add_edge(newEdges[0][1], newEdges[1][0])
		G.remove_edge(newEdges[0][0], newEdges[0][1]) 
		G.remove_edge(newEdges[1][0], newEdges[1][1]) 
	print(G.edges)
	return G

def SearchGraph(G : nx.Graph, node : int, visited : set = None) :
	if visited is None:
		visited = {node}

	for neighbor in G.neighbors(node):
		if neighbor not in visited:
			visited.add(neighbor)
			visited |= SearchGraph(G, neighbor, visited)

	return visited

def GraphComponents(G : nx.Graph) :
	comp = {n : 0 for n in G.nodes}
	nr = 0

	for node in G.nodes:
		if 0 == comp.get(node):
			nr += 1
			for v in SearchGraph(G, node):
				comp[v] = nr

	components = defaultdict(list)
	for key, value in comp.items():
		components[value].append(key)
	return dict(components)
