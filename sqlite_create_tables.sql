CREATE TABLE filenames (
 id TEXT NOT NULL PRIMARY KEY,
 filename TEXT NOT NULL
);

CREATE TABLE intonation_units (
 id INTEGER PRIMARY KEY,
 N_sint INTEGER,
 type TEXT NOT NULL,
 content TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL,
 file_id TEXT NOT NULL,
 FOREIGN KEY (file_id)  REFERENCES filenames (id)
);

CREATE TABLE words (
 id INTEGER PRIMARY KEY,
 N_word INTEGER,
 word TEXT NOT NULL,
 transcription TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL,
 sint_id INTEGER,
 file_id TEXT NOT NULL,
 FOREIGN KEY (sint_id)  REFERENCES intonation_units (id),
 FOREIGN KEY (file_id)  REFERENCES filenames (id)
);

CREATE TABLE transcription (
 id INTEGER PRIMARY KEY,
 file_id TEXT NOT NULL,
 alloph TEXT NOT NULL,
 start REAL NOT NULL,
 end REAL NOT NULL,
 word_id INTEGER,
 FOREIGN KEY (file_id)  REFERENCES filenames (id),
 FOREIGN KEY (word_id)  REFERENCES words (id)
);