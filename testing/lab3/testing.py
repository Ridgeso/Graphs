import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab2
from functions import lab3

#-------------------EXERCISE 1----------------------------#
G = lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 5, 5, 3, 2, 3, 2, 4, 1]), 5)
lab3.SetRandomWeights(G, 1, 10)
#-------------------EXERCISE 1----------------------------#


#-------------------EXERCISE 2----------------------------#
lab3.ShowAllPaths(*lab3.Dijkstra(G, 1))
#-------------------EXERCISE 2----------------------------#

#-------------------EXERCISE 3----------------------------#
props = lab3.GetGrapPropagation(G)
lab3.PrintWeights(props)
#-------------------EXERCISE 3----------------------------#

#-------------------EXERCISE 4----------------------------#
lab3.GraphCenter(props)
#-------------------EXERCISE 4----------------------------#

#-------------------EXERCISE 5----------------------------#
T = lab3.PrimeAlgorithm(G)
drw.DrawGraphWithWeights(T)
#-------------------EXERCISE 5----------------------------#

#-------------------EXTENTIONS-----------------------------#
drw.DrawGraphWithWeights(G)
