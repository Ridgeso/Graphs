import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from draw import graph_drawer as drw
from functions import lab5
#-------------------- ZAD 1 ----------------------#
layers = 3
G = lab5.generate_flow_network(layers)
drw.draw_network(G)
#-------------------------------------------------#

#------------------- ZAD 2 ----------------------#
max_flow = lab5.ford_fulkerson(G, 's', 't')
print(f'Maksymalny przepływ: {max_flow}')
drw.draw_network_with_flow(G)
#-------------------------------------------------#
