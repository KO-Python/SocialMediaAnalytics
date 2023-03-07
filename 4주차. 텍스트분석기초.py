moon = open('4주차.문재인대통령취임사.txt', encoding='EUC-KR').read()
yoon = open('4주차.윤석열대통령취임사.txt', encoding='utf-8-sig').read()







import re #불필요한문자제거
moon = re.sub('[^가-힣]', ' ', moon)
moon
import konlpy
hannanum = konlpy.tag.Hannanum()








#명사추출
nouns = hannanum.nouns(moon)
nouns









#데이터프레임으로변환
import pandas as pd
df_word = pd.DataFrame({'word': nouns})
df_word









#글자 수 추가
df_word['count'] = df_word['word'].str.len()
df_word








#두 글자 이상만 남기기
df_word = df_word.query('count >= 2')
df_word.sort_values('count')








#단어빈도구하기
df_word = df_word.groupby('word', as_index = False)\
    .agg(n = ('word', 'count'))\
    .sort_values('n', ascending= False)








#상위단어 20개 추출
top20 = df_word.head(20)
top20







#시각화
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family'    : 'AppleGothic',  # 한글 폰트 설정
                     'figure.dpi'     : '120',            # 해상도 설정
                     'figure.figsize' : [6.5, 6]})        # 가로 세로 크기 설정
sns.barplot(data = top20, y = 'word', x = 'n')








#워드클라우드
font = 'AppleGothic.ttf'
# 데이터 프레임을 딕셔너리로 변환
dic_word = df_word.set_index('word').to_dict()['n']







from wordcloud import WordCloud
wc = WordCloud(random_state = 1234,         # 난수 고정
               font_path = font,            # 폰트 설정
               width = 400,                 # 가로 크기
               height = 400,                # 세로 크기
               background_color = 'white')  # 배경색







# 워드 클라우드 만들기
img_wordcloud = wc.generate_from_frequencies(dic_word)
# 워드 클라우드 출력하기
plt.figure(figsize = (5, 5))  # 가로, 세로 크기 설정
plt.axis('off')                 # 테두리 선 없애기
plt.imshow(img_wordcloud)       # 워드 클라우드 출력




