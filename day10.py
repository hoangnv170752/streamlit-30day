import streamlit as st

st.header('st.selectbox')

#Create the options
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.subheader('Kich ban anh sang')

if (option == 'Blue'):
    light_bulb = st.slider('DIM LED', 0 , 100, 40)
else:
    light_bulb = st.slider('DIM LED', 0 , 100, 100)
st.write("Chỉnh cường độ sáng", light_bulb, 'lux')