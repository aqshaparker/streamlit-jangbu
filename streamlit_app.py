import streamlit as st
st.header ("Hello World")
st.title ("Hello World")
 
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
