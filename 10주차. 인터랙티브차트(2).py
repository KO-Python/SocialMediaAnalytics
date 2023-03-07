import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()









#대륙 간 지진 현황 그래프
import plotly.express as px
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="natural earth")
fig.show()








#Animated Figures
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px # for visualization
import plotly.offline as py
import plotly.graph_objs as go
from plotly.figure_factory import create_table # for creating nice table

df = px.data.gapminder()
df.info() #데이터확인
#GDP와 LifeExp(생애수명)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig.show()








#3D Plot
df = pd.read_excel('corona_dataset.xlsx', sheet_name = 'Sheet1')
df.info()
df = pd.DataFrame(df)
fig = px.scatter_3d(df, x='UserStatusesCount', y='UserFollowersCount', z='FavoriteCount',
                    color='Retweets')
fig.show()