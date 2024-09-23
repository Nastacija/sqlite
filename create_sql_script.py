import sqlite3

sql_query = """
CREATE TABLE filenames (
 id INTEGER PRIMARY KEY,
 filename TEXT NOT NULL
);

CREATE TABLE intonation_units (
 id INTEGER PRIMARY KEY,
 filename TEXT NOT NULL,
 unit TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL
);

CREATE TABLE words (
 id INTEGER PRIMARY KEY,
 filename TEXT NOT NULL,
 unit TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL
);

CREATE TABLE transcription (
 id INTEGER PRIMARY KEY,
 filename TEXT NOT NULL,
 unit TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL
);

CREATE TABLE F0 (
 id INTEGER PRIMARY KEY,
 filename TEXT NOT NULL,
 unit TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL
);
""".strip()

with open("sqlite_create_tables.sql", "w", encoding="UTF-8") as wh:
  wh.write(sql_query)