import sqlite3
from create_database import table_R_ids

to_insert = []
for line in table_R_ids:
        data = line.rstrip('\n').split(',')
        id = data[0]
        fl_id = data[1]
        N_sint = data[2]
        tp = data[3]
        content = data[4]
        start = data[5]
        end = data[6]
        ln = (id, N_sint, f'{tp}', f'{content}', start, end, f'{fl_id}')
        to_insert.append(ln)

try:
    con = sqlite3.connect('sqlite_python.db')
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO intonation_units
                             (id, N_sint, type, content, start, end, file_id)
                             VALUES(?, ?, ?, ?, ?, ?, ?);"""
    with con:
        con.executemany(sqlite_insert_query, to_insert)

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")