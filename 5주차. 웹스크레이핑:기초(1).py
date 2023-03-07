#웹 스크레이핑 (Web Scraping): 웹에서 데이터를 추출하는 모든 행위
#웹 크롤링 (Web Crawling): Web scraping을 자동하여 웹 데이터를 추출하고 분석수행하는 프로그램 (crawler, bot, spider)이라고 함






"""
웹에 저장된 데이터나 정보를 컴퓨터가 자동으로 수집하도록 하는 기술
뉴스, 소셜미디어여론, 상품 리뷰 등 다량의 정보를 자동으로 추출해 데이터화
"""






"""
#HTTP 요청 방법 GET, POST, PUT, DELETE 방법 
1. Get: 서버에 있는 리소스에 대한 조회 (읽기 & 검색) 요청 
2. Post: 서버에 새로운 자원 생성을 요청 
3. Put: 서버에 있는 자원에 대한 수정 요청 
4. Delete: 서버에 있는 자원에 대한 삭제 요청 
"""






"""
속성             타입        설명 
r.status_code   정수형      요청에 대한 응답코드, 성공 시 200을 반환
r.url           문자열      요청한 최종URL
r.text          문자열      응답본문의 문자열 데이터 
r.content       바이너리     응답 본문의 바이너리(바이트)데이터
r.json          딕셔너리     응답 본문을 JSON형식으로 변환 데이터 
r.headers       딕셔너리     응답 헤더 
"""







#get을 통해 웹사이트 소스 가져오기
import requests
r = requests.get("https://www.google.com/")
r
r.text[0:100]#소스 일부만 출력확인
r.headers #응답헤더확인
html = requests.get("https://www.google.com/").text #한번에 작성하기







#데이터찾고 추출하기 (웹스크레이핑1-1 먼저 확인하기)
from bs4 import BeautifulSoup

# 테스트용 html 소스
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        <a href=https://www.pusan.ac.kr/kor/Main.do>부산대학교</a>\
        </span></div></body></html>"""
# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml')
soup #결과확인
print(soup.prettify())#정렬해서 확인
soup.find('a')#첫번째 태그명 검색 후 출력
soup.find_all('a')#태그명 a 가 들어간 요소 전부 출력 (리스트형태임)
soup.find('a').get_text()#첫번째 태그명 검색 후 출력
soup.find('a')['href']#a태그 요소에서 href 속성 값 출력
[x.get_text() for x in soup.find_all('a')]#get_text()는 리스트형태 데이터에 적용하기 힘들기 때문에 for문으로 추출








#예제2
from bs4 import BeautifulSoup
# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>

  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
  </body>
</html>
"""
soup2 = BeautifulSoup(html2, "lxml")
soup2.title
soup2.p
soup2.body
soup2.body.h1
soup2.p
soup2.find_all('p')
soup2.find('p')#첫번째 태그명 검색 후 출력
soup2.find_all('p')#태그명 a 가 들어간 요소 전부 출력 (리스트형태임)
soup2.find('p').get_text()#첫번째 태그명 검색 후 출력
soup2.find('p')['id']#a태그 요소에서 href 속성 값 출력
soup2.find('p', {"id":"book_title"})
soup2.find('p', {"id":"author"})
soup2.find_all('p', {'id':'book_title'})
soup2.find_all('p', {'id':'author'})
#html2에서 텍스트만 추출하기
soup2 = BeautifulSoup(html2, "lxml")
book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})
for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())







#soup.select를 통해 추출하기
soup2.select_one('body h1') # body 내의 h1 태그를 갖는 모든 요소 찾기
soup2.select_one('body p') #첫 번째 요소 값 불러오기
soup2.select('body p')
soup2.select('p')
soup2.select('p#book_title') # = id 기호임; 해당 태그에 해당하는 책 이름 불러오기
soup2.select('p#author') #해당 태그에 해당하는 저자 이름 불러오기







#웹스크레이핑 html코드를 활용해 연습하기
f = open('./5주차. 웹스크레이핑(1-2).html', encoding='utf-8')
html3 = f.read()
f.close()
soup3 = BeautifulSoup(html3, "lxml")
"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>국내/외 검색 사이트 모음집</title>
  </head>
  <body>
    <p id="title"><b>검색사이트 모음</b></p>
    <p id="contents">다양한 검색 사이트 모음</p>
    <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>
    <a href="https://www.google.com" class="search" id="google">구글</a> <br>
    <a href="http://www.daum.net" class="portal" id="daum">다음</a> <br>
    <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a> <br>
    <a href="https://www.pusan.ac.kr/kor/Main.do" class="institution" id="psu">부산대학교</a>
  </body>
</html>
"""






#웹스크레이핑
soup3.select('a')
soup3.select('a.portal')#a class portal
soup3.select('a.institution')#a class portal
soup3.select_one('a').get_text() #1개 출력
soup3.select_one('a').get_text() #soup.select는 리스트 형태이기 때문에 실행오류 발생함
[x.get_text() for x in soup3.select('a')]
#html코드에 접속한 후 태그 확인하기






#확인
soup3.select('html body a')
soup3.select('body a')
soup3.select('html a')
soup3.select('a') #모두가 같은 결과를 출력함; 최대한 간소화 할 필요가 있음







#contents추출
soup3.select('a#naver')
soup3.select('a#naver.portal')
a = soup3.select('a#psu') #부산대학교 이름만 추출하기
for i in a:
    print(i.string)








#웹사이트 주소에 매개변수 추가하기
import requests

where_value = 'nexearch'
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'
base_url = "https://search.naver.com/search.naver"
parameter = "?where={0}&sm={1}&fbm={2}&ie={3}&query={4}".format(where_value, sm_value, fbm_value, ie_value, query_value)
url_para = base_url + parameter
r = requests.get(url_para)
print(r.url)









#라이브러리 불러오기
"""
스크레이핑을 위한 패키지 설치 (터미널)
pip install requests 
pip install beautifulsoup4
pip list 
"""
import requests
r = requests.get('https://sneakernews.com/category/adidas/') # 웹에서 html 태그정 확인하기
html = r.text #html변수생성
print(html) #확인








# Requests.py
import requests
from bs4 import BeautifulSoup #beautifulsoup4
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.post-content > h4 > a')
for title in titles:
    print(title.text)







import requests






#get
re = requests.get('https://httpbin.org/get')
print(re.text)






#post
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)






#웹검색
resp = requests.get('https://www.youtube.com/')
# resp.raise_for_status()
if (resp.status_code == requests.codes.ok):
    html = resp.text
    print(html)







#request에서 한글깨지는 경우 발생함
resp = requests.get('http://naver.com')
resp.encoding #UTF-8로 한글이 깨지지 않고 출력
resp = requests.get('http://finance.naver.com')
resp.encoding #ECU-KR 가능
resp =  requests.get('https://shop.buyee.jp/?lang=en')
resp.encoding #ISO 코드는 한글이 깨짐








#유니코드인코딩
resp = requests.get('https://shop.buyee.jp/?lang=en')
resp.encoding='euc-kr'  # 한글 인코딩
html = resp.text
print(html)








"""
웹 스크레이핑 과정 요약 
1. 추출 대상 데이터 객체 정의 및 페이지 선정
2. 페이지 상 추출 대상 데이터 분석 (html)
3. 웹 스크레이핑 코드 작성 
4. 가져온 데이터 저장 (SQL, xls, csv, JSON 등) 
"""


