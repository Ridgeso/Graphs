import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab4

#-------------------- ZAD 1 ----------------------#
G = lab4.DigraphRandomGenerate(10, 0.2)
# drw.DrawGraph(G)
# lab4.NeighborhoodListFromDigraph(G)
# print("")
# lab4.NeighborhoodMatrixFromDigraph(G)
# print("")
# lab4.IncidencesMatrixFromDigraph(G)
# print("")
#-------------------------------------------------#


#------------------- ZAD 2 ----------------------#
print(lab4.Kosaraju(G))
#-------------------------------------------------#

#------------------- ZAD 3 ----------------------#
lab4.BellmanFord(G, lab4.GenerateWeightMatrix(G), 1)
#-------------------------------------------------#

#------------------- ZAD 3 ----------------------#
for i in lab4.Johnson(G, lab4.GenerateWeightMatrix(G)):
    for j in i:
        print(j, end=" ")
    print("")
#-------------------------------------------------#