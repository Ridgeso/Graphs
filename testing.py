from draw import graph_drawer as drw
from functions import lab1
from functions import lab2

drw.Draw_Graph_Circular(lab1.Erodos_Renyia_Probability(10, 0.2))
drw.Draw_Graph_Circular(lab1.Erodos_Renyia_Edges(10, 14))
###########################
lab1.NeighborhoodMatrixToList('test.txt', 'NeighborhoodList.txt')
lab1.NeighborhoodListToMatrix('NeighborhoodList.txt', 'NeighborhoodMtx.txt')
lab1.NeighborhoodMatrixToIncidence('NeighborhoodMtx.txt', 'IncidenceMtx.txt')
lab1.IncidenceToNeighborhoodMatrix('IncidenceMtx.txt', 'NeighborhoodMtx2.txt')
############################
print(lab2.GraphicSeqCheck([4, 3, 3, 2, 2, 1, 1]))
drw.Draw_Graph_Circular(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]))
drw.Draw_Graph_Circular(lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]), 5))
drw.Draw_Graph_Circular_Multicolor(
    lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]),
    lab2.GraphComponents(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1])),
    {1 : 'skyblue', 2 : 'red'})
#lab 2 zad 5
drw.Draw_Graph_Circular(lab2.GraphRandomGenerate(7,2))