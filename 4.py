import streamlit as st
#anchor가 있는 경우
st.subheader("이것은 서브헤더입니다.", anchor="https://docs.streamlit.io/library/api-reference/text/st.subheader" ,help="anchor 존재") 
# anchor가 None 경우
st.subheader("이것은 서브헤더입니다.", anchor=None)
