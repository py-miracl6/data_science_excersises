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

st.subheader("Блок Python 1. Задача 4")
st.markdown(
    "- Создайте переменную **value** и присвойте ей словарь с тремя различными типами ключей и их значений.\n"
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
    value_check = {1: [1, 3], "key": (1, 2, 4), 2: "строка"}

    try:
        exec(content, globals(), loc)
        try:
            value = loc["value"]
            if isinstance(value, dict) is not True:
                st.error(f"Проверьте, что в переменной value словарь")
            elif len(list(value.keys())[:-1]) != len(value_check.keys()):
                st.error(f"Проверьте кол-во ключей в словаре value")
            elif "key3" not in list(value.keys()):
                st.error(f"Проверьте, что вы добавили в словарь ключ 'key3'")
            else:
                st.success("Все верно! Ключ = 48")
        except Exception as ex:
            st.error(f"Проверьте названия переменных {ex}")
    except Exception as ex:
        st.error(ex)
