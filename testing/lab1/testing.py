import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab1

#-------------------EXERCISE 1----------------------------#
lab1.NeighborhoodMatrixToList('test.txt', 'NList.txt')
lab1.NeighborhoodListToMatrix('NList.txt', 'NMtx.txt')
lab1.NeighborhoodMatrixToIncidence('NMtx.txt', 'IMtx.txt')
lab1.IncidenceToNeighborhoodMatrix('IMtx.txt', 'NMtx2.txt')
lab1.IncidenceToNeighborhoodList('IMtx.txt', 'NList2.txt')
lab1.NeighborhoodListToIncidence('NList.txt', 'IMtx2.txt')

drw.DrawGraphCircular(lab1.GetGraphFromNeighMtx('test.txt'), name = 'Graf z macierzy sasiedztwa')
drw.DrawGraphCircular(lab1.GetGraphFromList('NList.txt'), name = 'Graf z listy sasiedztwa')
drw.DrawGraphCircular(lab1.GetGraphFromIncidMtx('IMtx.txt'), name = 'Graf z macierzy incydencji')
#----------------------------------------------------------#


#-------------------EXERCISE 3----------------------------#
drw.DrawGraphCircular(lab1.ErodosRenyiaProbability(10, 0.2), name='Graf losowy G(n,p)')
drw.DrawGraphCircular(lab1.ErodosRenyiaEdges(10, 14), name='Graf losowy G(n,l)')
#----------------------------------------------------------#