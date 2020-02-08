# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with your connections
df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})

# Build your graph
G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

# Custom the nodes:
fig = plt.figure()
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='white')
fig.set_facecolor("#00000F")

#If you want to save the figure to png:
plt.savefig('yourname.png', facecolor=fig.get_facecolor() )