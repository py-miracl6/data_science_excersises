import streamlit as st
from streamlit_ace import st_ace


hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .css-fblp2m {visibility: hidden;}
    button {visibility: hidden;}
    stSidebar {visibility: hidden;}
    .css-1siy2j7 {visibility: hidden;}
    
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 1%;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 1%;
      }
    </style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader("Welcome to Python")
