import sqlite3 as sl

con = sl.connect('sqlite_python.db')

with con:
    data = con.execute("SELECT * FROM transcription")
    for row in data:
        print(row)