import plotly.express as py
import pandas as pd
import numpy as np
import plotly.express as px






fig = py.bar(x=["a", "b", "c"], y=[1, 3, 2]) #데이터 생성하기
fig.show()







#X&Y 점선 그래프
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()








#트위터 기반 인터랙티브플랏
df = pd.read_excel('corona_dataset.xlsx', sheet_name = 'Sheet1')
df.info()
df = pd.DataFrame(df)
fig1 = px.scatter(df, x = "UserStatusesCount", y="UserFollowersCount")
fig1.show()

fig2 = px.scatter(df, x = "UserFollowersCount", y="FavoriteCount", color="FavoriteCount")
fig2.show()

import statsmodels.api as sm
fig3 = px.scatter(df, x = "UserFollowersCount", y="FavoriteCount", trendline="ols")
fig3.show()










import pandas as pd
mpg = pd.read_csv('10주차.mpg.csv')

# 산점도 만들기
import plotly.express as px #https://plotly.com/python/
fig = px.scatter(data_frame = mpg, x = 'cty', y = 'hwy', color = 'drv')
fig.show()




mpg

# 자동차 종류별 빈도 구하기
df = mpg.groupby('manufacturer', as_index = False)\
        .agg(n = ('manufacturer', 'count'))
df








# 막대 그래프 만들기
fig = px.bar(data_frame = df, x = 'manufacturer', y = 'n', color = 'manufacturer')
fig.show()







# 상자 그림 만들기
fig = px.box(data_frame = mpg, x = 'drv', y = 'hwy', color = 'drv')
fig.show()








#html로 저장하기
#fig.write_html('scatter_plot.html')








