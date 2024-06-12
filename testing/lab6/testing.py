import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab4
from functions import lab6
import numpy as np

####### ZADANIE 1
G = lab4.DigraphRandomGenerate(10, 0.7)
lab6.logParsedPraph(lab6.parsGraph(G))
drw.DrawGraphNoWeights(G)

pageRank = lab6.randomWalk(G)
lab6.logRandomWalk(pageRank)

pageRank = lab6.vectorIteration(G)
lab6.logVectorIter(pageRank)

####### ZADANIE 2
points = np.loadtxt("points.dat")
lab6.simulatedAnnealing(points, 50_000)
