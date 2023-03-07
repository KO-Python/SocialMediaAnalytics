import feedparser

query = '머신러닝'

# RSS 서비스 주소
rss_url = f'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko'
rss_news = feedparser.parse(rss_url) # RSS 형식의 데이터를 파싱

title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("['구글 뉴스' RSS 피드 제목]", title)
print("['구글 뉴스' RSS 피드 제공 일시]", updated)






from datetime import datetime, timedelta

# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경 하는 함수
def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])

    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str, '%d %b %Y %H:%M:%S')

    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)

    return date_time_KST  # 변경된 시간대의 날짜와 시각 반환





print("['구글 뉴스' RSS 피드 제공 일시]", get_local_datetime(updated))







import feedparser
import pandas as pd

df_gnews = pd.DataFrame(rss_news.entries) # 구글 뉴스 아이템을 판다스 DataFrame으로 변환

selected_columns = ['title', 'published', 'link'] # 관심있는 열만 선택
df_gnews2 = df_gnews[selected_columns].copy()     # 선택한 열만 다른 DataFrame으로 복사

# published 열의 작성 일시를 한국 시간대로 변경
df_gnews2['published'] = df_gnews2['published'].apply(get_local_datetime)

df_gnews2.columns = ['제목', '제공 일시', '링크'] # 열 이름 변경
df_gnews2.head(3)                                 # 앞의 일부만 출력







from IPython.display import HTML
df = df_gnews2.head(3) # DataFrame 데이터의 일부 열과 행을 선택
# df = df_gnews2       # DataFrame 데이터 전체를 선택

html_table = df.to_html(escape=False, render_links=True) # DataFrame 데이터를 HTML 코드로 변환
HTML(html_table)  # HTML 코드의 내용을 웹 브라우저처럼 보여줌

from datetime import datetime, timedelta

google_news_datetime_KST = get_local_datetime(updated)  # 한국 날짜와 시간으로 변경

df = df_gnews2.head()  # DataFrame 데이터 앞의 일부
# df = df_gnews2 # DataFrame 데이터 전체

# DataFrame 데이터를 HTML 코드로 변환 (justify='center' 옵션을 이용해 열 제목을 중간에 배치)
html_table = df.to_html(justify='center', escape=False, render_links=True)

# HTML 기본 구조를 갖는 HTML 코드
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = "./google_news.html"  # 생성할 HTML 파일 이름 지정
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)

print("생성한 파일:", file_name)


