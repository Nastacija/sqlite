sql_drop = """
DROP TABLE IF EXISTS filenames;
DROP TABLE IF EXISTS intonation_units;
DROP TABLE IF EXISTS words;
DROP TABLE IF EXISTS transcription;
DROP TABLE IF EXISTS f0
""".strip()

with open("sqlite_drop_tables.sql", "w", encoding="UTF-8") as wh:
  wh.write(sql_drop)