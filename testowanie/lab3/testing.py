import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab2
from functions import lab3


G = lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 5, 5, 3, 2, 3, 2, 4, 1]), 5)
lab3.randomWeights(G)
lab3.showAllPaths(*lab3.Dijkstra(G, 1))
drw.DrawGraphWithWeights(G)
lab3.GraphCenter(G)