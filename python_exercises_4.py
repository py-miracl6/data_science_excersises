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
st.subheader("HW1. Блок Python. Задача 4")
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
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert "value" in loc.keys(), "Проверьте название переменной value"
            assert (
                isinstance(loc["value"], dict) is True
            ), "Проверьте, что в переменной value словарь"
            assert len(list(loc["value"].keys())[:-1]) == len(
                value_check.keys()
            ), "Проверьте кол-во ключей в словаре value"
            assert "key3" in list(
                loc["value"].keys()
            ), "Проверьте, что вы добавили в словарь ключ 'key3'"
            st.success("Все верно! Ключ = 48")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
