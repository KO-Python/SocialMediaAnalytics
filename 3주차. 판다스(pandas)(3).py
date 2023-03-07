import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

df = pd.read_csv("3주차. PNU_data.csv", encoding="utf-8-sig")
df = df[['연번', '년도', '프로그램', '파견학기', '소속대학(원)','파견국', '파견자매대학']] #새로운 변수 명 데이터 생성
df.info()


#년도 변수 빈도 그래프 생성
df['년도'].value_counts()
year = [2020, 2021, 2022]
frequency = [62, 109, 245]


plt.bar(year, frequency)
plt.rcParams["font.family"] = 'AppleGothic'
plt.xlabel('년도')
plt.ylabel('빈도')
plt.title('연도 별 파견 현황')
plt.show()


#x축 조정
fig, ax = plt.subplots()
ax.bar(year, frequency)
ax.set_xticks(year)
ax.set_xticklabels(["2020", "2021", "2022"])
plt.rcParams["font.family"] = 'AppleGothic'
plt.xlabel('년도')
plt.ylabel('빈도')
plt.title('연도 별 파견 현황')
plt.show()


#색깔 변경
fig, ax = plt.subplots()
ax.bar(year, frequency, color='black')
ax.set_xticks(year)
ax.set_xticklabels(["2020", "2021", "2022"])
plt.rcParams["font.family"] = 'AppleGothic'
plt.xlabel('년도')
plt.ylabel('빈도')
plt.title('연도 별 파견 현황')
plt.show()


#프로그램 변수 분석
df['프로그램'].value_counts()
programs = ['교환', '교비/글로벌', '교환/SAM', '교환/단위기관', '복수학위/캠퍼스아시아사업',
            '교환(온라인)', '복수학위', '교비/SAM', '자비', '교비', '교환/캠퍼스아시아사업', '교환/단위기관(온라인)']
frequency = [317, 25, 15, 15, 15, 9, 8, 5, 4, 1, 1, 1]


plt.bar(programs, frequency)
plt.rcParams["font.family"] = 'AppleGothic'
plt.xlabel('프로그램')
plt.ylabel('빈도')
plt.title('프로그램 별 파견 현황')
plt.xticks(rotation=90)
plt.show()


#x와 y축 변경
data = [317, 25, 15, 15, 15, 9, 8, 5, 4, 1, 1, 1]
labels = ['교환', '교비/글로벌', '교환/SAM', '교환/단위기관', '복수학위/캠퍼스아시아사업', '교환(온라인)', '복수학위', '교비/SAM', '자비', '교비', '교환/캠퍼스아시아사업', '교환/단위기관(온라인)']

fig, ax = plt.subplots()
ax.barh(labels, data)
plt.xlabel('빈도')
plt.ylabel('카테고리')
plt.title('카테고리 별 빈도')
plt.show()


#빈도 순으로 정렬한 후 그래프
data = {'Program': ['교환', '교비/글로벌', '교환/SAM', '교환/단위기관', '복수학위/캠퍼스아시아사업', '교환(온라인)', '복수학위', '교비/SAM', '자비', '교비', '교환/캠퍼스아시아사업', '교환/단위기관(온라인)'],
         'Frequency': [317, 25, 15, 15, 15, 9, 8, 5, 4, 1, 1, 1]}
data = pd.DataFrame(data)
data = data.sort_values('Frequency', ascending=True)
plt.barh(data['Program'], data['Frequency'])
plt.rcParams["font.family"] = 'AppleGothic'
plt.xlabel('빈도')
plt.ylabel('프로그램')
plt.title('프로그램 현황')
plt.show()


#파이차트
df['파견국'].value_counts().plot(kind='pie', autopct='%.1f%%', fontsize=5)
plt.axis('equal')
plt.show()


#교차분석
crosstab = pd.crosstab(index=df['프로그램'], columns=df['파견국'])
crosstab
crosstab.to_csv('cross_tabulation.csv', index=True, header=True, encoding = 'utf-8-sig')


#교차분석그래프
crosstab.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Program')
plt.ylabel('Country')
plt.title('International Program')
plt.show()


#교차분석 그래프 변경
crosstab = pd.crosstab(index=df['프로그램'], columns=df['파견국'])
crosstab.plot(kind='barh', stacked=True, figsize=(10, 6))
plt.ylabel('Program')
plt.xlabel('Country')
plt.title('International Program')
plt.show()



#파견자매대학 빈도 찾기
freq = df['파견자매대학'].value_counts()
freq
if '이위베스퀼레대학' in freq.index:
  print("The frequency of '이위베스퀼레대학' is:", freq['이위베스퀼레대학'])
else:
  print("'이위베스퀼레대학' is not present in the column '파견자매대학'.")


#파견자매대학시각화
import folium
from geopy.geocoders import Nominatim

data = {'University': ['Jyväskylä', 'Kyushu University', 'University of Montreal', 'Södertörn University'],
        'Frequency': [16, 15, 11, 9]}
df = pd.DataFrame(data)


#위도&경도 생성
university_coordinates = {}


# Geopy를 활용한 지역 위치 찾기
geolocator = Nominatim(user_agent="geoapiExercises")
for university in df['University']:
    location = geolocator.geocode(university)
    university_coordinates[university] = [location.latitude, location.longitude]


# 지도시각화
m = folium.Map(location=[20, 0], zoom_start=2)


# 좌표 찍기
for university, coordinates in university_coordinates.items():
    folium.Marker(coordinates, popup=university).add_to(m)


# 시각화 확인
m.save('3주차.map.html')

"""지도에서 화살표를 그려보기"""
# 부산대학교 발 각 학교
pusan_location = geolocator.geocode("Pusan National University")
pusan_latitude = pusan_location.latitude
pusan_longitude = pusan_location.longitude

for university, coordinates in university_coordinates.items():
    folium.PolyLine([[pusan_latitude, pusan_longitude], coordinates], color="red", weight=2.5, opacity=1).add_to(m)

# 시각화 확인
m.save('3주차.map_from_PNU.html')
