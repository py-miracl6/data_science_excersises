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

st.set_page_config(layout="wide")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.subheader("HW1. Блок Python. Задача 3")
st.markdown(
    "- Создайте переменную **value** и присвойте ей список, включающий три любых значения\n"
    "- Добавьте в конец списка строку **'это строка'**"
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
    value_check = [1, 2, 3]
    value_check_append = value_check.copy()
    value_check_append.append("это строка")

    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            value = loc["value"]
            if not isinstance(value, list):
                st.error(f"Проверьте, что в переменной value список")
            elif len(value[:-1]) != len(value_check):
                st.error(f"Проверьте кол-во значений в переменной value")
            elif value[-1] != value_check_append[-1]:
                st.error(
                    f"Проверьте, что вы добавили в список элемент со значением 'это строка'"
                )
            else:
                st.success("Все верно! Ключ = 68")
        except Exception as ex:
            st.error(f"Проверьте названия переменных {ex}")
    except Exception as ex:
        st.error(ex)
