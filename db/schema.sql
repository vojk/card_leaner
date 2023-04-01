CREATE TABLE quizes
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    questions TEXT NOT NULL,
    answers   TEXT NOT NULL,
    card_set  TEXT
);

CREATE TABLE card_sets
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);