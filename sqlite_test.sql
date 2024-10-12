CREATE TABLE companies
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id)  REFERENCES companies (id)
);