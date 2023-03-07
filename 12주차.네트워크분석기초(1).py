import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

#Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("A", "D")
G.add_edge("C", "D")

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("Closeness Centrality:", closeness_centrality)

# Plot the network
nx.draw(G, with_labels=True)
plt.show()