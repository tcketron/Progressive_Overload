CREATE TABLE IF NOT EXISTS workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    notes TEXT,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS legs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    set_number INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workout (id)
);

CREATE TABLE IF NOT EXISTS push (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    set_number INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workout (id)
);

CREATE TABLE IF NOT EXISTS pull (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    set_number INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workout (id)
);

