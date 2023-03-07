import networkx as nx   # import해야 사용 가능; 보통 nx로 줄여서 import
import matplotlib.pyplot as plt   # 시각화를 위해 미리 함께 import
#https://chaelist.github.io/docs/network_analysis/network_basics/





# Create an empy undirected graph
g = nx.Graph()
type(g)
g.add_nodes_from([1,2,3,4,5,6]) # Add nodes from a list
g.add_edges_from([(1,3), (2,4), (2,5), (2,6), (3,4), (4,6), (5,6)]) # Add edges from a list
print(g.nodes()) # nodes
print(g.edges()) # edges
print(g.number_of_nodes()) # number of nodes
print(g.number_of_edges()) # number of edges






#Network visualization
nx.draw_networkx(g)
plt.axis('off')  # turn off axis
plt.show()





#node, edge에 attribute 더하기
nx.write_graphml(g, 'graph_test.graphml')
g.nodes[1]['gender'] = 'male'  # {'gender':'male'}이라는 dictionary의 느낌. key-value pair.
g.nodes[2]['gender'] = 'female'
g.nodes[3]['gender'] = 'male'
g.nodes[4]['gender'] = 'female'
g.nodes[5]['gender'] = 'male'
g.nodes[6]['gender'] = 'male'
print(nx.get_node_attributes(g, 'gender'))






#Add edge attributes
g[1][3]['weight'] = 3
g[2][4]['weight'] = 1
g[2][5]['weight'] = 4
g[2][6]['weight'] = 3
g[3][4]['weight'] = 2
g[4][6]['weight'] = 3
g[5][6]['weight'] = 4

print(nx.get_edge_attributes(g, 'weight'))
g.nodes(data=True)  ## node들의 속성까지 함께 볼 수 있음
g.edges(data=True)  ## edge들의 속성까지 함께 볼 수 있음






#edge와 weight를 포함해서 시각화
pos=nx.spring_layout(g)  # 각 node의 position을 정해서 그려줘야 edge_label를 맞춰서 넣을 수 있음
nx.draw_networkx(g, pos)

labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.axis('off')  # turn off axis
plt.show()







#node의 ‘gender’ attribute에 따라 색 다르게 표현
color_map = []
for n, d in g.nodes(data=True):
     if d['gender'] == 'female':
         color_map.append('pink')   # 여성: pink
     else:
         color_map.append('skyblue')   # 남성: skyblue

pos=nx.spring_layout(g)
nx.draw_networkx(g, pos, node_color=color_map)

labels = nx.get_edge_attributes(g,'weight')
plt.axis('off')  # turn off axis
plt.show()








#특정 조건의 node, edge 찾기
female_nodes = [n for n, d in g.nodes(data=True) if d['gender'] == 'female']
print(female_nodes)
strong_edges = [(u, v) for u, v, d in g.edges(data=True) if d['weight'] > 3]#weight가 3보다 큰 edge찾기
print(strong_edges)





#Directed-edge 그래프 그리기
diG = nx.DiGraph()
diG.add_edges_from([(1, 2), (2, 4), (4, 2), (3, 3), (1, 3), (5, 1)]) # edge만 추가해도, 자동으로 이에 포함된 node도 함께 추가됨
nx.draw_networkx(diG)
plt.axis('off')  # turn off axis
plt.show()

nx.number_of_selfloops(diG) #self-loop  개수 파악하기






# 위에서 생성한 g 네트워크를 이어서 사용
nx.draw_networkx(g)
plt.axis('off')  # turn off axis
plt.show()

print(list(g.neighbors(4))) # 4's neighbors
print(g.degree(4)) # 4's degree, i.e., number of neighbors
nx.shortest_path(g, 3, 5)






# 각 node별 degree centrality 값을 dictionary 형태로 보여줌
nx.degree_centrality(g)  # key: node, value: degree centrality score for that node
nx.betweenness_centrality(g) # 각 node별 betweenness centrality 값을 dictionary 형태로 보여줌
nx.closeness_centrality(g) # 각 node별 closeness centrality 값을 dictionary 형태로 보여줌
nx.eigenvector_centrality(g) # 각 node별 eigenvector centrality 값을 dictionary 형태로 보여줌 (얼마나 중심 노드 간 연결이 존재하는지)





import nxviz as nv

color_map = []
for n, d in g.nodes(data=True):
    if d['gender'] == 'female':
        color_map.append('pink')   # 여성: pink
    else:
        color_map.append('skyblue')   # 남성: skyblue

pos=nx.spring_layout(g)
nx.draw_networkx(g, pos, node_color=color_map)

labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g, pos,edge_labels=labels)

plt.axis('off')  # turn off axis
plt.show()

