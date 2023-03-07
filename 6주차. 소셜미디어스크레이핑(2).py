"""
국내 대표적인 소셜 미디어인 디시인사이드에서 게시글 수집하기
"""

from bs4 import BeautifulSoup
import requests as req
import re
import pandas as pd
import urllib

search = input("검색어 입력: ")
uni_kor = urllib.parse.quote(search)
urls = []
titles = []
posts = []
gall_names = []
times = []
header = {"User-Agent":"Mozilla/5.0"}
#링크 10페이지
for i in range(1, 11):
    url = "https://search.dcinside.com/post/p/" + str(i) + "/sort/accuracy/q/" + str(uni_kor)
    urls.append(url)
    for i in urls:
        header = {"User-Agent":"Mozilla/5.0"}
        res = req.get(i, headers=header)
        soup = BeautifulSoup(res.text, "html.parser")

        # 파싱 (제목, 글, 갤러리이름, 날짜)
        title = soup.find_all('a', attrs={'class': 'tit_txt'})
        for i in title:
            titles.append(i.get_text())
        post = soup.find_all('p', attrs={'class': 'link_dsc_txt'})
        for i in post:
            posts.append(i.get_text())

        gall_name = soup.select('a.sub_txt')
        for i in gall_name:
            gall_names.append(i.get_text())

        time = soup.select('span.date_time')
        for i in time:
            times.append(i.get_text())

#본문 내용 노이즈 (갤러리이름, 날짜) 삭제 (홀수)
posts = posts[0::2]

# 데이터 프레임 만들기
df = pd.DataFrame({'date': times, 'title': titles, 'content': posts, 'gall_name': gall_names})
df.to_csv(f'{search}.csv')