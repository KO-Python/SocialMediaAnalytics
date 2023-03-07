import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset

import pandas as pd
import numpy as np
import random
import re
from tqdm import tqdm



#from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



### GPU 또는 CPU 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("cpu와 cuda 중 다음 기기로 학습함:", device)

import pandas as pd
df= pd.read_csv('./nsmc_ratings.txt', sep='\t', encoding='utf8')
df.head()


# 시간 관계상 1000개씩만... 실제에서는 아래 코드 실행하지 말고 모두 학습 필요
d1=df[df['label']==0][:1000]  # negative
d2=df[df['label']==1][:1000]  # positive
df=pd.concat([d1,d2],axis=0)
print(df)


### 학습데이터 전처리
import re
from konlpy.tag import Okt

def tokenize(txt):
    stopwords=['기자','단독','사진']
    txt = re.sub(r"[^가-힣a-zA-Z.]", " ",txt)
    tokens = Okt().morphs(txt, norm=True, stem=True)
    tokens = [d for d in tokens if (len(d)>1)&(d not in stopwords)]
    return tokens

# tokenize('파이썬을 재미있게 학습합니다.')

df['document_token']=df['document'].apply(lambda x: tokenize(x) if x else None)
df



### 주요 토큰(형태소) 확인
all_words = []
for d in list(df['document_token']):
    all_words.append(d)
all_words=sum(all_words, [])

from collections import Counter
count_words = Counter(all_words)
total_words=len(all_words)
sorted_words=count_words.most_common(total_words)
print(sorted_words)



### 사전 생성과 정수 인코딩
dict = {}
for i,(w,f) in enumerate(sorted_words):
    dict[w]=i+1

def int_encoding(txt):
    txt_token=tokenize(txt)
    result=[dict[w] if w in dict.keys() else 0 for w in txt_token]
    return result

df['token_int']=df['document'].apply(lambda x: int_encoding(x) if x else None)
df




### 패딩(padding): 각 문장의 토큰 길이를 같게 정리
import numpy as np

sequence_len=[len(t) for t in list(df['token_int'])]
token_mean=np.mean(sequence_len)
token_max=np.max(sequence_len)
token_90=np.percentile(sequence_len, 90)
print('토큰 개수의 평균='+str(token_mean)+' 최대값='+str(token_max)+' 90% 수준='+str(token_90))

sequence_length=18

def token_padding(token_int, sequence_length):
    token_0 = [0]*sequence_length
    if len(token_int)<=sequence_length:
        for i in range(len(token_int)):
            token_0[i]=token_int[i]
    else:
        for i in range(len(token_int[:sequence_length])):
            token_0[i]=token_int[:sequence_length][i]
    return token_0

df['token_padded']=df['token_int'].apply(lambda x: token_padding(x, sequence_length))
df



### 데이터 분리: 학습용, 검증용, 평가용
import random
split_trainvalid_test=0.8
split_train_valid=0.8

df1=df[['token_padded', 'label']]
df1['ids']=list(range(len(df1)))
train_valid_id=random.sample(list(df1['ids']), int(split_trainvalid_test*len(list(df.index))))
train_id=random.sample(train_valid_id, int(split_train_valid*len(train_valid_id)))
valid_id=list(set(train_valid_id)-set(train_id))
test_id=list(set(list(df1['ids']))-set(train_valid_id))
print('train='+str(len(train_id))+' valid='+str(len(valid_id))+' test='+str(len(test_id)))

train_x=df1[df1['ids'].isin(train_id)]['token_padded'].tolist()
train_y=df1[df1['ids'].isin(train_id)]['label'].tolist()
valid_x=df1[df1['ids'].isin(valid_id)]['token_padded'].tolist()
valid_y=df1[df1['ids'].isin(valid_id)]['label'].tolist()
test_x=df1[df1['ids'].isin(test_id)]['token_padded'].tolist()
test_y=df1[df1['ids'].isin(test_id)]['label'].tolist()



### 데이터 형태를 tensor로 변경하고, 미니배치로 분리: 모델에 입력 준비

#create Tensor Dataset
train_data=TensorDataset(torch.LongTensor(train_x), torch.LongTensor(train_y))
valid_data=TensorDataset(torch.LongTensor(valid_x), torch.LongTensor(valid_y))
test_data=TensorDataset(torch.LongTensor(test_x), torch.LongTensor(test_y))

#dataloader
batch_size=16
train_loader=DataLoader(train_data, batch_size=batch_size, shuffle=True)
valid_loader=DataLoader(valid_data, batch_size=batch_size, shuffle=True)
test_loader=DataLoader(test_data, batch_size=batch_size)

