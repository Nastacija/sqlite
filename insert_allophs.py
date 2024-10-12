import sqlite3
from create_database import table_B_ids

to_insert = []
for line in table_B_ids:
        data = line.rstrip('\n').split(',')
        id = data[0]
        fl_id = data[1]
        alloph = data[2]
        start = data[3]
        end = data[4]
        word_id = data[5]
        ln = (id, f'{fl_id}', f'{alloph}', start, end, word_id)
        to_insert.append(ln)

try:
    con = sqlite3.connect('sqlite_python.db')
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO transcription
                             (id, file_id, alloph, start, end, word_id)
                             VALUES(?, ?, ?, ?, ?, ?);"""
    with con:
        con.executemany(sqlite_insert_query, to_insert)

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")