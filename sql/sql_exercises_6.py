import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from sql_func import show_tables, hide_part_of_page, check_update_db


hide_part_of_page()
st.subheader("HW3. Блок SQL. Задача 6")
st.markdown(
    "- Найдите **вторую по счету максимальную зарплату среди менеджеров** при помощи **LIMIT**\n"
    "- Поле с максимальной зарплатой назовите **max_salary**\n"
    "- Выведите следующие поля: **id сотрудника - emp_no** и **размер MAX зарплаты - max_salary**\n"
    "- Не забывайте использовать таблицу dept_manager\n"
    "- Оконные функции использовать в этом задании не нужно!\n"
    "\n**Примечание**: вам уже даны таблицы, их импортировать не нужно, также можно выводить\n"
    "таблицу только до 80 строк при тестировании скрипта"
)
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
    test_sql = """select d.emp_no, s.salary as max_salary\n
                    from dept_manager d\n
                    inner join salaries s on d.emp_no = s.emp_no\n
                    order by salary desc\n
                    limit 1, 1"""

    try:
        check_update_db(content=content)
        df = pd.read_sql(content, conn)[:80]
        st.dataframe(df)
        df_check = pd.read_sql(test_sql, conn)

        assert (
            "over" not in content.lower()
        ), "Проверьте, что вы не используете в запросе оконные функции"
        assert (
            "max_salary" in content.lower()
        ), "Проверьте, что название поля с MAX зарплатой - max_salary"
        assert "limit" in content.lower(), "Проверьте, что вы используете LIMIT"
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте, что по итогу у вас получились те же поля (колонки), что в задании"
        assert list(df.columns) == list(
            df_check.columns
        ), "Проверьте последовательность названия полей как в задании"
        assert (
            "dept_manager" in content.lower()
        ), "Проверьте, что вы используете таблицу dept_manager для поиска максимальной зарплаты"
        assert (
            ("inner join" in content.lower())
            and ("from salaries" in content.lower())
            or ("from dept_manager" in content.lower())
        ), "Проверьте, что вы находите зарплату только среди менеджеров. Подсказка: проблема в типе JOIN"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert (
            df["max_salary"][0] == 71612
        ), "Проверьте все типы JOIN в запросе, а также какие таблицы и как их использовали для соединения, так как значение max_salary сейчас некорректное"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 453")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан неккоретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
