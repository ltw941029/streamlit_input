import streamlit as st

# anchor가 있는 경우
st.header("이것은 헤더입니다.", anchor="https://docs.streamlit.io/library/api-reference/text/st.header" ,help="anchor 존재") 
# anchor가 None인 경우
st.header("이것은 헤더입니다.", anchor=None)
