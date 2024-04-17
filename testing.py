from draw import graph_drawer as drw
from functions import lab1
from functions import lab2
from functions import lab3

drw.DrawGraphCircular(lab1.ErodosRenyiaProbability(10, 0.2))
drw.DrawGraphCircular(lab1.ErodosRenyiaEdges(10, 14))
###########################
lab1.NeighborhoodMatrixToList('test.txt', 'NeighborhoodList.txt')
lab1.NeighborhoodListToMatrix('NeighborhoodList.txt', 'NeighborhoodMtx.txt')
lab1.NeighborhoodMatrixToIncidence('NeighborhoodMtx.txt', 'IncidenceMtx.txt')
lab1.IncidenceToNeighborhoodMatrix('IncidenceMtx.txt', 'NeighborhoodMtx2.txt')
############################
print(lab2.GraphicSeqCheck([4, 3, 3, 2, 2, 1, 1]))
drw.DrawGraphCircular(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]))
drw.DrawGraphCircular(lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]), 5))
drw.DrawGraphCircularMulticolor(
    lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]),
    lab2.GraphComponents(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1])),
    {1 : 'skyblue', 2 : 'red'})
#lab 2 zad 5
drw.DrawGraphCircular(lab2.GraphRandomGenerate(7,2))
###########################
G = lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 5, 5, 3, 2, 3, 2, 4, 1]), 5)
lab3.randomWeights(G)
lab3.showAllPaths(*lab3.Dijkstra(G, 1))
drw.DrawGraphWithWeights(G)
lab3.GraphCenter(G)