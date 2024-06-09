
import sys
import os
from networkx import Graph
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from draw import graph_drawer as drw
from functions import lab6
from functions import lab4
import numpy as np

pagerank_random = lab6.pagerank_random_walk(lab4.DigraphRandomGenerate(10, 0.2))
pagerank_iter = lab6.pagerank_iteration(lab4.DigraphRandomGenerate(10, 0.2))

norm_diff = np.linalg.norm(pagerank_random - pagerank_iter)
print(pagerank_random)
print(pagerank_iter)
print("Norma różnicy:", norm_diff)
