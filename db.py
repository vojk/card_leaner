import sqlite3
import os


def init_db():
    database_exists = os.path.exists('./db/database.db')

    if not database_exists:
        conn = sqlite3.connect('./db/database.db')
        conn.executescript(
            "CREATE TABLE quizes (id INTEGER PRIMARY KEY AUTOINCREMENT, sada TEXT NOT NULL, questions TEXT NOT NULL, answers TEXT NOT NULL)"
        )
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
