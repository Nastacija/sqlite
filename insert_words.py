import sqlite3
from create_database import table_Y_ids

to_insert = []
for line in table_Y_ids:
        data = line.rstrip('\n').split(',')
        id = data[0]
        fl_id = data[1]
        N_word = data[2]
        word = data[3]
        trscr = data[4]
        start = data[5]
        end = data[6]
        sint_id = data[7]
        ln = (id, N_word, f'{word}', f'{trscr}', start, end, sint_id, f'{fl_id}')
        to_insert.append(ln)

try:
    con = sqlite3.connect('sqlite_python.db')
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO words
                             (id, N_word, word, transcription, start, end, sint_id, file_id)
                             VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
    with con:
        con.executemany(sqlite_insert_query, to_insert)

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")