



"""
웹스크레이핑 실습
"""
#웹 사이트 날씨 정보 가져오기
import requests #웹페이지 불러오기위한 패키지
from bs4 import BeautifulSoup #html 활용을 위한 뷰티풀솦
location = "부산광역시 금정구 장전동" #지역 설정
search_query = location + "날씨" #검색어 설정
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="#한글깨진부분 삭제
url = search_url + search_query #객체 설정
html_weather = requests.get(url).text #해당 객체 url불러오기
soup_weather = BeautifulSoup(html_weather, "lxml") #html url
print(url)#url 클릭 후 기온 html 코드 검사하기
temp = soup_weather.select_one('strong.txt_temp').get_text()#기온 추출하기
weather = soup_weather.select_one('span.txt_weather').get_text()#기온 추출하기
weather_details = soup_weather.select('dl.dl_weather dd') #습도, 풍속, 미세먼지 추출하기; soup_select
temp #확인
weather #확인
weather_details #확인
[wind_speed, humidity, pm10] = [x.get_text() for x in weather_details]#리스트데이터 객체 생성
print(f"풍속:{wind_speed}, 습도:{humidity}, 미세먼지:{pm10}")








#함수 적용 코드문 만들기(1)
import requests
from bs4 import BeautifulSoup
import time

def get_weather_daum(location):
    search_query = location + "날씨" #검색어 설정
    earch_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    soup_weather = BeautifulSoup(html_weather, "lxml")
    temp = soup_weather.select_one('strong.txt_temp').get_text()
    weather = soup_weather.select_one('span.txt_weather').get_text()
    weather_details = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in weather_details]#리스트데이터 객체 생성
    return (temp, weather, wind_speed, humidity, pm10)

location = "부산시 금정구 장전동" #지역 설정
get_weather_daum(location) #함수 호출
location = "서울시 서초구 양재동"
get_weather_daum(location)








#함수 적용 코드문 만들기 (2)
import requests
from bs4 import BeautifulSoup
import time

def get_weather_daum(location):
    search_query = location + "날씨" #검색어 설정
    earch_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    soup_weather = BeautifulSoup(html_weather, "lxml")
    temp = soup_weather.select_one('strong.txt_temp').get_text()
    weather = soup_weather.select_one('span.txt_weather').get_text()
    weather_details = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in weather_details]#리스트데이터 객체 생성
    print(f"-------[오늘의 날씨]-------")
    print(f"1.지역: {location}")
    print(f"2.기온: {temp}")
    print(f"3.날씨: {weather}")
    print(f"4.풍속: {temp}, 습도: {humidity}, 미시먼지: {pm10}")
    return (temp, weather, wind_speed, humidity, pm10)


location = "부산시 금정구 장전동" #지역 설정
get_weather_daum(location) #함수 호출
location = "서울시 서초구 양재동"
get_weather_daum(location)







#지상파시청률 스크레이핑
import bs4
from bs4 import BeautifulSoup
import urllib.request as req
url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&qvt=0&query=01%EC%9B%9410%EC%9D%BC%20%EC%A7%80%EC%83%81%ED%8C%8C%20%EC%8B%9C%EC%B2%AD%EB%A5%A0"
res=req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
news = soup.select("td > p > a")
for i in news:
    print(i.string)









#네이버증권top종록 스크레이핑
url="https://finance.naver.com/"
res=req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
news = soup.select("tr.up > th > a")
for i in news:
    print(i.string)








#네이버증권주요뉴스 스크레이핑
url="https://finance.naver.com/"
res=req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
news = soup.select("li > span > a")
for i in news:
    print(i.string)








"""
Q: 네이버증권 웹페이지에서 "환정고시환율"추출하기 
"""










"""
심화: 네이버 주식정보 가져오기 (finance.naver.com)
"""
import requests
from bs4 import BeautifulSoup
base_url = "https://finance.naver.com/item/main.naver"
stock_code = "066570" #LG전자 주식 종목 코드
url = base_url + "?code=" + stock_code #url + 검색어 코드
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml') #html parsing
print(url) #url 기반 출력
#주식가 html code = p.no_tody
soup.select_one("p.today")
stock_price = soup.select_one('p.no_today span.blind').get_text()
stock_price #확인
#stock_price 확인 후 함수화 작업
def get_stock_price(stock_code):
    base_url = "https://finance.naver.com/item/main.naver"
    url = base_url + "?code=" + stock_code  # url + 검색어 코드
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')  # html parsing
    soup.select_one("p.today")
    stock_price = soup.select_one('p.no_today span.blind').get_text()
    return stock_price
#삼성전자 주식 현재가
stock_code = "005930"
current_stock_price = get_stock_price(stock_code)
current_stock_price
#출력 명 수정 코드 작성
company_stocks = {"삼성전자":"005930", "현대자동차":"005380", "네이버":"035420"}
print("[현재 주식 가격(원)]")
for company, stock in company_stocks.items():
    current_stock_price = get_stock_price(stock_code)
    print(f"{company}:{current_stock_price}")







"""
심화II: 주식코드가져오기 
"""
import pandas as pd

# 한국 거래소(KRX)에서 전체 상장법인 목록 가져오기
base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
method = "download"
url = "{0}?method={1}".format(base_url, method)

df = pd.read_html(url, header=0)[0]

with pd.option_context('display.max_columns',4):
    pd.set_option("show_dimensions", False)
df.head() #위 5개 데이터 확인
df = df[['회사명', '종목코드']]
# ----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
# ----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt"  # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)
    df = pd.read_html(url, header=0)[0]
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드'] = df['종목코드'].apply(lambda x: f"{x:06d}")
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명', '종목코드']]
    return df
df_kospi = get_stock_info('kospi')
df_kospi #결과확인
df_kosdaq = get_stock_info('kosdaq')
df_kosdaq #결과확인
# --------------------------------------------------
# 회사 이름을 입력하면 종목 코드를 가져오는 함수
# --------------------------------------------------
def get_stock_code(company_name, maket_type=None):
    df = get_stock_info(maket_type)
    code = df[df['회사명'] == company_name]['종목코드'].values
    if (code.size != 0):
        code = code[0]
        return code
    else:
        print(f"[Error]입력한 [{company_name}]에 대한 종목 코드가 없습니다.")
get_stock_code('삼성전자','kospi')