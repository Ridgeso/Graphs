import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab4

#-------------------- ZAD 1 ----------------------#
G = lab4.DigraphRandomGenerate(10, 0.2)
# print("Lista sąsiedztwa")
# lab4.NeighborhoodListFromDigraph(G)
# print("")
# print("Macierz sąsiedztwa")
# lab4.NeighborhoodMatrixFromDigraph(G)
# print("")
# print("Macierz incydencji")
# lab4.IncidencesMatrixFromDigraph(G)
# print("")
# drw.DrawGraph(G)
#-------------------------------------------------#

#------------------- ZAD 2 ----------------------#
# print("Kosaraju: ", lab4.Kosaraju(G), end='\n\n')
# drw.DrawGraph(G)
#-------------------------------------------------#

G = lab4.DigraphRandomGenerate(4, 0.2)
while len(set(lab4.Kosaraju(G).values()))!=1:
    G = lab4.DigraphRandomGenerate(5, 0.2)
w = lab4.GenerateWeightMatrix(G)

#------------------- ZAD 3 ----------------------#
try:
	print(lab4.BellmanFord(G, w, 1, draw=True), end='\n\n')
	lab4.PrintDistanceMatrix(G, w)
except ValueError as e:
	 print(e)
#-------------------------------------------------#

G = lab4.DigraphRandomGenerate(4, 0.2)
while len(set(lab4.Kosaraju(G).values()))!=1:
    G = lab4.DigraphRandomGenerate(4, 0.2)
w = lab4.GenerateWeightMatrix(G)

#------------------- ZAD 4 ----------------------#
try:
	D, G_with_w = lab4.Johnson(G, w)
	print(D)
	for i in G_with_w.edges(data='weight'):
		print(i)
	drw.DrawGraphWithWeights(G_with_w)
except ValueError as e:
	 print(e)
#-------------------------------------------------#