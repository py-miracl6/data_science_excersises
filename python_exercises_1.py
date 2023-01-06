import streamlit as st
from streamlit_ace import st_ace


# .css-fblp2m {visibility: hidden;}
#     button {visibility: hidden;}
#     stSidebar {visibility: hidden;}
#     .css-1siy2j7 {visibility: hidden;}
#
#       section[data-testid="stSidebar"][aria-expanded="true"]{
#         width: 1%;
#       }
#       section[data-testid="stSidebar"][aria-expanded="false"]{
#         width: 1%;
#       }
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader("Блок Python 1. Задача 1")
st.markdown(
    "- Создайте переменную **x** и присвойте ей значение равное 6\n"
    "- Создайте переменную **y** и присвойте ей значение равное 2.5\n"
    "- Запишите в переменную **result** выражение, используя ранее объявленные переменные **x** и **y**,\n"
    "а также арифметические операторы так, чтобы по итогу значение **result** было равно **8.75**"
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
    x_check = 6
    y_check = 2.5
    result_check = x_check + 2 * 2 - y_check / 2

    try:
        exec(content, globals(), loc)

        try:
            x = loc["x"]
            y = loc["y"]
            result = loc["result"]
            if x != x_check:
                st.error(f"Проверьте значение в переменной x")
            elif y != y_check:
                st.error(f"Проверьте значение в переменной y")
            elif result != result_check:
                st.error(f"Проверьте значение в переменной result")
            else:
                st.success("Все верно! Ключ = 51")
        except Exception as ex:
            st.error(f"Проверьте названия переменных {ex}")
    except Exception as ex:
        st.error(ex)
