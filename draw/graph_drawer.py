import networkx as nx
import matplotlib.pyplot as plt

##### lab 1 excercide 2 #######

def Draw_Graph(G, pos = None, color='skyblue', labels = True):
    nx.draw(G, pos = pos, with_labels = labels, node_color=color)
    plt.show()

def Draw_Graph_Circular(G, color='skyblue', labels = True):
    nx.draw_circular(G, with_labels = labels, node_color=color)
    plt.show()

def Draw_Graph_Planar(G, color='skyblue', labels = True):
    nx.draw_planar(G, with_labels = labels, node_color=color)
    plt.show()