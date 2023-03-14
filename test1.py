##### https://www.datacamp.com/tutorial/networkx-python-graph-tutorial

import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#### Grab edge list data hosted on Gist
edgelist = pd.read_csv('./edgelist_sleeping_giant.csv')
#print(edgelist.head(10))

#### Grab node list data hosted on Gist
nodelist = pd.read_csv('./nodelist_sleeping_giant.csv')
#print(nodelist.head(10))

#### Create empty graph
g = nx.Graph()

#### Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())
    ##### Edge list example
    #print(elrow[0]) #### node1
    #print(elrow[1]) #### node2
    #print(elrow[2:].to_dict()) #### edge attribute dict

#### Add node attributes
for i, nlrow in nodelist.iterrows():
    ###### https://stackoverflow.com/questions/58518554/attributeerror-graph-object-has-no-attribute-node
    ###### https://stackoverflow.com/questions/47045155/typeerror-nodeview-object-does-not-support-item-assignment-networkx
    g.nodes[nlrow['id']].update(nlrow[1:].to_dict())
    ##### Node list example
    #print(nlrow)

#### Preview first 5 edges
##### https://stackoverflow.com/questions/47325667/object-is-not-subscripable-networkx
#print(list(g.edges(data=True))[0:5])
#print(list(g.nodes(data=True))[0:10])

#### Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]['X'], -node[1]['Y']) for node in g.nodes(data=True)}

#### Preview of node_positions with a bit of hack (there is no head/slice method for dictionaries).
#print(dict(list(node_positions.items())[0:5]))


#### Define data structure (list) of edge colors for plotting
edge_colors = [e[2]['attr_dict']['color'] for e in g.edges(data=True)]

#### Preview first 10
#print(edge_colors[0:10])

#### Now you can make a nice plot that lines up nicely with the Sleeping Giant trail map:
plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
plt.title('Graph Representation of Sleeping Giant Trail Map', size=15)
plt.show()

"""
Stopping Point:

https://www.datacamp.com/tutorial/networkx-python-graph-tutorial#overview-of-cpp-algorithm
"""
