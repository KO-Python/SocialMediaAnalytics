import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from scipy import stats
import numpy as np

df = pd.read_excel('corona_dataset.xlsx', sheet_name = 'Sheet1')

df.rename(columns={'Content(Blank)':'트윗','AuthorName':'이용자','Retweets':'리트윗',
                            'UserFollowersCount':'팔로우수', 'UserStatusesCount':'포스트',
                            'FavoriteCount':'좋아요'},inplace=True) #여러 변수 명 변경
df = df[['트윗', '이용자', '리트윗', '좋아요', '팔로우수', '포스트']] #새로운 변수 명 데이터 생성
df.info()







#변수 정보 시각화
df['좋아요'].hist()
df['팔로우수'].hist()
df['포스트'].hist()






#상관관계
"""
0.7 - 1.0: 강한 양적 상관관계
0.3 - 0.7: 뚜렷한 양적 상관관계
0.1 - 0.3: 약한 양적 상관관계
-0.1 - 0.1: 상관관계 거의없음
-0.3 - 0.1: 약한 음적 상관관계
-0.7 - -0.3: 뚜렷한 음적 상관관계 
-1.0 - -0.7: 강한 음적 상관관계
"""
df.info()
df.corr() #df 변수 간 상관관계
np.corrcoef(df['좋아요'], df['팔로우수']) #넘파이 활용 상관관계







#상관관계 시각화
import seaborn as sns
#plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams["font.family"] = 'AppleGothic'#폰트 생성용 코드
sns.heatmap(df.corr(), vmin=-1, vmax=1,annot=True, cmap="rocket_r")#전체 상관관계 시각화
sns.scatterplot(x='좋아요', y='팔로우수', data=df) #두 변수 간 scatter plot
sns.lmplot(x='좋아요', y='포스트', data=df); #라인 그래프






#교차분석
#포스트 숫자를 범주화로 변수 변경
df['포스트'].describe()
df.loc[df['포스트'] > 12000, '포스트RE'] = '높음'
df.loc[df['포스트'] <= 19999, '포스트RE'] = '낮음'
df['포스트범주화변수'].value_counts()
df['좋아요'].describe()
df.loc[df['좋아요'] > 2800, '좋아요RE'] = '높음'
df.loc[df['좋아요'] <= 2799, '좋아요RE'] = '낮음'
df['좋아요RE'].value_counts()
pd.crosstab(df["포스트RE"], df["좋아요RE"])









