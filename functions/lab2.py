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

#lab 2 zad 5
def GraphRandomGenerate(n: int, k: int):
	def min_index(node: int, degree: list):
		min_degree = min(degree)
		min_degree_nodes = [i for i, d in enumerate(degree) if d == min_degree]
		min_index = min_degree_nodes[0]
		if min_index != node:
			return min_index
		elif len(min_degree_nodes) > 1:
			return min_degree_nodes[1]  
		else:
			return None

	if n * k % 2 != 0 or n <= k:
		raise ValueError("Nie można wygenerować grafu k-regularnego dla podanych wartości n i k.")    
	
	G = nx.Graph()
	G.add_nodes_from(range(n))
	degree = [0] * n
	
	for node in G.nodes:
		while degree[node] < k:
			index = min_index(node, degree)
			if degree[index] < k and not G.has_edge(node, index):
				G.add_edge(node, index)
				degree[node] += 1
				degree[index] += 1
	G = RandomizeEdges(G, 5)
	return G

					
					
				
		
	
