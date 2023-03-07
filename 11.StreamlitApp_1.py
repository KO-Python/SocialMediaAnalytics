"""
스트림릿은 웹 앱을 제작하기 위한 툴
예를 들어, 다양한 데이터 결과를 웹 앱으로 만들 수 있음
pip install streamli (터미널)
터미널에서 streamlit hello 입력
"""

import streamlit as st

st.title("st.title(문자열): 제목")
st.header("st.header(문자열): 헤더")
st.subheader("st.subheader(문자열): 서브헤더")
st.text("st.text(문자열): 일반 텍스트입니다.")

st.text("st.code(code): 파이썬 코드 표시")

code = '''
def hello():
    print("Hello, Streamlit!")
'''
st.code(code)

st.markdown('스트림릿에서 **마크다운**을 사용할 수 있습니다.:sunglasses:')

#streamlit run 11.StreamlitApp_1.py









