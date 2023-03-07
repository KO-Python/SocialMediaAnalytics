#pandas: 데이터 정리오 분석

"""
1. 데이터분석을 위해 널리 사용되는 파이선라이브러리;엑셀과 상당히 유사함
2. DataFrame: 행과 열로 구성된 데이터세트
3. Series: DataFrame에서 각 변수(열) 1개에 해당하는 데이터
4. index: 데이터에서 가장 왼쪽에 위치하고 데이터 확인의 기준이 됨
"""

import pandas as pd  # pandas를 불러와 pd라는 축약어로 변경
import numpy as np # numpy는 숫자 배열과 연산에 사용하는 라이브러리. 데이터 분석에는 기본적으로 사용됨.







"""
파일 불러오기: df = pd.read_csv("XXX.csv", encoding="CP949")
파일 저장하기: df.to_csv("UUU.csv") 
"""






#DataFrame, Series, Index 생성
new_data=pd.DataFrame({"var1":[1,2,3,4,5], "var2":[90,80,90,85,95]})
new_series=pd.Series([201, 332, 564, 789, 973])
new_data.index=[1,2,3,4,5]
new_data







"""
import pandas as pd
import 

#Excel 파일 불러오기 
df = pd.read_excel(excel_file.xlsx, sheet_name = ‘Sheet1’)
df.info()
"""
import openpyxl
df = pd.read_excel('corona_dataset.xlsx', sheet_name = 'Sheet1')







"""
df.head()
df.tail()
df.info()
df.describe()
df[“변수명”].value_counts()
df[“변수명”].describe()
"""
df.head() # 데이터의 첫 5행을 보여줌. 첫 10행까지 보고 싶으면, 괄호 안에 10을 넣어주면 됨.
df.tail() # 데이터의 마지막 5행을 보여줌.
df.shape # 데이터의 모양을 행과 열 갯수로 보여줌.
df.columns # 데이터의 변수에 해당하는 열 이름을 보여줌
df.info() # 데이터의 변수, 행 갯수, 결측치 여부, 데이터 유형 등을 보여줌.
df.describe() # 데이터의 변수별 갯수, 평균, 표준편차, 사분위 등 기초 통계를 보여줌.
df.drop(['Published', 'Geo', 'AuthorURL'], axis=1, inplace=True)#특정변수를 데이터프레임에서 삭제
df.info()
df_tweet = df['Content(Blank)']#오리지널데이터에서 특정 변수만 추출 후 다른 변수에 추가
df_tweet.index
df_tweet.values








"""
Variable types 
Unit of analysis 
Missing values 
Duplicated record (i.e., 텍스트 마이닝)
"""
df['Content(Blank)'] #df에서 Content(Blank)변수만 선택
df[['Content(Blank)', 'UserFollowersCount']] #두 개 변수 선택
df.iloc[0,:] # df내 첫번째 행 선택
df.iloc[0,0] # mydata내 첫번째 행과 첫번째 열 선택







#데이터 전처리: 결측치 처리, 표기 변경 등
pd.isnull(df) #결측치 확인
pd.isnull(df['Content(Blank)'])
#df.dropna()#df에서 결측치가 있는 모든 행 제거
#df.fillna('x') #결측치를 x로 대체







#변수 이름 변환
#df = df.rename(columns={'FavoriteCount':'좋아요'}) #변수 1개 이름 변경
df.rename(columns={'Content(Blank)':'트윗','AuthorName':'이용자','Retweets':'리트윗',
                            'UserFollowersCount':'팔로우수', 'UserStatusesCount':'포스트',
                            'FavoriteCount':'좋아요'},inplace=True) #여러 변수 명 변경
df.info()#확인
df = df[['트윗', '이용자', '리트윗', '좋아요', '팔로우수', '포스트']] #새로운 변수 명 데이터 생성
df.info()#확인






#평균확인
df['좋아요'].mean()
df['팔로우수'].mean()
df['포스트'].mean()






#특정 조건으로 변수 정렬
df.sort_values("좋아요", ascending=False)
df.sort_values(["좋아요", "팔로우수"], ascending=[True, False]) #df에서 좋아요 기준 오름차순, 팔로우수 내림차순 정렬
df.describe()
df['좋아요'].mean()
df['좋아요'].median()
df['좋아요'].max()
df['좋아요'].min()
df['좋아요'].std()







# 데이터 사례 만들기
data1=pd.DataFrame({"변수1":[1,2,3], "변수2":[5,3,1]})
data2=pd.DataFrame({"변수1":[21,43], "변수2":[54,12]})
data3=pd.DataFrame({"변수3":[224,453,648]})
data4=pd.DataFrame({"변수1":[1,2,5], "변수3":[224,453, 648]})
# 합치기
pd.concat([data1, data2], axis=0) # data1의 아래쪽에 data2를 추가. 행(axis=0)이 늘어나는 합치기. 두 데이터는 변수가 같아야 함.
pd.concat([data1, data3], axis=1) # data1의 오른쪽에 data3를 추가. 열(axis=1)이 늘어나는 합치기. 두 데이터는 사례 수가 같아야 함.
pd.merge(data1, data4, on="변수1",how="inner")  # on에는 합치기 위한 기준 변수 입력.
# how에는 3가지 옵션 가능. inner는 두 데이터 공통 부분만 합치기. outer는 두 데이터 모두 살리면서 합치기.
# left는 왼쪽 데이터만 살리면서 합치기. right는 오른쪽 데이터만 살리면서 합치기.
data1.append(data2) # data1의 아래쪽에 data를 추가. 행이 늘어나는 합치기. 두 데이터는 변수가 같아야 함.
