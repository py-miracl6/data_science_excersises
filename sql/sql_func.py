import streamlit as st
import pandas as pd
from sqlite3 import connect


def show_tables(url_db: str = "data/EmployeeSQL.db"):
    col1, col2, col3, col4 = st.columns(4)
    conn = connect(url_db)

    with col1:
        df = pd.read_sql("SELECT * FROM employees limit 4", conn)
        st.write("Table - **employees**")
        st.dataframe(df)

    with col2:
        df = pd.read_sql("SELECT * FROM dept_emp limit 4", conn)
        st.write("Table - **dept_emp**")
        st.dataframe(df)

    with col3:
        df = pd.read_sql("SELECT * FROM dept_manager limit 4", conn)
        st.write("Table - **dept_manager**")
        st.dataframe(df)

    with col4:
        df = pd.read_sql("SELECT * FROM salaries limit 4", conn)
        st.write("Table - **salaries**")
        st.dataframe(df)


def hide_part_of_page():
    st.set_page_config(layout="wide")
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        stActionButton {visibility: hidden;}
        </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def check_update_db(content):
    assert (
        "create" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "alter" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "delete" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "update" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
