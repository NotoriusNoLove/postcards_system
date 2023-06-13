from db import conn, cur
from datetime import datetime, timedelta


def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS people (
        name VARCHAR(255),
        group_id VARCHAR(50),
        birthday date);

        CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        group_id VARCHAR(50),
        text_birth VARCHAR(600),
        send_date date,
        submit boolean default true
        )
    """)
    conn.commit()


def insert_task(package: list):
    for item in package:
        text_birth = "TEST TEXT(replace to chatgpt_text)"
        send_date = datetime.now() + timedelta(days=1)
        query = """
        INSERT INTO tasks (name, group_id, text_birth, send_date) VALUES (%s, %s, %s, %s)
        """
        values = (item[0], item[1], text_birth, send_date)

        cur.execute(query, values)
    conn.commit()


def insert_users(path: str):
    df = open(path, "r", encoding="utf-8")
    cur.copy_from(df, "people", sep=';')
    conn.commit()


def get_users_birthday():
    """ returns users whose birthday is today - 1 day """

    cur.execute("""
    SELECT name, group_id
    FROM people
    WHERE TO_CHAR(birthday, 'MM-DD') = TO_CHAR(CURRENT_DATE - INTERVAL '1 day', 'MM-DD');
    """
                )
    result = cur.fetchall()
    return result


def test():
    cur.execute("""
    SELECT name, group_id
    FROM people
    WHERE TO_CHAR(birthday, 'MM-DD') = '03-01'
    """
                )
    result = cur.fetchall()
    return result
