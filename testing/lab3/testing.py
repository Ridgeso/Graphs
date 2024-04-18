import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab2
from functions import lab3

#-------------------EXERCISE 1----------------------------#
G = lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 5, 5, 3, 2, 3, 2, 4, 1]), 5)
lab3.randomWeights(G)


props = lab3.getGrapPropagation(G)
lab3.showAllPaths(*props[1])

#-------------------EXERCISE 1----------------------------#
lab3.GraphCenter(props)
lab3.printWeights(props)
lab3.PrimeAlgorithm(G)
drw.DrawGraphWithWeights(G)