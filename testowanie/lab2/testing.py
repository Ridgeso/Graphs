import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab2

#-------------------EXERCISE 1----------------------------#
print(lab2.GraphicSeqCheck([4, 3, 3, 2, 2, 1, 1]))
drw.DrawGraphCircular(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]))
#---------------------------------------------------------#


#-------------------EXERCISE 2----------------------------#
drw.DrawGraphCircular(lab2.RandomizeEdges(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]), 5))
#---------------------------------------------------------#


#-------------------EXERCISE 3----------------------------#
drw.DrawGraphCircularMulticolor(
    lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]),
    lab2.GraphComponents(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1])),
    {1 : 'skyblue', 2 : 'red'})
#---------------------------------------------------------#


#-------------------EXERCISE 4----------------------------#
print(lab2.EulerCycle(lab2.GraphRandomGenerateEuler(10)))
#---------------------------------------------------------#


#-------------------EXERCISE 5----------------------------#
drw.DrawGraphCircular(lab2.GraphRandomGenerateKRegular(7,2))
#---------------------------------------------------------#


#-------------------EXERCISE 6----------------------------#
print(lab2.HamiltonCycle(lab2.GraphRandomGenerateKRegular(6, 4)))
#---------------------------------------------------------#