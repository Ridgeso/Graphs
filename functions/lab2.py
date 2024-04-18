import networkx as nx
import random
from collections import defaultdict
from draw import graph_drawer as drw

#----------------------- ZAD 1 ----------------------#
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
#-------------------------------------------------#


#----------------------- ZAD 2 --------------------#
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
#----------------------------------------------------#


#-------------------- ZAD 3 -------------------------#
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
#-------------------------------------------------#


#---------------------- ZAD 4 -------------------#
def IsBridge(G : nx.Graph, u : int, v : int):
	comp_before = len(GraphComponents(G))
	G_temp = G.copy()
	G_temp.remove_edge(u, v)
	comp_after = len(GraphComponents(G_temp))
	return comp_before < comp_after

def GraphRandomGenerateEuler(n : int):
	while True:
		sequence = [random.randint(0, int((n-1)/2))*2 for _ in range(n)]
		if GraphicSeqCheck(sequence):
			G = GraphFromGraphicSeq(sequence)
			if len(GraphComponents(G)) == 1:
				drw.DrawGraphCircular(G)
				return G
	
def EulerCycle(G : nx.Graph):
	if len(GraphComponents(G)) != 1:
		print("Graf nie jest spójny!")
		return None
	for node in G.nodes:
		if G.degree(node)%2 != 0:
			print("Graf posiada wierzchołek o stopniu nieparzystym!")
			return None
	G_copy = G.copy()

	current = list(G_copy.nodes)[0]

	cycle = [current]

	while G_copy.edges():
		for neighbour in G_copy.neighbors(current):
			if len(list(G_copy.neighbors(current))) == 1:
				next = neighbour
				break
			else:
				if not IsBridge(G_copy, current, neighbour):
					next = neighbour
					break
		
		G_copy.remove_edge(current, next)
		cycle.append(next)
		current = next

	cycle_str = ''
	for i in range(0, len(cycle)-2):
		cycle_str += str(cycle[i]) + ' - '
	return cycle_str + str(cycle[len(cycle)-1])

#-------------------------------------------------#


#---------------------- ZAD 5 -------------------------#
def GraphRandomGenerateKRegular(n: int, k: int):
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
#-----------------------------------------------#
					
					
#-------------------- ZAD 6 --------------------#	

def FindHamiltonCycle(G : nx.Graph, current : int, cycle : list, visited : set):
	cycle.append(current)
	visited.add(current)

	if len(cycle) == len(list(G.nodes)):
		if G.has_edge(cycle[-1], cycle[0]):
			return True
		else:
			cycle.pop()
			visited.remove(current)
			return False
	
	for neighbour in G.neighbors(current):
		if neighbour not in visited:
			if FindHamiltonCycle(G, neighbour, cycle, visited):
				return True
	
	cycle.pop()
	visited.remove(current)
	return False

def HamiltonCycle(G : nx.Graph):
	if len(G.nodes) < 3:
		return False
	
	has_degree = False
	for node in G.nodes:
		if G.degree(node) >= int(len(G.nodes)/2):
			has_degree = True
			break
	if not has_degree:
		return False

	drw.DrawGraphCircular(G)

	hamilton_cycle = []
	visited = set()

	if FindHamiltonCycle(G, list(G.nodes)[0], hamilton_cycle, visited):
		cycle_str = ''
		for i in range(0, len(hamilton_cycle)-1):
			cycle_str += str(hamilton_cycle[i]) + ' - '
		print(cycle_str + str(hamilton_cycle[0]))
		return True
	else:
		return False

	

	
#-----------------------------------------------#
