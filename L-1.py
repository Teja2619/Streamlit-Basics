import streamlit as st
st.title('Hello! Learning Streamlit...')
st.subheader('Brewed with streamlit')
st.text('Welcome to the First Interactive App')
st.write("Choose you own Choice")


a = st.selectbox('Your Favourite choice is ',[1,2,3,4,5])
st.write(f'You have selected {a}. Good One to choose.')

st.success("You Streamlit App for choosing a Number is Working as Expected.")
