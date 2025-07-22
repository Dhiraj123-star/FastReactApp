import sqlite3

def create_table():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
