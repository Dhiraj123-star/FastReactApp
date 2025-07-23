import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    db_url = os.getenv("DATABASE_URL", "test.db")
    conn = sqlite3.connect(db_url)
    conn.row_factory = sqlite3.Row
    return conn