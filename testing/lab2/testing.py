import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab2

#-------------------EXERCISE 1----------------------------#
print(lab2.GraphicSeqCheck([4, 3, 3, 2, 2, 1, 1]))
drw.DrawGraphCircular(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]), name='Graf powstały z ciągu graficznego')
#---------------------------------------------------------#


#-------------------EXERCISE 2----------------------------#
G = lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1])
drw.DrawGraphCircular(G, name='Graf przed randomizacją')
drw.DrawGraphCircular(lab2.RandomizeEdges(G, 5), name='Graf po randomizacji')
#---------------------------------------------------------#


#-------------------EXERCISE 3----------------------------#
drw.DrawGraphCircularMulticolor(
    lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1]),
    lab2.GraphComponents(lab2.GraphFromGraphicSeq([1, 3, 2, 3, 2, 4, 1])),
    {1 : 'skyblue', 2 : 'red'}, name='Największa spójna składowa')
#---------------------------------------------------------#


#-------------------EXERCISE 4----------------------------#
G = lab2.GraphRandomGenerateEuler(5)
drw.DrawGraphCircular(G,  name='Graf, w którym szukamy cyklu Eulera')
lab2.EulerCycle(G)
#---------------------------------------------------------#


#-------------------EXERCISE 5----------------------------#
drw.DrawGraphCircular(lab2.GraphRandomGenerateKRegular(7,2), name='Graf k-regularny')
#---------------------------------------------------------#


#-------------------EXERCISE 6----------------------------#
G = lab2.GraphRandomGenerateKRegular(14, 9)
drw.DrawGraphCircular(G, name='Graf, w którym szukamy cyklu Hamiltona')
lab2.HamiltonCycle(G)
#---------------------------------------------------------#