
import streamlit as st
import pandas as pd
import json

# 딕셔너리 데이터
dict_data = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}








# 딕셔너리 데이터를 JSON 데이터로 변경
json_data = json.dumps(dict_data, indent=3, sort_keys=True, ensure_ascii=False)

st.title("스트림릿에서 데이터 표시 (2/2)")

st.subheader("st.json() 이용")
st.json(json_data)

st.subheader("st.metric() 이용")
st.metric("온도", "25 °C", delta="1.5 °C")








import streamlit as st
import pandas as pd

data1 = [ -2,   5,  -3,  -3,   9,  -4,  -7,  -9,   2,   3]
data2 = [  3,   4,  -4,  -2,  -3,  -2,   0,   7,  -6,   6]
data3 = [-10,   2,   8,   6,  -7,  -1,  -4,  -1,   4,   5]

dict_data = {"data1":data1, "data2":data2, "data3":data3}
df = pd.DataFrame(dict_data) # DataFrame

st.title("스트림릿에서 차트 그리기")

st.subheader("꺾은선형 차트: st.line_chart(df) 이용")
st.line_chart(df, height=170) # 높이 지정

st.subheader("영역형 차트: st.area_chart(df) 이용")
st.area_chart(df, height=170) # 높이 지정

st.subheader("세로 막대형 차트: st.bar_chart(df) 이용")
st.bar_chart(df, height=170) # 높이 지정

#streamlit run 11.StreamlitApp_3.py