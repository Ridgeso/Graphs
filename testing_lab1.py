from draw import graph_drawer as drw
from functions import lab1

#-------------------EXERCISE 1----------------------------#

lab1.NeighborhoodMatrixToList('test.txt', 'NeighborhoodList.txt')
lab1.NeighborhoodListToMatrix('NeighborhoodList.txt', 'NeighborhoodMtx.txt')
lab1.NeighborhoodMatrixToIncidence('NeighborhoodMtx.txt', 'IncidenceMtx.txt')
lab1.IncidenceToNeighborhoodMatrix('IncidenceMtx.txt', 'NeighborhoodMtx2.txt')

#----------------------------------------------------------#

#-------------------EXERCISE 3----------------------------#

drw.DrawGraphCircular(lab1.ErodosRenyiaProbability(10, 0.2))
drw.DrawGraphCircular(lab1.ErodosRenyiaEdges(10, 14))

#----------------------------------------------------------#