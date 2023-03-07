import matplotlib as plt
from wordcloud import WordCloud
from konlpy.corpus import kolaw #한국어 문서에 대한 그래프와 워드클라우드





const_doc = kolaw.open('9주차.constitution.txt').read() #헌법 파일 분석






print(type(const_doc)) #가져온 데이터의 type을 확인
print(len(const_doc)) #데이터 글자수 확인
print(const_doc[:600]) #첫 600자 확인






from konlpy.tag import Okt #KoNLP 패키지에서 Okt 형태소 분석
t = Okt()
tokens_const = t.morphs(const_doc) #형태소 단위로 tokenize






print('#토큰의 수:', len(tokens_const))
print('#앞 100개의 토큰')
print(tokens_const[:100]) #단어에 불필요한 용어 파악 필요






tokens_const = t.nouns(const_doc) #형태소 단위로 tokenize 후 명사만 추출
print('#토큰의 수:', len(tokens_const))
print('#앞 100개의 토큰')
print(tokens_const[:100])#명사 추출






tokens_const = [token for token in tokens_const if len(token) > 1] #단어 글자 수 1보다 큰 단어만 추출
print('#토큰의 수:', len(tokens_const)) #토큰의 수 확인
print('#앞 100개의 토큰')
print(tokens_const[:100])






from matplotlib import font_manager, rc
import platform






#font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() #윈도우 경로 지정확
# 맥인 경우에는 아래와 같이 font_name을 지정
font_name = 'AppleGothic'
rc('font', family=font_name)







const_cnt = {} #단어 카운트
for word in tokens_const:
    const_cnt[word] = const_cnt.get(word, 0) + 1 #단어 하나씩 반복해 카운트 함







#함수생성
def word_graph(cnt, max_words=10): #단어 10번 이상
    sorted_w = sorted(cnt.items(), key=lambda kv: kv[1]) #단어 정렬
    print(sorted_w[-max_words:]) #단어 빈도수 역순으로 출력
    n, w = zip(*sorted_w[-max_words:]) #zip 함수 사용 역순 계산
    plt.barh(range(len(n)), w, tick_label=n) #단어 빈도 체크
    # plt.savefig('bar.png')  # 필요한 경우, 그래프를 이미지 파일 저장
    plt.show()







word_graph(const_cnt, max_words=20) #단어 20개만 출력






#font_path = 'c:/Windows/Fonts/malgun.ttf'
# 맥인 경우에는 아래와 같이 font_path를 지정
font_path = 'AppleGothic'#폰트지정
wordcloud = WordCloud(font_path = font_path).generate(const_doc) #폰트지정







plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()







wordcloud = WordCloud(
    font_path = font_path,
    max_font_size = 100,
    width = 800, #이미지 너비 지정
    height = 400, #이미지 높이 지정
    background_color='white', #이미지 배경색 지정
    max_words=50)







wordcloud.generate_from_frequencies(const_cnt) #원문이 아닌 형태소 분석 결과로부터 워드클라우드를 생성
wordcloud.to_file("const.png") #생성한 이미지를 파일로 저장
plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()



