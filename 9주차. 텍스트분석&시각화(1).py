import nltk

#분석에 필요한 NLTK library download

nltk.download('punkt')
nltk.download('webtext')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')




#문장 토큰화 (영어)
para = "Hello everyone. It's good to see you. Let's start our text mining class!"






from nltk.tokenize import sent_tokenize #토크나이징






print(sent_tokenize(para)) #주어진 text를 sentence 단위로 tokenize함. 주로 . ! ? 등을 기준으로 함






#문장 토큰화 (한글)
para_kor = "안녕하세요, 여러분. 만나서 반갑습니다. 이제 텍스트마이닝 클래스를 시작해봅시다!"
print(sent_tokenize(para_kor)) #한국어에 대해서도 sentence tokenizer 작동 원활






#단어 토큰화 (영문)
from nltk.tokenize import word_tokenize #토크나이저 첫 번째 유형
print(word_tokenize(para)) #주어진 text를 word 단위로 tokenize함






from nltk.tokenize import WordPunctTokenizer #토크나이저 두 번째 유형
print(WordPunctTokenizer().tokenize(para))






#단어 토큰화 (한글)
print(word_tokenize(para_kor))






"""
정규표현식을 이용한 토큰화 
1. NLTK 제공 함수 토큰화 간편함 
2. 세밀한 토큰화 단점 
3. regex (정규표현식): 대상 문자열로부터 원하는 패턴의 문자열 검색가능 
"""






import re
re.findall("[abc]", "how are you, boy") #문장에서 a와 b가 있는지 검색
re.findall("[0123456789]", "3a7b5c9d") #문자에서 숫자 검색
#[a-zA-Z] 모든 알파벳 검색
#[a-zA-Z0-9] 알파벳 숫자 검색
# [\w] 모든 알파벳 숫자 검색
re.findall("[\w]+", "How are you, boy?")
re.findall("[o]{2,4}", "oh, hoow are yoooou, boooooooy?") #문장에서 O가 2-4회 반복된 문자 검색






#정규표현식 활용 토크나이저
"""
NLTK에서는 정규표현식을 사용하는 RegexTokenizer를 제공함 
RegexTokenizer() 함수의 인수로 원하는 정규표현식 기반 토큰화 수행함 
"""






from nltk.tokenize import RegexpTokenizer






#example1
tokenizer = RegexpTokenizer("[\w']+") #regular expression(정규식)을 이용한 tokenizer
#단어단위로 tokenize \w:문자나 숫자를 의미 즉 문자나 숫자 혹은 '가 반복되는 것을 찾아냄






print(tokenizer.tokenize("Sorry, I can't go there."))
# can't를 하나의 단어로 인식






#example2
tokenizer = RegexpTokenizer("[\w]+")
print(tokenizer.tokenize("Sorry, I can't go there."))






#example3
text1 = "Sorry, I can't go there."
tokenizer = RegexpTokenizer("[\w']{3,}") #문자를 소문자로 변경; 세 글자 이상 단어만 선택
print(tokenizer.tokenize(text1.lower()))






"""
노이즈와 불용어 제거 
NLTK: stopwords library를 통해 불용어 제공 
"""






from nltk.corpus import stopwords #일반적으로 분석대상이 아닌 단어들
english_stops = set(stopwords.words('english')) #반복이 되지 않도록 set으로 변환






text1 = "Sorry, I couldn't go to movie yesterday."






tokenizer = RegexpTokenizer("[\w']+")
tokens = tokenizer.tokenize(text1.lower()) #word_tokenize로 토큰화






result = [word for word in tokens if word not in english_stops] #stopwords를 제외한 단어들만으로 list를 생성
print(result)






#nltk가 제공하는 stopwords 리스트 확인
print(english_stops)






#불용어 사전 만들기
my_stopwords = ['i', 'go', 'to']
result = [word for word in tokens if word not in english_stops] #stopwords를 제외한 단어들만으로 list를 생성
print(result)






"""
정규화 
같은 의미를 가진 동일한 단어이면서 다른 형태로 사용된 단어를 통일해 표준화 작업
1. 어간추출 (stem)
2. 표제어 추출 (lemmatization)
"""






