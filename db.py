import sqlite3
import os


def init_db():
    database_exists = os.path.exists('./db/database.db')
    schema_path = './db/schema.sql'

    if not database_exists:
        with open(schema_path, 'r') as sql_file:
            sql_script = sql_file.read()
        conn = sqlite3.connect('./db/database.db')
        conn.executescript(sql_script)
        conn.execute(
            "INSERT INTO quizes (questions, answers) VALUES (?,?)", ("kolik je 2+2?", "4")
        )
        conn.commit()
        conn.close()


def get_data_from_db():
    conn = sqlite3.connect('./db/database.db')
    conn.row_factory = sqlite3.Row
    records = conn.execute("SELECT * FROM quizes").fetchall()
    conn.close()
    return records
