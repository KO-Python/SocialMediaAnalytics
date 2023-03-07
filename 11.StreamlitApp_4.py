import streamlit as st
import pandas as pd
import numpy as np

base_lat = 35.166668  # 기준 위치 (위도)
base_lon = 129.0666666  # 기준 위치 (경도)

rand1 = [0.38731831, 0.88186355, 0.73767047, 0.48262488, 0.40470396,
         0.44718457, 0.62209526, 0.00927177, 0.45061387, 0.29512467,
         0.03209323, 0.21555133, 0.18564942, 0.21124898, 0.56080097,
         0.07353603, 0.96114633, 0.43632126, 0.61204948, 0.56378569]

rand2 = [0.33344199, 0.60650414, 0.30760968, 0.15650897, 0.61547323,
         0.4844213, 0.5180108, 0.52112468, 0.38900425, 0.71651658,
         0.75229359, 0.31247536, 0.53251045, 0.37826329, 0.17648217,
         0.57750034, 0.38393327, 0.34383632, 0.31099857, 0.26455346]

pos_lat = base_lat + np.array(rand1) * 0.02
pos_lon = base_lon + np.array(rand2) * 0.02

# 위도(latitude)와 경도(longitude)를 지정한 DataFrame 데이터 생성
pos_data = {"lat": pos_lat, "lon": pos_lon}  # 위도와 경도 데이터를 이용해 딕셔너리 데이터 생성
df_for_map = pd.DataFrame(pos_data)  # DataFrame 데이터의 열 이름은 lat와 lon으로 지정됨

st.title("스트림릿에서 차트 그리기")
st.subheader("지도 좌표(위도, 경도)에 점 그리기: st.map(df) 이용")
st.map(df_for_map, zoom=12)  # zoom에 초기의 지도 크기를 지정

#streamlit run 11.StreamlitApp_4.py