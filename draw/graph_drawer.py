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
def DrawGraph(G : nx.Graph, pos = None, color='skyblue', labels = True, name = None):
    plt.figure(num=name)
    nx.draw(G, pos = pos, with_labels = labels, node_color=color)
    saveOrShowFig()

def DrawGraphCircular(G : nx.Graph, color='skyblue', labels = True, name = None):
    plt.figure(num=name)
    nx.draw_circular(G, with_labels = labels, node_color=color)
    ax = plt.gca()
    circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='dotted')
    ax.add_artist(circle)
    saveOrShowFig()
#--------------------------------------------------------------#




def DrawGraphPlanar(G, color='skyblue', labels = True, name = None):
    plt.figure(num=name)
    nx.draw_planar(G, with_labels = labels, node_color=color)
    saveOrShowFig()

def DrawGraphCircularMulticolor(G : nx.Graph, colorToNodes, colors, labels = True, name = None):
    plt.figure(num=name)
    nodesToColor = {}
    for key in colorToNodes:
        nodesToColor.update({value : key for value in colorToNodes[key]})
    nodesToColor = dict(sorted(nodesToColor.items()))
    nodeColors = [colors[nodesToColor[node]] for node in nodesToColor]
    nx.draw_circular(G, with_labels = labels, node_color=nodeColors)
    ax = plt.gca()
    circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='dotted')
    ax.add_artist(circle)
    saveOrShowFig()

def DrawGraphWithWeights(G : nx.Graph, name = None):
    plt.figure(num=name)
    pos=nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    saveOrShowFig()

def DrawGraphNoWeights(G : nx.Graph, name = None):
    plt.figure(num=name)
    pos=nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    nx.draw_networkx_edges(G, pos)
    saveOrShowFig()

#-------------------LAB 5----------------------------#
def draw_network(G):
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{G[u][v]['capacity']}" for u, v in G.edges()}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.show()

def draw_network_with_flow(G):
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{G[u][v]['flow']}/{G[u][v]['capacity']}" for u, v in G.edges()}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.show()