from nltk.stem import PorterStemmer #포터스테머가 고안한 어간 추출 예
stemmer = PorterStemmer()
print(stemmer.stem('cooking'), stemmer.stem('cookery'), stemmer.stem('cookbooks'))






#토큰화와 결합하여 어간 추출 사례
from nltk.tokenize import word_tokenize
para = "Hello everyone. It's good to see you. Let's start our text mining class!"
tokens = word_tokenize(para) #토큰화 실행
print(tokens)






result = [stemmer.stem(token) for token in tokens] #모든 토큰에 대해 스테밍 실행
print(result)







#랭카스터 스테머
from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()
print(stemmer.stem('cooking'), stemmer.stem('cookery'), stemmer.stem('cookbooks'))






"""
표제어추출
표제어 (lemmatization): 단어의 기본현으로 변환 
WordNet을 활용한 어휘 데이터베이스 활용 (영어) 
"""






from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('cooking'))
print(lemmatizer.lemmatize('cooking', pos='v')) #품사를 지정
print(lemmatizer.lemmatize('cookery'))
print(lemmatizer.lemmatize('cookbooks'))






#lemmatizing and stemming 비교
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print('stemming result:', stemmer.stem('believes'))
print('lemmatizing result:', lemmatizer.lemmatize('believes'))
print('lemmatizing result:', lemmatizer.lemmatize('believes', pos='v'))






"""
품사태깅

CC = Coordinating conjunction
CD = Cardinal number 
DT = Determiner 
EX = Existential there (like: there is)
FW = Foreign word 
IN = Prepositio/subordinating conjunction 
JJ = Adjective big 
JJR = Adjective, comparative bigger 
JJS = Adjective, superlative biggest 
LS = List market 
MD = Modal could, will 
NN = Noun, singular 'desk' 
NNS = Noun plural desks 
NNP = proper noun, singular 'Harrison' 
NNPS = Proper noun, plural 'Americans'
PDT = Predeterminer 'all the kids' 
POS = Possessive ending parent's 
PRP = Personal Pronoun, I, he, she
PRP$ = Possesive pronoun my, his, hers
RB = Adverb very, silently
RBR = Adverb, very silently 
RBS = Adverb, superlative best 
RP = Paricle give up 
To = To go
UH = Interjection
VB = Verb
VB = Verb, base from take 
VBD = Verb, past tense took 
VBG = Verb, gerund/present participle taking 
VBN = Verb, past participle taken 
VBP = Verb, sing, present, non-3rd take 
VBZ = Verb, 3rd person sing
WDT = Wh-determiner which 
WP = Wh-proboun who, what 
WP$ = Posseesive wh-pronoun whose 
WRB = Wh-adverb where, when 

"""






#NLTK 활용 품사태깅
import nltk
from nltk.tokenize import word_tokenize





tokens = word_tokenize("Hello everyone. It is good to see you. Let's start our class")
print(nltk.pos_tag(tokens))





#품사태깅에 관한 설명 보고 싶은 경우
nltk.help.upenn_tagset('CC')





#원하는 품사의 단어 추출
my_tag_set = ['NN', 'VB', 'JJ']
my_words = [word for word, tag in nltk.pos_tag(tokens) if tag in my_tag_set]
print(my_words)





#한글 형태소 분석과 품사 태깅
sentence = '''절망의 반대는 희망이 아니다. 
어두운 밤하늘에 별이 빛나듯 
희망은 절망 속에 싹트는 거지 
만약에 우리가 희망함이 적다면 
그 누가 세상을 비추어줄까 
'''





tokens = word_tokenize(sentence)
print(tokens)
print(nltk.pos_tag(tokens))





"""
KoNLP 설치 
1. 맥 또는 리눅스 Jpypel을 별도 설치 필요 없음 
2. 윈도우 사용자 - 자바 1.7이상 설치 
3. 윈도우 Mecab 클래스 지원하지 않음
"""





from konlpy.tag import Okt
t = Okt()






"""
morphs(phrase): 주어진 텍스트를 형태소 단위로 분리함 
nouns(phrase): 주어진 텍스트를 형태소 단위로 분리해 명사만 반환 
pos(phrase): 주어진 텍스트를 형태소 단위로 분리하고, 각 형태소에 품사를 더해 반환 
"""





print('형태소', t.morphs(sentence))
print('명사', t.nouns(sentence))
print('품사', t.pos(sentence))

