from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_data_from_youtube(word, scroll=False):
    driver = Chrome()

    base_url = "https://www.youtube.com"
    search_word = '/results?search_query=' + word
    search_option = "&sp=CAMSAhAB"  # 조회수로 정렬

    url = base_url + search_word + search_option  # 접속하고자 하는 웹 사이트
    driver.get(url)  # URL에 접속
    time.sleep(3)  # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림

    if (scroll == True):
        # 수직(Y축 방향)으로 스크롤 동작하기
        y = 0  # Y축 방향으로 스크롤 이동할 거리 초기화
        y_step = 1000
        for k in range(1, 5):  # 반복 횟수 지정
            y = y + y_step  # 반복할 때마다 Y축 방향으로 더해지는 거리를 지정
            script = "window.scrollTo({0},{1})".format(0, y)
            driver.execute_script(script)  # Y축 방향으로 스크롤
            time.sleep(3)  # 결과를 받아올 때까지 잠시 기다림

    html = driver.page_source  # 접속 후에 해당 page의 HTML 코드를 가져옴
    # driver.quit() # 웹 브라우저를 종료함

    soup = BeautifulSoup(html, 'lxml')

    # 동영상 제목과 URL 추출하기
    title_hrefs = soup.select('a#video-title')

    titles = []
    urls = []
    for title_href in title_hrefs:
        title = title_href['title']  # 태그 안에서 title 속성의 값을 가져오기
        url = base_url + title_href['href']  # href 속성의 값 가져와 기본 url과 합치기
        titles.append(title)
        urls.append(url)

    # 조회수와 업로드 시기 추출하기
    view_uploads = soup.select('span.style-scope.ytd-video-meta-block')

    view_numbers = view_uploads[0::2]  # 인덱스가 짝수인 요소 선택
    upload_times = view_uploads[1::2]  # 인덱스가 홀수인 요소 선택

    views = []
    uploads = []
    for view_number, upload_time in zip(view_numbers, upload_times):
        view = view_number.get_text().split(" ")[-1]  # 조회수 추출
        upload = upload_time.get_text()  # 업로드 시기 추출
        views.append(view)
        uploads.append(upload)

    # 추출된 정보를 모으기
    search_results = []
    for title, url, view, upload in zip(titles, urls, views, uploads):
        search_result = [title, url, view, upload]
        search_results.append(search_result)

    # 추출 결과를 판다스 DataFrame 데이터 형식으로 변환
    df = pd.DataFrame(search_results, columns=["제목", "링크", "조회수", "업로드"])

    return df


df = get_data_from_youtube('방탄소년단', True)
df.tail() # 전체 중 끝 부분만 확인
# df # 전체를 다 출력하려면 df.tail() 대신 df를 이용