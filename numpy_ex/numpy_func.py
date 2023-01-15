import sys
import streamlit as st
from io import StringIO
import contextlib


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def hide_part_of_page():
    st.set_page_config(layout="wide")
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
