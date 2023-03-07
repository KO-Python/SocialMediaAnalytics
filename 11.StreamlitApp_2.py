# 데이터 표시 예제1

import streamlit as st
import pandas as pd

# CSV 파일 경로
folder = './' # 폴더 경로를 지정
excel_file = folder + 'corona_dataset.xlsx' # 파일 경로를 지정

# 파일을 읽어와서 DataFrame 데이터 생성
df = pd.read_excel(excel_file)
df = df[['Tweet(Title)', 'FavoriteCount', 'UserFollowersCount', 'UserStatusesCount']]
df.info()

st.title("스트림릿에서 트위터 데이터 표시 (1/2)")

st.subheader("st.dataframe() 이용")
st.dataframe(df)

st.subheader("st.table() 이용")
st.table(df)
# streamlit run 11.StreamlitApp_2.py
