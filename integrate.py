import streamlit as st

st.markdown(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=True, help='unsafe_allow_html=True인 경우')

st.markdown(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=False, help='unsafe_allow_html=False인 경우')

st.markdown('Streamlit은 **_매우_ 훌륭하다**.')
st.markdown("이 문장은 :red[빨강], 그리고 이문장은 **:blue[파랑]** 그리고 볼드체이다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 피타고라스 항등식이다. :pencil:")


st.title('이것은 제목입니다', anchor='https://docs.streamlit.io/library/api-reference/text/st.title' ,help='anchor 존재') 
st.title('이것은 제목입니다', anchor=None) 

st.title('이것은 제목입니다.')
st.title('_이탤릭체 제목_ :blue[파랑색] 그리고 선글라스 이모지 :sunglasses:')

st.header('이것은 헤더입니다', anchor='https://docs.streamlit.io/library/api-reference/text/st.header' ,help='anchor 존재') 
st.header('이것은 헤더입니다', anchor=None) 

st.header('이것은 헤더입니다.')
st.header('_이탤릭체 헤더_ :red[빨강색] 그리고 선글라스 이모지 :sunglasses:')

st.subheader('이것은 서브헤더입니다', anchor='https://docs.streamlit.io/library/api-reference/text/st.subheader' ,help='anchor 존재') 
st.subheader('이것은 서브헤더입니다', anchor=None) 

st.subheader('이것은 서브헤더입니다.')
st.subheader('_이탤릭체 서브헤더_ :red[빨강색] 그리고 선글라스 이모지 :sunglasses:')


st.caption(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=True, help='unsafe_allow_html=True인 경우')
st.caption(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=False, help='unsafe_allow_html=False인 경우')

st.caption('이것은 위의 내용을 설명하는 문자열입니다.')
st.caption('_이탤릭체 캡션_ :blue[파랑색] 그리고 이모티콘 :sunglasses:')

st.code('import streamlit as st', language="python", line_numbers=True)
st.code('import streamlit as st', language="python", line_numbers=False)

code = '''def text():
    print("안녕, Streamlit!")'''
st.code(code, language="python")

st.text('이것은 텍스트입니다', help='help')
st.text('이것은 텍스트입니다.')

st.latex(r'''
    a + ar + a r^2 + a r^3
    ''', help='3차 방정식')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')



st.title("이것은 title입니다.")
st.header("이것은 header입니다.")
st.subheader("이것은 subheader입니다.")

st.divider()

code = '''def text():
    print("안녕, Streamlit!")'''
st.code(code, language="python")

st.divider()  

st.latex(r'''a + ar + a r^2 + a r^3''', help="3차 방정식")

st.divider()  
