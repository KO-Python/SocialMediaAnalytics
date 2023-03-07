#엣지리스트 데이터 생성

# Define the graph as a list of edges
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D")]

# Print the edge list
print("Edge List:")
for u, v in edges:
    print(u, "->", v)






#인접행렬매트릭스 생성
import numpy as np

# Define the graph as a list of edges
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D")]

# Get the unique nodes in the graph
nodes = set()
for u, v in edges:
    nodes.add(u)
    nodes.add(v)

# Create a dictionary mapping nodes to indices
node_to_index = {node: i for i, node in enumerate(sorted(nodes))}

# Create the adjacency matrix
n = len(nodes)
adj_matrix = np.zeros((n, n), dtype=int)
for u, v in edges:
    i = node_to_index[u]
    j = node_to_index[v]
    adj_matrix[i, j] = 1
    adj_matrix[j, i] = 1

print("Adjacency Matrix:")
print(adj_matrix)