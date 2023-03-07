"""
edgelist를 adjcency matrix로 변환

import numpy as np
def adjacency_matrix(n, edges):
    adj_matrix = np.zeros((n, n), dtype=int)
    for i, j in edges:
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1
    return adj_matrix

# Example edge list
n = 5
edges = [(0, 1), (1, 2), (2, 3)]

# Create the adjacency matrix
adj_matrix = adjacency_matrix(n, edges)
print(adj_matrix)
"""







# 분석에 사용할 text 준비
import requests
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.washingtonpost.com/" #워싱턴포스트 헤드라인
res = req.urlopen(url) #URL 검색
soup = BeautifulSoup(res, "html.parser") #파싱
news = soup.select("div > h2 > a") #HTML 선택
text = [] #변수 생성
for content in news:
    text.append(content.text)






#Text cleaning
import re #불필요한문자제거
filtered_text = re.sub('[^.,?!\s\w]', ' ', str(text))
filtered_content = filtered_text.lower()






#Tokenization
import nltk
word_tokens = nltk.word_tokenize(filtered_content)






#POS tagging
tokens_pos = nltk.pos_tag(word_tokens)






#Select Noun words
NN_words = []
for word, pos in tokens_pos:
    if 'NN' in pos:
        NN_words.append(word)






#Lemmatization
# nltk의 WordNetLemmatizer을 이용
wlem = nltk.WordNetLemmatizer()
lemmatized_words = []

for word in NN_words:
    new_word = wlem.lemmatize(word)
    lemmatized_words.append(new_word)






#Stopwords removal
# 1차적으로 nltk에서 제공하는 불용어사전을 이용해서 불용어를 제거
from nltk.corpus import stopwords

stopwords_list = stopwords.words('english') #nltk에서 제공하는 불용어사전 이용
unique_NN_words = set(lemmatized_words)   #set을 사용해 중복 제거
final_NN_words = lemmatized_words

for word in unique_NN_words:
    if word in stopwords_list:
        while word in final_NN_words: final_NN_words.remove(word)







# 아래와 같이 추가로 직접 만든 불용어사전을 이용해 불용어 제거
customized_stopwords = ['be', 'today', 'yesterday', 'new', 'york', 'time']  # 직접 만든 불용어 사전
unique_NN_words1 = set(final_NN_words)

for word in unique_NN_words1:
    if word in customized_stopwords:
        while word in final_NN_words: final_NN_words.remove(word)







## final_NN_words 출력해보기
print(final_NN_words)







#Frequency Analysis
from collections import Counter
c = Counter(final_NN_words)
print(c.most_common(10))   # 가장 빈번하게 나오는 10개의 단어 출력






# 가장 많이 나오는 단어 10개 저장
list_of_words = []
for word, count in c.most_common(10):
    list_of_words.append(word)

print(list_of_words)






#원본 text 문장 단위로 쪼개기
# 위에서 만들어두었던 filtered_content을 활용해서 문장을 쪼갬. (., ?, ! 등 문장 구분자 꼭 필요)
sentences = filtered_content.split('.\n')

sentences1 = []
sentences2 = []
sentences3 = []
for sentence in sentences:
     sentences1.extend(sentence.split('. '))
for sentence in sentences1:
     sentences2.extend(sentence.split('!'))
for sentence in sentences2:
     sentences3.extend(sentence.split('?'))
article_sentences = sentences3

print(article_sentences)   ## 각 문장을 element로 담고 있는 list






#단어들을 node로 생성
# 가장 많이 출현하는 10개의 명사 단어들을 node로 하는 network 생성
import networkx as nx

G = nx.Graph()   # undirected graph 생성
G.add_nodes_from(list_of_words)   # node 생성 (가장 많았던 명사 단어 10개)

print(G.nodes()) # nodes
print(G.edges()) # edge, 즉 node 간의 관계는 아직 없는 상황






import itertools

for sentence in article_sentences:  # 각 문장을 element로 담고 있는 list
    sentence = sentence.lower()

    word_tokens = nltk.word_tokenize(sentence)
    tokens_pos = nltk.pos_tag(word_tokens)

    NN_words = []
    for word, pos in tokens_pos:
        if 'NN' in pos:
            NN_words.append(word)

    wlem = nltk.WordNetLemmatizer()
    lemmatized_words = []
    for word in NN_words:
        new_word = wlem.lemmatize(word)
        lemmatized_words.append(new_word)

    selected_words = []
    for word in lemmatized_words:
        if word in list_of_words:
            selected_words.append(word)   # 빈도 top 10에 포함된 단어만 append

    selected_words = set(selected_words)   # 중복을 제거하기 위해 set(집합자료형)으로 변환


    for pair in list(itertools.combinations(list(selected_words), 2)): # itertools.combinations: selected_words 리스트에서 2개씩 골라 조합을 만들어준다
        if pair in G.edges():
            weight = G[pair[0]][pair[1]]['weight']
            weight += 1
            G[pair[0]][pair[1]]['weight'] = weight
        else:
            G.add_edge(pair[0], pair[1], weight=1)


 # 생성된 edge 확인해보기
print(nx.get_edge_attributes(G, 'weight'))







import matplotlib.pyplot as plt

## 노드의 degree에 따라 color 다르게 설정하기
color_map = []
for node in G:
    if G.degree(node) >= 8:   # 중요한 노드 (degree가 8 이상)
        color_map.append('pink')
    else:
        color_map.append('beige')

plt.figure(figsize=(8, 6))  # size 설정
pos = nx.spring_layout(G, scale=0.2)   # spring layout 사용, 글씨가 잘리는 것을 방지하기 위해 scale=0.2로 조정
nx.draw_networkx(G, pos, node_color=color_map, edge_color='grey')
plt.axis('off') # turn off axis
plt.show()






#circular layout으로도 시각화해보기
plt.figure(figsize=(8, 7))

pos = nx.circular_layout(G, scale=0.2)   # circular layout 모양
nx.draw_networkx(G, pos, node_color=color_map, edge_color='grey')  # 위에서 지정한 color_map 그대로 사용

plt.axis('off') # turn off axis
plt.show()







#centrality measures
print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))







#https://chaelist.github.io/docs/network_analysis/semantic_network/

