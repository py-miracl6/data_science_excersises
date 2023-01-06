import streamlit as st
from streamlit_ace import st_ace

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.subheader("HW1. Блок Python. Задача 2")
st.markdown(
    "- Создайте переменную **value** и присвойте ей список со значениями элементов с 1-го по 9-ый включительно \n"
    "- Создайте переменную **value_1** и присвойте ей элементы списка **value** с 1-го по 4-ый **индексы**\n"
    "- Создайте переменную **value_2** и присвойте ей последний элемент списка **value**\n"
    "- Создайте переменную **value_3** и присвойте ей два последних элемента списка **value**\n"
    "- Создайте переменную **value_4** и присвойте перевернутый список **value**"
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
    value_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value_1_check = value_check[1:4]
    value_2_check = value_check[-1]
    value_3_check = value_check[-2:]
    value_4_check = value_check[::]

    try:
        exec(content, globals(), loc)
        try:
            value, value_1, value_2, value_3, value_4 = (
                loc["value"],
                loc["value_1"],
                loc["value_2"],
                loc["value_3"],
                loc["value_4"],
            )
            if isinstance(value, list) != True:
                st.error(f"Проверьте, что в переменной value список")
            elif value != value_check:
                st.error(f"Проверьте значение в переменной value")
            elif value_1 != value_1_check:
                st.error(f"Проверьте значение в переменной value_1")
            elif value_2 != value_2_check:
                st.error(f"Проверьте значение в переменной value_2")
            elif value_3 != value_3_check:
                st.error(f"Проверьте значение в переменной value_3")
            elif value_4 != value_4_check:
                st.error(f"Проверьте значение в переменной value_4")
            else:
                st.success("Все верно! Ключ = 15")
        except Exception as ex:
            st.error(f"Проверьте названия переменных {ex}")
    except Exception as ex:
        st.error(ex)
