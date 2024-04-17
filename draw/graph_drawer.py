import networkx as nx
import matplotlib.pyplot as plt
import os
import sys

saveToImFlag = '--image' in sys.argv or '-i' in sys.argv

def saveOrShowFig():
    if saveToImFlag:
        plt.savefig(os.path.abspath(os.path.dirname(__file__)))
    else:
        plt.show()

#-------------------LAB 1 EXERCISE 2----------------------------#

def DrawGraph(G, pos = None, color='skyblue', labels = True):
    nx.draw(G, pos = pos, with_labels = labels, node_color=color)
    saveOrShowFig()

def DrawGraphCircular(G, color='skyblue', labels = True):
    nx.draw_circular(G, with_labels = labels, node_color=color)
    saveOrShowFig()

#--------------------------------------------------------------#




def DrawGraphPlanar(G, color='skyblue', labels = True):
    nx.draw_planar(G, with_labels = labels, node_color=color)
    saveOrShowFig()

def DrawGraphCircularMulticolor(G : nx.Graph, colorToNodes, colors, labels = True):
    nodesToColor = {}
    for key in colorToNodes:
        nodesToColor.update({value : key for value in colorToNodes[key]})
    nodesToColor = dict(sorted(nodesToColor.items()))
    nodeColors = [colors[nodesToColor[node]] for node in nodesToColor]
    nx.draw_circular(G, with_labels = labels, node_color=nodeColors)
    plt.savefig(os.path.abspath(os.path.dirname(__file__)))
    saveOrShowFig()

def DrawGraphWithWeights(G : nx.Graph):
    pos=nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    saveOrShowFig()
