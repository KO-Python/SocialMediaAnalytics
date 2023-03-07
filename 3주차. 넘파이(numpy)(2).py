#1. 관심 있는 데이터 찾기
"""공공데이터포털 (www.data.go.kr)"""






#2. 데이터 살펴보며 질문하기
"""인구 데이터를 예로 들며
1. 전국에서 영유아들이 가장 많이 사는 지역은 어디일까
2. 보통 학군이 좋다고 알려진 지역에는 청소년들이 많이 살까
3. 광역시 데이터를 10년 단위로 살펴보면 청년 비율이 줄고 있다는 사실을 알 수 있을까
4. 서울에서 지난 5년간 인구가 가장 많이 증가한 구는 어디일까
5. 우리 동네의 인구 구조가 비슷한 동네는 어디일까"""






#3. 질문을 명확한 문제로 정의하기






#4. 알고리즘 설계하기
"전국에서 신도림동의 연령별 인구 구조와 가장 형태가 비슷한 지역은 어디일까"
"""
1. 데이터를 읽어온다.
2. 궁금한 지역의 이름을 입력 받는다.
3. 궁금한 지역의 인구 구조를 저장한다.
4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다.
"""

#5. 알고리즘을 코드로 표현하기








"1. 데이터를 읽어온다."
import csv
import numpy as np
import matplotlib.pyplot as plt

f = open('3주차.age.csv')
data = csv.reader(f)
next(data)
for row in data:
    print(row)








"2. 궁금한 지역의 이름을 입력 받는다."







"3. 궁금한 지역의 인구 구조를 저장한다."
f = open('3주차.age.csv')
data = csv.reader(f)
next(data)
name = input('궁금한 지역을 입력하세요: ')
home = [] #입력받은 지역의 데이터를 저장할 리스트 생성
for row in data:
    if name in row[1]: #입력받은 지역의 이름이 포함된 행 찾기
        for i in row[4:]: #4번(0세) 인덱스부터 슬라이싱
            home.append(int(i)) #입력받은 데이터를 home 리스트에 추가
print(home)








"numpy 사용하여 수정"
f = open('3주차.age.csv')
data = csv.reader(f)
next(data)
name = input('궁금한 지역을 입력하세요: ')
home = []
for row in data:
    if name in row[1]:
        home = np.array(row[4:], dtype=int) #dtype = int는 리스트를 numpy 배열로 저장할 때 데이터 타입을 정수로 변환하라.
print(home)

plt.style.use('ggplot') #책에 없어서 추가
plt.rc('font', family='AppleGothic')
plt.title('%s 지역의 인구 구조'%(name))
plt.plot(home)
plt.show()





"4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기"
"""
1. 전국의 모든 지역 중 한 곳(B)을 선택한다.
2. 궁금한 지역 A의 0세 인구 비율에서 B의 0세 인구 비율을 뺀다.
3. 2를 100세 이상 인구수에 해당하는 값까지 반복한 후 각각의 차이를 모두 더한다.
4. 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.
"""

