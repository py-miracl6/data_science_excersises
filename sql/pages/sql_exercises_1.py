import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from sql_func import show_tables, hide_part_of_page, check_update_db


hide_part_of_page()

st.subheader("HW3. Блок SQL. Задача 1")
st.markdown(
    "- Выведите первые 10 строк из таблицы **dept_emp**\n"
    "\n**Примечание**: вам уже даны таблицы, их импортировать не нужно, также можно выводить\n"
    "таблицу только до 80 строк при тестировании скрипта"
)
st.markdown("Пример скрипта:")
st.code("SELECT * FROM MY_TABLE LIMIT 5", language="sql")
show_tables()

loc = {}
content = st_ace(
    placeholder="Ваш скрипт",
    language="sqlserver",
    theme="xcode",
    keybinding="vscode",
    show_gutter=True,
    min_lines=10,
    key="ace",
)

if content:
    conn = connect("data/EmployeeSQL.db")
    st.markdown("### Результат")
    test_sql = """select * from dept_emp LIMIT 10"""

    try:
        check_update_db(content=content)
        df = pd.read_sql(content, conn)[:80]
        st.dataframe(df)
        df_check = pd.read_sql(test_sql, conn)
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте название таблицы"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 131")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан неккоретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )