import streamlit as st
from streamlit_ace import st_ace
from typing import Union


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

st.subheader("Блок Python 2. Задача 1")
st.markdown(
    "- НАПИСАТЬ ТУТ Создайте переменную **value** и присвойте ей словарь с тремя различными типами ключей и их значений.\n"
    "- Добавьте значение в словарь типа int и назовите ключ **'key3'**"
)

loc = {}

content = st_ace(
    placeholder="Ваш код",
    language="python",
    theme="chrome",
    keybinding="vscode",
    show_gutter=True,
    min_lines=10,
    key="ace",
)


if content:
    st.subheader("Answer")

    try:
        exec(content, globals(), loc)
        try:
            assert loc["function"].__annotations__['value_1'] == Union[int, float], 'Проверьте type hints для параметра value_1'
            assert loc["function"].__annotations__['value_2'] == Union[int, float], 'Проверьте type hints для параметра value_2'
            assert loc["function"](5, 1.1) == 6.1, 'Проверьте, что внутри функции function() вы складываете value_1 и value_2'
            st.success("Все верно! Ключ = 99")
        except Exception as ex:
            st.error(f"{ex}")
    except Exception as ex:
        st.error(ex)

