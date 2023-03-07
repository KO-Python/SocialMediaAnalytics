"""

텍스트 데이터에 있는 인물 간 네트워크 분석

"""

import pandas as pd

df = pd.read_csv('debate.csv')
df.head()







import networkx as nx
import matplotlib.pyplot as plt
#create an empty graph object
G = nx.Graph()






import warnings
warnings.filterwarnings("ignore")

#iterate throught the dataframe and add edges
for _, edge in df.iterrows():
    G.add_edge(edge['area'], edge['job'])

nx.draw_networkx(G)
plt.axis('off')
plt.show()






#centrality measures
d = nx.degree_centrality(G)  # key: node, value: degree centrality score for that node
b = nx.betweenness_centrality(G)
c= nx.closeness_centrality(G)







#Correlation with centrality measures
measures = [nx.closeness_centrality(G),
            nx.betweenness_centrality(G, weight='weight'),
            nx.degree_centrality(G)]

cor = pd.DataFrame.from_records(measures, index=['closeness', 'betweenness', 'degree'])
cor.T.corr()
