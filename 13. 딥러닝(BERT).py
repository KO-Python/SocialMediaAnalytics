"""
BERT (Bidirectional Encoder Representations from Transformers) is a large deep learning model that requires significant
computational resources to train. This is why BERT typically requires a GPU (Graphics Processing Unit) for training.

GPUs are designed to handle complex parallel computations and are well-suited for training large deep learning models like BERT.
They can perform the matrix operations required for deep learning at a much faster pace than CPUs (Central Processing Units).
This allows for faster training times, which is particularly important for models like BERT,
which require a large amount of data and computational resources to train.

Additionally, GPUs typically have a large amount of memory (VRAM), which is needed to store the model's parameters and
intermediate results during training. This memory is important for training models like BERT, which have a large number
of parameters and require a lot of memory to store the intermediate computations.

In summary, the use of a GPU for training BERT is crucial to ensure fast and efficient training times,
and to accommodate the large computational and memory requirements of this model.

GPT는 이전 단어들이 주어졌을 때 다음 단어가 무엇인지 알아맞히는 프리트레인이라고 (일방향), BERT는 문장 중간에 빈칸을 만들고 해당 빈칸에 어떤 단어가 적합한지
알아맞추는 양방향 프리트레인 방식
"""






import pandas as pd

data= pd.read_csv('./nsmc_ratings.txt', sep='\t', encoding='utf8')
print(data.head())
print(data.columns)   # ['id', 'document', 'label']
data.groupby('label').count()  # 1=긍정, 0=부정

# 시간 관계상 1000개씩만... 실제에서는 아래 코드 실행하지 말고 모두 학습 필요
d1=data[data['label']==0][:1000]
d2=data[data['label']==1][:1000]
data=pd.concat([d1,d2],axis=0)
print(data)



from sklearn.model_selection import train_test_split

df_train_val, df_test=train_test_split(data, test_size=0.2, shuffle=True, random_state=123)
df_train, df_val=train_test_split(df_train_val, test_size=0.15, shuffle=True, random_state=123)
print(len(df_train), len(df_val), len(df_test))

print(df_train.groupby('label').count())
print(df_val.groupby('label').count())
print(df_test.groupby('label').count())

downstream_corpus_model_save="/content/drive/MyDrive/ratsnlp/nsmc긍부정/"

df_train.to_csv(downstream_corpus_model_save+"train.txt", sep="\t", index=False)
df_val.to_csv(downstream_corpus_model_save+"val.txt", sep="\t", index=False)
df_test.to_csv(downstream_corpus_model_save+"test.txt", sep="\t", index=False)