print(train_loader.dataset.tensors)


### 모델 구성

class LSTM_SentimentAnalysis(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, dropout):
        super().__init__()

        # The embedding layer takes the vocab size and the embeddings size as input
        # The embeddings size is up to you to decide, but common sizes are between 50 and 100.
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)

        # The LSTM layer takes in the the embedding size and the hidden vector size.
        # The hidden dimension is up to you to decide, but common values are 32, 64, 128
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)

        # We use dropout before the final layer to improve with regularization
        self.dropout = nn.Dropout(dropout)

        # The fully-connected layer takes in the hidden dim of the LSTM and
        #  outputs a a 3x1 vector of the class scores.
        self.fc = nn.Linear(hidden_dim, 2)

    def forward(self, x, hidden):
        """
        The forward method takes in the input and the previous hidden state
        """

        # The input is transformed to embeddings by passing it to the embedding layer
        embs = self.embedding(x)

        # The embedded inputs are fed to the LSTM alongside the previous hidden state
        out, hidden = self.lstm(embs, hidden)

        # Dropout is applied to the output and fed to the FC layer
        out = self.dropout(out)
        out = self.fc(out)

        # We extract the scores for the final hidden state since it is the one that matters.
        out = out[:, -1]
        return out, hidden

    def init_hidden(self):
        return (torch.zeros(1, batch_size, 32), torch.zeros(1, batch_size, 32))




### model 규정

mymodel = LSTM_SentimentAnalysis(vocab_size=len(dict)+1, embedding_dim=128, hidden_dim=32, dropout=0.2)
mymodel = mymodel.to(device)




### model 학습(train)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(mymodel.parameters(), lr = 5e-4)
epochs = 50

losses = []
val_accs = []
for i, e in enumerate(range(epochs)):

    h0, c0 =  mymodel.init_hidden()

    h0 = h0.to(device)
    c0 = c0.to(device)

    for batch_idx, batch in enumerate(train_loader):

        input = batch[0].to(device)
        target = batch[1].to(device)

        optimizer.zero_grad()
        with torch.set_grad_enabled(True):
            out, hidden = mymodel(input, (h0, c0))
            loss = criterion(out, target)
            loss.backward()
            optimizer.step()
    losses.append(loss.item())

    batch_acc = []
    for batch_idx, batch in enumerate(valid_loader):

        input = batch[0].to(device)
        target = batch[1].to(device)

        optimizer.zero_grad()
        with torch.set_grad_enabled(False):
            out, hidden = mymodel(input, (h0, c0))
            _, preds = torch.max(out, 1)
            preds = preds.to("cpu").tolist()
            batch_acc.append(accuracy_score(preds, target.tolist()))
        val_acc=sum(batch_acc)/len(batch_acc)
    val_accs.append(val_acc)
    print([i, loss.item(), val_acc])




### 손실(loss)과 정확도(acuracy) 변화
from matplotlib import pyplot as plt

plt.plot(losses)
plt.plot(val_accs)



# 최종 정확도 평가: test data 사용
batch_acc = []
for batch_idx, batch in enumerate(test_loader):

    input = batch[0].to(device)
    target = batch[1].to(device)

    optimizer.zero_grad()
    with torch.set_grad_enabled(False):
        out, hidden = mymodel(input, (h0, c0))
        _, preds = torch.max(out, 1)
        preds = preds.to("cpu").tolist()
        batch_acc.append(accuracy_score(preds, target.tolist()))
test_acc=sum(batch_acc)/len(batch_acc)
print('정확도:' + str(test_acc))




### 모델 저장과 불러오기
torch.save(mymodel.state_dict(), './mymodel.pt')
model = LSTM_SentimentAnalysis(vocab_size=len(dict)+1, embedding_dim=128, hidden_dim=32, dropout=0.2)
model.load_state_dict(torch.load('./mymodel.pt'))
model_loaded = model.to('cpu')
model_loaded.eval()


## 일반 문장 테스트
input1='남자 주인공이 연기를 못하고 시나리오가 재미 없어요'
input2='남녀 주인공이 멋있고 연기를 잘해서 감동했어요'

inputs=int_encoding(input1)
#sequence_length=18
inputs=token_padding(inputs, sequence_length)

with torch.no_grad():
    model_loaded.eval()
    inputs = torch.LongTensor(inputs, device='cpu')
    inputs=torch.unsqueeze(inputs, 0)
    out, hidden = model_loaded(inputs, (torch.zeros(1,1,32, device='cpu'), torch.zeros(1,1,32, device='cpu')))
    print(int(torch.max(out, 1)[1][0]))          # 0=negative, 1=positive


