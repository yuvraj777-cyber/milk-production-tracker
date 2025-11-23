import sqlite3
from pathlib import Path

# Path to the database file (milk.db) inside data/ folder
DB_PATH = Path(__file__).parent.parent / "data" / "milk.db"

def get_conn():
    """
    Create data folder if missing and return sqlite3 connection.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH.as_posix())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Create tables if they do not exist.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        address TEXT
    );

    CREATE TABLE IF NOT EXISTS animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER,
        tag_id TEXT UNIQUE,
        name TEXT,
        dob TEXT,
        breed TEXT,
        lactation_start_date TEXT,
        FOREIGN KEY(farmer_id) REFERENCES farmers(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS milk_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER NOT NULL,
        entry_date TEXT NOT NULL,
        morning_liters REAL DEFAULT 0,
        evening_liters REAL DEFAULT 0,
        total_liters REAL DEFAULT 0,
        notes TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY(animal_id) REFERENCES animals(id) ON DELETE CASCADE
    );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database successfully created at:", DB_PATH)

