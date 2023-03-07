#단어 빈도 그래프

import nltk
#nltk.download('gutenberg') #구텐베르그 프로젝트 다운로드





from nltk.corpus import gutenberg
file_names = gutenberg.fileids()#제목으로 열기
print(file_names) #파일 이름 확인하기






#특정 파일 불러오기
tokens_alice = gutenberg.open('carroll-alice.txt').read()
print('#Number of Character Used>>>', len(tokens_alice))#사용된 문자의 수
print('Text Sample>>>')
print(tokens_alice[:500])#처음 500자만 출력







#NLTK를 활용한 토큰화
from nltk.tokenize import word_tokenize
tokens = word_tokenize(tokens_alice)#doc_alice 토크나이징







print('#Number of Tokens Used>>>', len(tokens_alice))#사용된 문자의 수
print('Tokens Sample>>>')
print(tokens[:20])#20개 확인







from nltk.stem import PorterStemmer #포터스테밍
stemmer = PorterStemmer() #포터스테머함수적용







stem_tokens_alice = [stemmer.stem(token) for token in tokens_alice] #모든 토큰에 대해 스테밍 실행
print('#Num of tokens after stemming:', len(stem_tokens_alice)) #스테밍 후 단어 수 확인
print('#Token sample >>>')
print(stem_tokens_alice[:20])







from nltk.stem import WordNetLemmatizer #WordNetLemmatizer를 활용해 표제어 추출
lemmatizer = WordNetLemmatizer() #토큰 수와 앞의 20개 토큰 스테밍 결과와 비교하기







lem_tokens_alice = [lemmatizer.lemmatize(token) for token in tokens_alice] #모든 토큰에 대해 스테밍 실행
print('#Num of tokens after lemmatization:', len(lem_tokens_alice))
print('#Token sample:')
print(lem_tokens_alice[:20])






from nltk.tokenize import RegexpTokenizer #정규표현식을 활용해 토큰화 결과 비교하기
tokenizer = RegexpTokenizer("[\w']{3,}")






reg_tokens_alice = tokenizer.tokenize(tokens_alice.lower()) #정규표현식을 활용한 토크나이징
print('#Num of tokens with RegexpTokenizer:', len(reg_tokens_alice)) #토큰 수가 현저히 줄어듦
print('#Token sample:')
print(reg_tokens_alice[:20])







from nltk.corpus import stopwords #일반적으로 분석대상이 아닌 단어들
english_stops = set(stopwords.words('english')) #반복이 되지 않도록 set으로 변환







result_alice = [word for word in reg_tokens_alice if word not in english_stops] #stopwords를 제외한 단어들만으로 list를 생성
print('#Num of tokens after stopword elimination:', len(result_alice)) #토큰 수가 줄어듦
print('#Token sample:')
print(result_alice[:20])







alice_word_count = dict() #딕셔너리함수로 단어 별 갯수 파악
for word in result_alice:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1 #빈도가 큰순으로 정렬






print('#Num of used words:', len(alice_word_count)) #단어 수 파악
sorted_word_count = sorted(alice_word_count, key=alice_word_count.get, reverse=True)#단어 정렬 후 변수 생성
print("#Top 20 high frequency words:")
for key in sorted_word_count[:20]: #빈도수 상위 20개의 단어를 출력
    print(f'{repr(key)}: {alice_word_count[key]}', end=', ') #딕셔너리 함수로 단어와 숫자를 정렬해서 출력







my_tag_set = ['NN', 'VB', 'VBD', 'JJ']
#NN = Noun, singular 'desk'
#VB = Verb
#VBD = Verb, past tense took
#JJ = Adjective big







my_words = [word for word, tag in nltk.pos_tag(result_alice) if tag in my_tag_set]
#print(my_words) #단어 확인 하고 싶으면 주석 풀고 실행

alice_word_count = dict() #딕셔너리 함수로 변수 생성
for word in my_words:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1

print('#Num of used words:', len(alice_word_count)) #단어 수 확인 후 출력
sorted_word_count = sorted(alice_word_count, key=alice_word_count.get, reverse=True) #단어 빈도 순서로 정렬 후 변수 생성

print("#Top 20 high frequency words:") #상위 20개 출력함수
for key in sorted_word_count[:20]: #빈도수 상위 20개의 단어를 출력
    print(f'{repr(key)}: {alice_word_count[key]}', end=', ') #딕셔너리 데이터형으로 출력







#시각화
import matplotlib.pyplot as plt
w = [alice_word_count[key] for key in sorted_word_count] #정렬된 단어 리스트에 대해 빈도수를 가져와서 리스트 생성
plt.plot(w) #단어 빈도가 극적 차이가 존재함
plt.show() #단어 순위가 100위만 넘어가도 빈도 수가 현저히 줄어듦

"""
지프의 법칙 (Zipf's law)
말뭉치의 단어들을 사용 빈도가 높은 순서대로 나열하면 단어의 사용 빈도는 단어의 순위에 반비례함 
텍스트 마이닝 관점에서 말뭉치에서의 단어 빈도가 상위 몇개에 집중됨 
"""







n = sorted_word_count[:20] #빈도수 상위 20개의 단어만 추출
w = [alice_word_count[key] for key in n] #추출된 단어에 대해 빈도를 추출
plt.bar(range(len(n)),w,tick_label=n) #막대그래프를 그림
plt.show()







n = sorted_word_count[:20][::-1] #빈도수 상위 20개의 단어를 추출하여 역순으로 정렬
w = [alice_word_count[key] for key in n]
plt.barh(range(len(n)),w,tick_label=n) #수평 막대그래프
plt.show()





from wordcloud import WordCloud  # Generate a word cloud image
wordcloud = WordCloud().generate(tokens_alice)
plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear') #이미지를 출력
plt.show()
wordcloud.to_array().shape #nd-array size (width, height, 3)







wordcloud = WordCloud(max_font_size=60).generate_from_frequencies(alice_word_count) #폰트 사이즈 조정
plt.figure()
plt.axis("off")
plt.imshow(wordcloud, interpolation="bilinear") #2차원 차트
plt.show()







import numpy as np
from PIL import Image







alice_mask = np.array(Image.open("alice_mask.png")) # 배경이미지를 불러와서 numpy array로 변환
wc = WordCloud(background_color="white", # 배경색 지정
               max_words=30, # 출력할 최대 단어 수
               mask=alice_mask, # 배경으로 사용할 이미지
               contour_width=3,  # 테두리선의 크기
               contour_color='steelblue') # 테두리선의 색

wc.generate_from_frequencies(alice_word_count) # 워드 클라우드 생성
wc.to_file("alice.png") # 결과를 이미지 파일로 저장
plt.figure()# 화면에 결과를 출력
plt.axis("off") #축 눈금제외
plt.imshow(wc, interpolation='bilinear')
plt.show()



