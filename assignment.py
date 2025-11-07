import streamlit as st

st.title('Youtube Learning assignment for Practice.')
st.subheader('Choosing or Picking any one programming Language..')
st.text('Select any one Programming Language from the below dropdown.')
st.write('Seelct one Language')


Languages = st.selectbox('The Available Programming Languages are ', ['Python','Java','C','C#','C++','R','Ruby','JavaScript','php'])

st.write(f'You have choosen {Languages} from the drop-down and Happy Learning..')
st.success(f'Thanks for choosing a popular Programming Language {Languages}')