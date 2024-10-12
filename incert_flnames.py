import sqlite3
from create_database import table_fl

to_insert = []
for line in table_fl:
        data = line.rstrip('\n').split(',')
        id = data[0]
        flname = data[1]
        ln = (f'{id}', f'{flname}')
        to_insert.append(ln)

try:
    con = sqlite3.connect('sqlite_python.db')
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO filenames
                             (id, filename)
                             VALUES(?, ?);"""
    with con:
        con.executemany(sqlite_insert_query, to_insert)

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")