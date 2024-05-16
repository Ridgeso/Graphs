import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab1

#-------------------EXERCISE 1----------------------------#
# lab1.IncidenceToNeighborhoodMatrix('test.txt', 'NMtx.txt')
# lab1.IncidenceToNeighborhoodList('test.txt', 'NList.txt')

# drw.DrawGraphCircular(lab1.GetGraphFromNeighMtx('NMtx.txt'), name = 'Graf z macierzy sasiedztwa')
# drw.DrawGraphCircular(lab1.GetGraphFromList('NList.txt'), name = 'Graf z listy sasiedztwa')
# drw.DrawGraphCircular(lab1.GetGraphFromIncidMtx('IMtx.txt'), name = 'Graf z macierzy incydencji')
#----------------------------------------------------------#


#-------------------EXERCISE 3----------------------------#
drw.DrawGraphCircular(lab1.ErodosRenyiaProbability(11, 0.1), name='Graf losowy G(n,p)')
# drw.DrawGraphCircular(lab1.ErodosRenyiaEdges(11, 54), name='Graf losowy G(n,l)')
#----------------------------------------------------------#