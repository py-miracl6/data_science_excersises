import streamlit as st
from streamlit_ace import st_ace
from typing import Union
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
st.subheader("HW2. Блок Python. Задача 1")
st.markdown(
    "- Создайте функцию и назовите ее **summation**. На вход она должна принимать два параметра **value_1** и **value_2** (может быть как тип int, так и float для каждого)\n"
    "- Функция должна возвращать результат суммы двух значений (return), которые поданы на вход функции\n"
    "- В функции должно быть предусмотрено исключение **TRY-EXCEPT** на случай, если будете подавать значения в нерелевантных форматах\n"
    "- Не забывайте про **DOCSTRING**, а также TYPE HINTS (подсказка Union[...,...])\n"
    "- Создайте переменную **result** и присвойте ей значения вызова функции **summation**, подав следующие значения: **value_1 = 21.9**, **value_2 = 99.5**"
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
    # st.subheader("Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert "summation" in loc.keys(), "Проверьте название функции summation()"
            assert (
                len(loc["summation"].__annotations__.keys()) == 3
            ), "Добавьте type hints для value_1, value_2 и возвращаемого значения"
            assert (
                loc["summation"].__annotations__["value_1"] == Union[int, float]
            ), "Проверьте type hints для value_1"
            assert (
                loc["summation"].__annotations__["value_2"] == Union[int, float]
            ), "Проверьте type hints для value_2"
            assert (
                loc["summation"].__annotations__["return"] == Union[int, float]
            ), "Проверьте type hints для возвращаемого значения"
            assert isinstance(
                loc["summation"].__doc__, str
            ), "Напишите docstring для функции"
            assert (
                loc["summation"](5, 1.1) == 6.1
            ), "Проверьте, что вы возращаете результат сложения value_1 и value_2"
            assert "result" in loc.keys(), "Проверьте переменную result"
            assert loc['result'] == 121.4, "Проверьте значение в переменной result"
            try:
                assert (
                    loc["summation"](3, "str") is None
                ), "Проблемы с try-except, в блоке except ничего не нужно возвращать"
                st.success("Все верно! Ключ = 99")
            except Exception as ex:
                st.error("Добавьте исключение try-except")
        except Exception as ex:
            st.error(f"{ex}")
    except Exception as ex:
        st.error(ex)
