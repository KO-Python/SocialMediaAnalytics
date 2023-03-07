import urllib.request as req
from bs4 import BeautifulSoup
import os
import urllib.parse as par

keyword = input("키워드 입력 >> ")
# 특수한 문자로 변환
encoded = par.quote(keyword)

# 폴더 만들기
if not os.path.exists("./이미지크롤링"):
    os.mkdir("./이미지크롤링")

if not os.path.exists("./이미지크롤링/{}".format(keyword)):
    os.mkdir("./이미지크롤링/{}".format(keyword))

code = req.urlopen("https://images.search.yahoo.com/search/images;_ylt=Awr9F69vHetfQTsAaMiJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANWcDlDdWpFd0xqSmpuemgxWDlISEx3VHhNVEUwTGdBQUFBQlI0OEpkBGZyA3lmcC10BGZyMgNzYS1ncARncHJpZANNM1dGVDczM1RnU3lKc0FnNVA2TU5BBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMjcEcXVlcnkDJUVDJTk1JTg0JUVDJTlEJUI0JUVEJThGJUIwBHRfc3RtcAMxNjA5MjQ0Nzk5?p={}&fr=yfp-t&fr2=sb-top-images.search&ei=UTF-8&n=60&x=wrt".format(encoded))
soup = BeautifulSoup(code, "html.parser")
img = soup.select("li > a > img")
cnt = 1
for i in img:
    img_url = i.attrs['data-src']
    req.urlretrieve(img_url, "./이미지크롤링/{}/{}.png".format(keyword, cnt))
    print("이미지 크롤링 완료 {}".format(cnt))
    cnt += 1