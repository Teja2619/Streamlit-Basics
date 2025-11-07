import streamlit as st

st.title('Juice Maker Application.')

if st.button('Prepare Juice'):
    st.success('Your Juice is Preparing')

add_Sugar = st.checkbox('Add more Sugar.')

if add_Sugar:
    st.write('Extra Sugar is Added.')

Juices_types = st.radio('Choose your Favourite Juice:', ['Apple', 'Orange','Pomegranate','Musk-Melon','Papaya'])
st.write(f'You Choose {Juices_types} Juice.')

extras = st.selectbox('Choose any Extras if Needed:' ,['ice','moderate cool','Plastic container', 'Glass Container'])

Sugar_levels = st.slider('Sugar-Level(in grams):', 5,10,7 )
st.write(f'Sugar-Level You have choose {Sugar_levels} grams')

glasses = st.number_input('How many glasses Juices you want? ', min_value = 1, max_value = 10, step = 1)
st.write(f'You have asked for {glasses} of Juice')\

name = st.text_input('Enter your Name: ')
if name:
    st.write(f'Welcome **{name}** to our Juice Center and your Juice will be ready in 5 minutes, Please have a seat and we Will inform Once your Order is Ready')

dob = st.date_input('Select your date of birth ')

st.write(f'Your Date of Birth is {dob}')














