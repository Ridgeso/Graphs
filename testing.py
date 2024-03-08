from draw import graph_drawer as drw
from functions import lab1

drw.Draw_Graph_Circular(lab1.Erodos_Renyia_Probability(10, 0.2))
drw.Draw_Graph_Circular(lab1.Erodos_Renyia_Edges(10, 14))

lab1.NeighborhoodMatrixToList('test.txt', 'NeighborhoodList.txt')
lab1.NeighborhoodListToMatrix('NeighborhoodList.txt', 'NeighborhoodMtx.txt')
lab1.NeighborhoodMatrixToIncidence('NeighborhoodMtx.txt', 'IncidenceMtx.txt')
lab1.IncidenceToNeighborhoodMatrix('IncidenceMtx.txt', 'NeighborhoodMtx2.txt')