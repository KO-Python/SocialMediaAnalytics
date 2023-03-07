from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup







#경고(주의) 메시지 없애기
import warnings
warnings.filterwarnings('ignore')
driver = webdriver.Chrome("chromedriver") #크롬드라이버 설치 필요
driver.get("https://www.youtube.com/watch?v=twieEBEf86s") #분석대상 유튜브링크
driver.implicitly_wait(3) #시간 지연
time.sleep(1.5)
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)








#마지막 댓글까지 크롤링
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(1.5)
try:
    driver.find_element(By.CSS_SELECTOR, "#dismiss-button > a").click()
except:
    pass
buttons = driver.find_elements(By.CSS_SELECTOR, "#more-replies > a")
time.sleep(1.5)
for button in buttons:
    button.send_keys(Keys.ENTER)
    time.sleep(1.5)
    button.click()
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
id_list = soup.select("div#header-author > h3 > #author-text > span")
comment_list = soup.select("yt-formatted-string#content-text")
id_final = []
comment_final = []
for i in range(len(comment_list)):
    temp_id = id_list[i].text
    temp_id = temp_id.replace('\n', '')
    temp_id = temp_id.replace('\t', '')
    temp_id = temp_id.replace('    ', '')
    id_final.append(temp_id)
    temp_comment = comment_list[i].text
    temp_comment = temp_comment.replace('\n', '')
    temp_comment = temp_comment.replace('\t', '')
    temp_comment = temp_comment.replace('    ', '')
    comment_final.append(temp_comment)








#유튜브댓글 저장
pd_data = {"아이디" : id_final , "댓글 내용" : comment_final}
youtube_pd = pd.DataFrame(pd_data)
youtube_pd.to_excel('youtube.xlsx')









