import networkx as nx
import random
import re

def Erodos_Renyia_Edges(n,l):
    G = nx.Graph()
    matrix = [[-1 for x in range(n)] for y in range(n)]
    if(l > n*(n-1)/2):
        print("The number of edges exceeds the maximum value for this amount of vertexes whis is " + n*(n-1)/2)
        return None
    else:
        for i in range(n):
            G.add_node(i)
        for i in range(l):
            rand1, rand2 = random.sample(range(0,n), 2)
            while matrix[rand1][rand2] != -1:
                rand1, rand2 = random.sample(range(0,n), 2)
            matrix[rand1][rand2] = matrix[rand2][rand1] = i
            G.add_edge(int(rand1), int(rand2))
        return G

def Erodos_Renyia_Probability(n,l):
    G = nx.Graph()
    matrix = [[-1 for x in range(n)] for y in range(n)]
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i>j and random.random() < l:
                G.add_edge(int(i), int(j))
    return G

def CountVertices(filename : str) :
	vertCount = 0
	with open(filename) as file :
		line = file.readline()
		while line != '' :
			vertCount += 1
			line = file.readline()
	return vertCount

def NeighborhoodListToMatrix(filename : str, outputName : str) :
	vertCount = CountVertices(filename)
	NeighborhoodMtx = [['0' for _ in range(vertCount)] for _ in range(vertCount)]
	with open(filename) as file :
		format = '[0-9]+[.][ [0-9]*]*\n'
		line  = file.readline()
		while line != '':
			if re.fullmatch(format, line) != None:
				vertices = re.findall('[0-9]+', line)
				for i in range(len(NeighborhoodMtx)) :
					if str(i) in vertices and str(i) != vertices[0]:
						NeighborhoodMtx[eval(vertices[0])][i] = '1'
			line  = file.readline()
	with open(outputName, 'w') as outFile :
		for i in range(vertCount) :
			for j in range(vertCount) :
				if j != vertCount - 1 :
					outFile.write(NeighborhoodMtx[i][j] + ' ')
				else :
					outFile.write(NeighborhoodMtx[i][j] + '\n')

def NeighborhoodMatrixToList(filename : str, outputName : str) :
	NeighborhoodList = []
	vertCount = CountVertices(filename)
	with open(filename) as file :
		line  = file.readline()
		while line != '':
			vertices = re.findall('[0-1]', line)
			if len(vertices) == vertCount :
				NeighborhoodList.append(str(len(NeighborhoodList)) + '.')
				for i in range(len(vertices)) :
					if vertices[i] == '1' :
						NeighborhoodList[len(NeighborhoodList) - 1] += ' ' + str(i)
			line  = file.readline()
	with open(outputName, 'w') as outFile :
		for row in NeighborhoodList :
			outFile.write(row + '\n')

def NeighborhoodMatrixToIncidence(filename : str, outputName : str) :
	NeighborhoodMtx = []
	vertCount = CountVertices(filename)
	IncidenceMtx = []
	with open(filename) as file :
		line  = file.readline()
		while line != '':
			vertices = re.findall('[0-1]', line)
			NeighborhoodMtx.append(vertices)
			line  = file.readline()
	for i in range(len(NeighborhoodMtx)) :
		for j in range(i) :
			if NeighborhoodMtx[i][j] == '1':
				IncidenceMtx.append(['0' for _ in range(vertCount)])
				IncidenceMtx[len(IncidenceMtx) - 1][i] = IncidenceMtx[len(IncidenceMtx) - 1][j] = '1'
	with open(outputName, 'w') as outFile :
		for j in range(len(IncidenceMtx[0])) :
			for i in range(len(IncidenceMtx)) :
				if i != len(IncidenceMtx) - 1 :
					outFile.write(IncidenceMtx[i][j] + ' ')
				else :
					outFile.write(IncidenceMtx[i][j] + '\n')

def IncidenceToNeighborhoodMatrix(filename : str, outputName : str) :
	IncidenceMtx = []
	vertCount = CountVertices(filename)
	NeighborhoodMtx = [['0' for _ in range(vertCount)] for _ in range(vertCount)]
	with open(filename) as file :
		line  = file.readline()
		while line != '':
			vertices = re.findall('[0-1]', line)
			IncidenceMtx.append(vertices)
			line  = file.readline()
	for j in range(len(IncidenceMtx[0])) :
		ids = [0, 0]
		k = 0
		for i in range(len(IncidenceMtx)) :
			if IncidenceMtx[i][j] == '1':
				ids[k] = i
				k = (k + 1) % 2
		NeighborhoodMtx[ids[1]][ids[0]] = '1'
	for i in range(len(NeighborhoodMtx)) :
		for j in range(i) :
			NeighborhoodMtx[j][i] = NeighborhoodMtx[i][j]
	with open(outputName, 'w') as outFile :
		for i in range(vertCount) :
			for j in range(vertCount) :
				if j != vertCount - 1 :
					outFile.write(NeighborhoodMtx[i][j] + ' ')
				else :
					outFile.write(NeighborhoodMtx[i][j] + '\n')