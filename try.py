import streamlit as st
from streamlit_ace import st_ace
import sys
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
st.set_page_config(layout="wide")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader("HW1. Блок Python. Задача 0")
st.markdown(
    "- Создайте переменную **x** и присвойте ей значение равное 3\n"
    "- Создайте переменную **y** и присвойте ей значение равное 1.1\n"
    "- Создайте переменную **result** и запишите в нее сумму двух ранее созданных переменных **x** и **y**\n"
    "Например:"
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
    st.markdown("### Результат")
    x_check = 3
    y_check = 1.1
    result_check = x_check + y_check
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert 'x' in loc.keys(), "Проверьте название переменной x"
            assert loc["x"] == x_check, "Проверьте значение в переменной x"
            assert 'y' in loc.keys(), "Проверьте название переменной y"
            assert loc["y"] == y_check, "Проверьте значение в переменной y"
            assert 'result' in loc.keys(), "Проверьте название переменной result"
            assert loc["result"] == result_check, "Проверьте значение в переменной result"
            st.success("Все верно! Ключ = 101")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
